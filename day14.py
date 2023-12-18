from copy import deepcopy

from tqdm import tqdm

x = list(map(list, open("input_day14.txt").read().split("\n")))
h, w = len(x), len(x[0])
res = 0


def calculate(xt):
    res = 0
    for i in range(h):
        for j in range(w):
            if xt[i][j] == "O":
                res += h - i
    return res


def show(xt):
    for l in xt:
        print("".join(l))
    print()


def north(xt):
    for i in range(w):
        cnt_pos = 0
        for j in range(h):
            if xt[j][i] == "O":
                xt[j][i] = "."
                xt[cnt_pos][i] = "O"
                cnt_pos += 1
            elif xt[j][i] == "#":
                cnt_pos = j + 1


def south(xt):
    for i in range(w):
        cnt_pos = h - 1
        for j in reversed(range(h)):
            if xt[j][i] == "O":
                xt[j][i] = "."
                xt[cnt_pos][i] = "O"
                cnt_pos -= 1
            elif xt[j][i] == "#":
                cnt_pos = j - 1


def west(xt):
    for i in range(h):
        cnt_pos = 0
        for j in range(w):
            if xt[i][j] == "O":
                xt[i][j] = "."
                xt[i][cnt_pos] = "O"
                cnt_pos += 1
            elif xt[i][j] == "#":
                cnt_pos = j + 1


def east(xt):
    for i in range(h):
        cnt_pos = w - 1
        for j in reversed(range(w)):
            if xt[i][j] == "O":
                xt[i][j] = "."
                xt[i][cnt_pos] = "O"
                cnt_pos -= 1
            elif xt[i][j] == "#":
                cnt_pos = j - 1


def group(xt):
    north(xt)
    west(xt)
    south(xt)
    east(xt)


# Part 1
north(x)
print(calculate(x))

# Part 2
x = list(map(list, open("input_day14.txt").read().split("\n")))
xp = None
cnt = 0

cc = []
while True:
    cc.append(deepcopy(x))
    group(x)
    for i in range(1, min(50, len(cc) + 1)):
        if cc[-i] == x:
            print("Circle detected!")
            circle_loop = i
            print(circle_loop)
            cur_index = len(cc) - i
            div = (1000000000 - cur_index) % i
            print("ans:", calculate(cc[cur_index + div]))

            exit(0)
