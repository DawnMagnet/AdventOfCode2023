import sys

sys.setrecursionlimit(10000000)
map = open("input_day16.txt", "r").read().splitlines()
h, w = len(map), len(map[0])
vis = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]
direc = [0, 1, 0, -1, 0]
slash = [3, 2, 1, 0]
backslash = [1, 0, 3, 2]


def dfs(x, y, d):
    global vis
    x += direc[d]
    y += direc[d + 1]
    if not (0 <= x < h and 0 <= y < w) or vis[x][y][d] == 1:
        return
    vis[x][y][d] = 1
    if map[x][y] == ".":
        dfs(x, y, d)
    elif map[x][y] == "/":
        dfs(x, y, slash[d])
    elif map[x][y] == "\\":
        dfs(x, y, backslash[d])
    elif map[x][y] == "|":
        if d == 1 or d == 3:
            dfs(x, y, d)
        else:
            dfs(x, y, 1)
            dfs(x, y, 3)
    else:
        if d == 0 or d == 2:
            dfs(x, y, d)
        else:
            dfs(x, y, 0)
            dfs(x, y, 2)


# Part 1
dfs(0, -1, 0)
res = sum(sum(max(x) for x in b) for b in vis)
print(res)


# Part 2
rres = 0
for i in range(h):
    vis = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]
    dfs(i, -1, 0)
    res = sum(sum(max(x) for x in b) for b in vis)
    rres = max(rres, res)

    vis = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]
    dfs(i, w, 2)
    res = sum(sum(max(x) for x in b) for b in vis)
    rres = max(rres, res)

for i in range(w):
    vis = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]
    dfs(-1, i, 1)
    res = sum(sum(max(x) for x in b) for b in vis)
    rres = max(rres, res)

    vis = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]
    dfs(h, i, 3)
    res = sum(sum(max(x) for x in b) for b in vis)
    rres = max(rres, res)
print(rres)
