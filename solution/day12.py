def get_arrangement1(s, c):
    res = 0
    nw = s.count("?")
    for i in range(1 << nw):
        new_s = ""
        cnt = 0
        for ch in s:
            if ch == "?":
                if ((i >> cnt) & 1) == 1:
                    new_s += "#"
                else:
                    new_s += "."
                cnt += 1
            else:
                new_s += ch
        if c == list(map(len, new_s.replace(".", " ").split())):
            res += 1
            # print(new_s)
    return res


def get_arrangement(s, c):
    s = "." + s + "."
    c = [0] + c
    # print(s, c)
    n = len(s)
    nc = len(c)
    dp = [[0 for _ in range(nc)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(nc - 1):
            if dp[i][j] != 0 and i + 1 + c[j + 1] <= n:
                left = i + 1
                right = i + 1 + c[j + 1]
                while right < n and s[i:left].count("#") == 0:
                    if s[left:right].count(".") == 0 and s[right] != "#":
                        dp[right][j + 1] += dp[i][j]
                        # print(
                        #     f"({i},{j})->({right},{j + 1})   {s[i:left]} {s[left:right]}  {dp[i][j]}"
                        # )
                    right += 1
                    left += 1
    # print(s, sum([i[nc - 1] for i in dp]))
    res = 0
    for i in reversed(range(n)):
        if s[i] != "#":
            res += dp[i][nc - 1]
        else:
            break
    return res


res = 0
with open("input_day12.txt", "r") as f:
    for line in f.readlines():
        a, b = line.split()
        b = list(map(int, b.split(",")))
        res += get_arrangement(a, b)

print(res)

res = 0
with open("input_day12.txt", "r") as f:
    for line in f.readlines():
        a, b = line.split()
        b = list(map(int, b.split(",")))
        res += get_arrangement(f"{a}?{a}?{a}?{a}?{a}", b * 5)

print(res)
