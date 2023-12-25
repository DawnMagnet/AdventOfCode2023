from dataclasses import dataclass


def str_hash(s):
    res = 0
    for ch in s:
        res = ((res + ord(ch)) * 17) % 256
    return res


x = open("input_day15.txt", "r").read().split(",")
# Part 1
print(sum(map(str_hash, x)))


# Part 2


focus = dict()
boxes = [[] for _ in range(256)]
for op in x:
    if op.endswith("-"):
        a = op[:-1]
        if a in boxes[str_hash(a)]:
            boxes[str_hash(a)].remove(a)

    else:
        a, b = op.split("=")
        if a not in boxes[str_hash(a)]:
            boxes[str_hash(a)].append(a)
        focus[a] = int(b)
res = 0
for i in range(256):
    for j in range(len(boxes[i])):
        res += (i + 1) * (j + 1) * focus[boxes[i][j]]
print(res)
