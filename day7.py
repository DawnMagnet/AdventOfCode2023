from collections import Counter
import numpy as np


# Part 1
def get_value(ch: str):
    if len(ch) == 1:
        return 13 - "AKQJT98765432".index(ch)
    else:
        return get_value(ch[:-1]) * 14 + get_value(ch[-1])


def parse(origin: str):
    a = sorted(list(Counter(origin).items()), key=lambda x: (-x[1], -get_value(x[0])))
    a = np.array(a)
    pat = "".join(a[:, 1])
    chs = "".join(a[:, 0])
    pats = ["5", "41", "32", "311", "221", "2111", "11111"]
    return (7 - pats.index(pat), get_value(origin))


with open("input_day7.txt", "r") as f:
    d = [(int(v), parse(k)) for k, v in map(lambda x: x.split(), f)]

res = 0
d = sorted(d, key=lambda x: x[1])
for i, (k, _) in enumerate(d):
    # print(d[i])
    res += (i + 1) * k
print(res)


# Part 2
def get_value(ch: str):
    if len(ch) == 1:
        return 13 - "AKQT98765432J".index(ch)
    else:
        return get_value(ch[:-1]) * 14 + get_value(ch[-1])


def parse(origin: str):
    jcnt = origin.count("J")

    a = sorted(
        list(Counter(origin.replace("J", "")).items()),
        key=lambda x: (-x[1], -get_value(x[0])),
    )
    if len(a) > 0:
        a[0] = (a[0][0], a[0][1] + jcnt)
    else:
        a = [("J", 5)]
    a = np.array(a)
    pat = "".join(a[:, 1])
    chs = "".join(a[:, 0])
    pats = ["5", "41", "32", "311", "221", "2111", "11111"]
    return (7 - pats.index(pat), get_value(origin))


with open("input_day7.txt", "r") as f:
    d = [(int(v), parse(k)) for k, v in map(lambda x: x.split(), f)]

res = 0
d = sorted(d, key=lambda x: x[1])
for i, (k, _) in enumerate(d):
    # print(d[i])
    res += (i + 1) * k
print(res)
