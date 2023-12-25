# %% [markdown]
# ## Part One

# %%
INPUT_FILE_PATH="input.txt"

# %%
s = 0
d = [str(i + 1) for i in range(9)]

with open(INPUT_FILE_PATH, "r") as f:
    for line in f.readlines():
        left = (1e10, 0)
        right = (-1e10, 0)
        for i, z in enumerate(d):
            posl = line.find(z)
            posr = line.rfind(z)
            if posl != -1 and posl < left[0]:
                left = (posl, i % 9 + 1)
            if posr != -1 and posr > right[0]:
                right = (posr, i % 9 + 1)
        s += left[1] * 10 + right[1]
print(s)

# %% [markdown]
# ## Part Two

# %%
s = 0
d = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d = [str(i + 1) for i in range(9)] + d

with open(INPUT_FILE_PATH, "r") as f:
    for line in f.readlines():
        left = (1e10, 0)
        right = (-1e10, 0)
        for i, z in enumerate(d):
            posl = line.find(z)
            posr = line.rfind(z)
            if posl != -1 and posl < left[0]:
                left = (posl, i % 9 + 1)
            if posr != -1 and posr > right[0]:
                right = (posr, i % 9 + 1)
        s += left[1] * 10 + right[1]
print(s)

# %%



