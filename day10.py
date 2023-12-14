# east 1 south 2 west 4 north 8
# | {10} - {5} L {9} J {12} 7 {6} F {3} .{0}

import sys  # 导入sys模块

sys.setrecursionlimit(1000000)  # 将默认的递归深度修改为3000
symbol = {".": 0, "F": 3, "-": 5, "7": 6, "L": 9, "|": 10, "J": 12}
directions_tr = {1: 4, 4: 1, 2: 8, 8: 2}
directions = {1: (0, 1), 2: (1, 0), 4: (0, -1), 8: (-1, 0)}
with open("input_day10.txt", "r") as f:
    map = [list(t) for t in f.readlines()]
h, w = len(map), len(map[-1])
poss = (0, 0)
for i in range(h):
    for j in range(w):
        if map[i][j] == "S":
            poss = (i, j)

vis = [[False for _ in range(w)] for _ in range(h)]

res = 0
rpath = []


def dfs(x, y, direc, cnt, path):
    global res, rpath
    if not (0 <= x < h and 0 <= y < w):
        return
    if map[x][y] == "S":
        res = max(res, cnt // 2)
        rpath = path.copy()
        return
    if symbol[map[x][y]] & direc == 0:
        return
    if vis[x][y]:
        return

    vis[x][y] = True
    nxt_direc = symbol[map[x][y]] ^ direc
    path.append((x, y, direc, directions_tr[nxt_direc]))
    dfs(
        x + directions[nxt_direc][0],
        y + directions[nxt_direc][1],
        directions_tr[nxt_direc],
        cnt + 1,
        path,
    )
    vis[x][y] = False
    path.pop()


for i in range(4):
    d = 1 << i
    dfs(poss[0] + directions[d][0], poss[1] + directions[d][1], directions_tr[d], 1, [])
print(res)

for x, y, d, d1 in rpath:
    map[x][y] += "*"
map[poss[0]][poss[1]] += "*"
for i in range(h):
    for j in range(w):
        if not map[i][j].endswith("*"):
            map[i][j] = " "
        else:
            map[i][j] = map[i][j][:-1]
for x, y, d, d1 in rpath:
    if (d == 2 or d1 == 2) and 0 <= x < h and 0 <= y - 1 < w and map[x][y - 1] == " ":
        map[x][y - 1] = "B"
    if (d == 2 or d1 == 2) and 0 <= x < h and 0 <= y + 1 < w and map[x][y + 1] == " ":
        map[x][y + 1] = "A"
    if (d == 8 or d1 == 8) and 0 <= x < h and 0 <= y - 1 < w and map[x][y - 1] == " ":
        map[x][y - 1] = "A"
    if (d == 8 or d1 == 8) and 0 <= x < h and 0 <= y + 1 < w and map[x][y + 1] == " ":
        map[x][y + 1] = "B"
    if (d == 4 or d1 == 4) and 0 <= x + 1 < h and 0 <= y < w and map[x + 1][y] == " ":
        map[x + 1][y] = "A"
    if (d == 4 or d1 == 4) and 0 <= x - 1 < h and 0 <= y < w and map[x - 1][y] == " ":
        map[x - 1][y] = "B"
    if (d == 1 or d1 == 1) and 0 <= x + 1 < h and 0 <= y < w and map[x + 1][y] == " ":
        map[x + 1][y] = "B"
    if (d == 1 or d1 == 1) and 0 <= x - 1 < h and 0 <= y < w and map[x - 1][y] == " ":
        map[x - 1][y] = "A"


def dfs(x, y, ch):
    for dx, dy in directions.values():
        if 0 <= x + dx < h and 0 <= y + dy < w and map[x + dx][y + dy] == " ":
            map[x + dx][y + dy] = ch
            dfs(x + dx, y + dy, ch)


for i in range(h):
    for j in range(w):
        if map[i][j] == "A" or map[i][j] == "B":
            dfs(i, j, map[i][j])


print("".join(["".join(t) for t in map]))

acnt = 0
bcnt = 0
for i in range(h):
    for j in range(w):
        if map[i][j] == "A":
            acnt += 1
        elif map[i][j] == "B":
            bcnt += 1
        elif map[i][j] == " ":
            print("WRONG", i, j)
print("A: ", acnt)
print("B: ", bcnt)
