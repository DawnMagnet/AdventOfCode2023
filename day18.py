x = open("input_day18.txt", "r").read().splitlines()
S = 0
cur = (0, 0)
direc = [0, 1, 0, -1, 0]
tr_direc = "RDLU"
border_point = 0
for line in x:
    a, b, c = line.split()

    # Part 1
    d = tr_direc.index(a)
    b = int(b)
    # Part 2
    # d = int(c[2:-1], 16) % 16
    # b = int(c[2:-1], 16) // 16

    border_point += b
    x1, y1 = cur
    x2, y2 = x1 + direc[d] * b, y1 + direc[d + 1] * b
    S += x1 * y2 - y1 * x2
    cur = (x2, y2)
S //= 2
inner_point = abs(S) + 1 - border_point // 2
print(inner_point + border_point)
