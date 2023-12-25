from tqdm import tqdm

tr = []
with open("input_day5.txt", "r") as f:
    k = f.read().split("\n\n")
    seeds = list(map(int, k[0][7:].split()))
    tr = [
        list(map(lambda x: list(map(int, x.split())), z.split("\n")[1:])) for z in k[1:]
    ]


def get_location(cur):
    for trc in tr:
        nxt = -1
        for line in trc:
            if line[1] <= cur < line[1] + line[2]:
                nxt = line[0] + cur - line[1]
                break
        else:
            nxt = cur
        cur = nxt
    return cur


# Part 1
print(min(map(get_location, seeds)))


# Part 2
lx = 100000000000000000
for i in range(len(seeds) // 2):
    for j in tqdm(range(seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1])):
        lx = min(lx, get_location(j))
        # lx.append(get_location(j))
print(lx)
