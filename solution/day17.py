# RUN ABOUT 1 minute
import sys

sys.setrecursionlimit(1000000)
m = open("input_day17.txt", "r").read().splitlines()
direc = [0, 1, 0, -1, 0]
h, w = len(m), len(m[0])
vis = [[[2147483647 for _ in range(4)] for _ in range(w)] for _ in range(h)]
print(h, w)

res = (h + w) * 10


def dfs1(x, y, d, cost):
    global res
    # print(x, y, d, cost)
    if not (0 <= x < h and 0 <= y < w) or vis[x][y][d] <= cost or cost > res:
        return

    vis[x][y][d] = cost
    if x == h - 1 and y == w - 1:
        res = min(res, cost)
        return
    for i in range(3):
        x += direc[d]
        y += direc[d + 1]
        if 0 <= x < h and 0 <= y < w:
            cost += int(m[x][y])
            if d == 1 or d == 3:
                dfs1(x, y, 0, cost)
                dfs1(x, y, 2, cost)
            else:
                dfs1(x, y, 1, cost)
                dfs1(x, y, 3, cost)
        else:
            break


def dfs2(x, y, d, cost):
    global res
    if not (0 <= x < h and 0 <= y < w) or vis[x][y][d] <= cost or cost > res:
        return

    vis[x][y][d] = cost
    if x == h - 1 and y == w - 1:
        res = min(res, cost)
        return
    for i in range(10):
        x += direc[d]
        y += direc[d + 1]
        if not (0 <= x < h and 0 <= y < w):
            return
        cost += int(m[x][y])
        if i >= 3:
            if d == 1 or d == 3:
                dfs2(x, y, 0, cost)
                dfs2(x, y, 2, cost)
            else:
                dfs2(x, y, 1, cost)
                dfs2(x, y, 3, cost)


# Part 1
# dfs1(0, 0, 0, 0)
# dfs1(0, 0, 1, 0)
# Part 2
dfs2(0, 0, 0, 0)
dfs2(0, 0, 1, 0)

print(vis[h - 1][w - 1])
