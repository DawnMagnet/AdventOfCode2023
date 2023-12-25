from collections import deque
import math

x = open("input_day20.txt").read().splitlines()
d = {}
NUM = 100
edge = [[] for _ in range(NUM)]
reverse = [[] for _ in range(NUM)]
kind = [0 for _ in range(NUM)]

broadcast = []
for line in x:
    a, b = line[1:].split(" -> ")
    b = b.replace(" ", "").split(",")
    if a not in d:
        d[a] = len(d)
    kind[d[a]] = line[0]
    for z in b:
        if z not in d:
            d[z] = len(d)
        if line[0] == "&" or line[0] == "%":
            edge[d[a]].append(d[z])
            reverse[d[z]].append(d[a])
        else:
            broadcast.append(d[z])
conj_reverse = {
    i: dict({j: 0 for j in reverse[i]}, **{"sum": 0})
    for i in range(len(d))
    if kind[i] == "&"
}
state = 0
related_rx = reverse[d["rx"]][0]
relatex_array = {t: [] for t in reverse[related_rx]}


def op(itx):
    global state, related_array
    q = deque()
    for b in broadcast:
        q.append((0, b))
    cnt = [1, 0]
    while len(q) > 0:
        p, c = q[0]
        cnt[p] += 1
        q.popleft()
        if kind[c] == "%":
            if p == 0:
                for nxt in edge[c]:
                    q.append((1 - ((state >> c) & 1), nxt))
                    if kind[nxt] == "&":
                        conj_reverse[nxt]["sum"] -= conj_reverse[nxt][c]
                        conj_reverse[nxt][c] = 1 - ((state >> c) & 1)
                        conj_reverse[nxt]["sum"] += conj_reverse[nxt][c]
                state ^= 1 << c
        elif kind[c] == "&":
            s = 0 if conj_reverse[c]["sum"] == len(conj_reverse[c]) - 1 else 1
            for nxt in edge[c]:
                q.append((s, nxt))
                if kind[nxt] == "&":
                    conj_reverse[nxt]["sum"] -= conj_reverse[nxt][c]
                    conj_reverse[nxt][c] = s
                    conj_reverse[nxt]["sum"] += conj_reverse[nxt][c]
            if s == 0:
                if c == d["ff"]:
                    related_array.append(itx + 1)
    return cnt


# Part 1
# cres = [0, 0]
# for i in range(1000):
#     a, b = op()
#     cres[0] += a
#     cres[1] += b
#     # print(i, bin(state))
# print(cres[0] * cres[1])


# Part 2


dp = [0 if kind[i] == "%" else 1 for i in range(NUM)]
for z in broadcast:
    dp[z] = 1
q = deque()
qnxt = deque()
for b in broadcast:
    q.append(b)
while len(q) > 0:
    c = q[0]
    q.popleft()
    for nxt in edge[c]:
        if kind[c] == "%":
            if kind[nxt] == "&":
                dp[nxt] |= dp[c]
                q.append(nxt)
            elif dp[nxt] == 0:
                dp[nxt] = dp[c] * 2
                q.append(nxt)
        else:
            qnxt.append(c)
q = qnxt
while len(q) > 0:
    c = q[0]
    q.popleft()
    for nxt in edge[c]:
        if kind[nxt] != "%":
            dp[nxt] = math.lcm(dp[c], dp[nxt])
            q.append(nxt)
print(dp[d["rx"]])
