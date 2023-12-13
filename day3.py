# %%

with open("input_day3.txt", "r") as f:
    x = [line.replace("\n", "") + "." for line in f]
h, w = len(x), len(x[0])

# %% [markdown]
# # Part 1

# %%
def check(it, sj, ej):
    for i in range(it - 1, it + 2):
        for j in range(sj - 1, ej + 2):
            if 0 <= i < h and 0 <= j < w:
                if not x[i][j].isdigit() and x[i][j] != ".":
                    return True
    return False


res = 0
for i in range(h):
    cur = [-1, 0]
    for j in range(w):
        if x[i][j].isdigit():
            if cur[0] == -1:
                cur = [j, 0]
            cur[1] = cur[1] * 10 + ord(x[i][j]) - ord("0")
        elif cur[0] != -1:
            if check(i, cur[0], j - 1):
                res += cur[1]
            cur = [-1, 0]
print(res)

# %% [markdown]
# # Part 2

# %%
from collections import defaultdict


d = defaultdict(list)
def check(it, sj, ej, val):
    for i in range(it - 1, it + 2):
        for j in range(sj - 1, ej + 2):
            if 0 <= i < h and 0 <= j < w:
                if x[i][j] == "*":
                    d[(i, j)].append(val)



for i in range(h):
    cur = [-1, 0]
    for j in range(w):
        if x[i][j].isdigit():
            if cur[0] == -1:
                cur = [j, 0]
            cur[1] = cur[1] * 10 + ord(x[i][j]) - ord("0")
        elif cur[0] != -1:
            check(i, cur[0], j - 1, cur[1])
            cur = [-1, 0]
res = 0
for v in d.values():
    if len(v) == 2:
        res += v[0] * v[1]
res

# %%



