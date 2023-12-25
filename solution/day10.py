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
        rpath = path.copy() + [(*poss, direc)]
        return
    if symbol[map[x][y]] & direc == 0:
        return
    if vis[x][y]:
        return

    vis[x][y] = True
    nxt_direc = symbol[map[x][y]] ^ direc
    path.append((x, y, direc))
    dfs(
        x + directions[nxt_direc][0],
        y + directions[nxt_direc][1],
        directions_tr[nxt_direc],
        cnt + 1,
        path,
    )
    vis[x][y] = False
    path.pop()


# Part 1
for i in range(4):
    d = 1 << i
    dfs(poss[0] + directions[d][0], poss[1] + directions[d][1], directions_tr[d], 1, [])
print(res)


# Part 2 Calculate Square
base_point = (0, 0)
S = 0
for i in range(len(rpath)):
    x1, y1, d = rpath[i]
    x2, y2, _ = rpath[(i + 1) % len(rpath)]
    S += x1 * y2 - y1 * x2
S //= 2
print("Square: ", abs(S))
print(abs(S) + 1 - len(rpath) // 2)
