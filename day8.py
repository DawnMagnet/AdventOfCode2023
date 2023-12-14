import math

left, right = {}, {}

with open("input_day8.txt", "r") as f:
    z = f.readlines()
    instruction = z[0].strip()
    for line in z[2:]:
        line = (
            line.replace("=", "")
            .replace(",", "")
            .replace("(", "")
            .replace(")", "")
            .split()
        )
        left[line[0]] = line[1]
        right[line[0]] = line[2]


cur = "AAA"
index = 0
while not cur.endswith("Z"):
    if instruction[index % len(instruction)] == "L":
        cur = left[cur]
    else:
        cur = right[cur]
    index += 1
print(index)


# Part 2
def get_path_length(cur):
    index = 0
    while not cur.endswith("Z"):
        if instruction[index % len(instruction)] == "L":
            cur = left[cur]
        else:
            cur = right[cur]
        index += 1
    return index


result = 1
for start in left.keys():
    if start.endswith("A"):
        z = get_path_length(start)
        result = math.lcm(result, z)
print(result)
