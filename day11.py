with open("input_day11.txt", "r") as f:
    image = [t.strip() for t in f]


def get_result(NUM):
    dp_row = [-1]
    dp_col = [-1]
    h, w = len(image), len(image[0])
    for i in range(h):
        if all(map(lambda x: x != "#", image[i])):
            dp_row.append(dp_row[-1] + NUM)
        else:
            dp_row.append(dp_row[-1] + 1)
    for i in range(w):
        if all(map(lambda x: x != "#", [image[t][i] for t in range(h)])):
            dp_col.append(dp_col[-1] + NUM)
        else:
            dp_col.append(dp_col[-1] + 1)
    dp_row = dp_row[1:]
    dp_col = dp_col[1:]
    # print(dp_row, dp_col)

    galaxies = []
    for i in range(h):
        for j in range(w):
            if image[i][j] == "#":
                galaxies.append((dp_row[i], dp_col[j]))
    res = 0
    for i in range(len(galaxies)):
        for j in range(i):
            res += abs(galaxies[i][0] - galaxies[j][0]) + abs(
                galaxies[i][1] - galaxies[j][1]
            )
    return res


# Part 1
print(get_result(2))
# Part 2
print(get_result(1000000))
