# %% [markdown]
# # Part 1

# %%
default_dict = {"red": 12, "green": 13, "blue": 14}


def deal(line):
    line = line.replace(":", ";").replace(",", " ").split(";")[1:]
    for z in line:
        z = z.split()
        z = {z[i * 2 + 1]: int(z[i * 2]) for i in range(len(z) // 2)}
        for k, v in z.items():
            if default_dict[k] < v:
                yield False
    yield True

res = 0
with open("input_day2.txt", "r") as f:
    for i, line in enumerate(f):
        if all(deal(line)):
            res += 1 + i
res

# %% [markdown]
# # Part 2

# %%
def deal(line):
    res = {"red": 0, "green": 0, "blue": 0}
    line = line.replace(":", ";").replace(",", " ").split(";")[1:]
    for z in line:
        z = z.split()
        z = {z[i * 2 + 1]: int(z[i * 2]) for i in range(len(z) // 2)}
        for k, v in z.items():
            res[k] = max(res[k], v)
    return res["red"] * res ["green"] * res["blue"]


res = 0
with open("input_day2.txt", "r") as f:
    for i, line in enumerate(f):
        res += deal(line)
res

# %%



