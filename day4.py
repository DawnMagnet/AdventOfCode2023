# %%
res = 0
with open("input_day4.txt", "r") as f:
    for line in f:
        _, a, b = line.replace(":", "|").split("|")
        a = set(map(int, a.split()))
        b = set(map(int, b.split()))
        c = a & b
        if len(c) > 0:
            res += (1 << ((len(c) - 1)))
print(res)

# %%
res = 0
suffix = [0] * 10000
cur = 1
with open("input_day4.txt", "r") as f:
    for i, line in enumerate(f):
        _, a, b = line.replace(":", "|").split("|")
        a = set(map(int, a.split()))
        b = set(map(int, b.split()))
        c = a & b
        res += cur
        if len(c) > 0:
            suffix[i + len(c)] += cur
            cur *= 2
        cur -= suffix[i]

print(res)

# %%



