x = map(lambda t: t.split("\n"), open("input_day13.txt").read().split("\n\n"))


def check1(x, y):
    return x == y


def check2(x, y):
    n = len(x)
    diff = -1
    for i in range(n):
        if x[i] != y[i]:
            if diff != -1:
                return False
            else:
                diff = i
    if diff == -1:
        return False
    diff = x[diff] ^ y[diff]
    return (diff & (diff - 1)) == 0


res1 = 0
res2 = 0
for block in x:
    row = [eval("0b" + t.replace("#", "1").replace(".", "0")) for t in block]
    col = [
        eval("0b" + "".join([t[i] for t in block]).replace("#", "1").replace(".", "0"))
        for i in range(len(block[0]))
    ]
    cnt = 0
    # print(row, col)
    for lb in range(1, len(row)):
        length = min(lb, len(row) - lb)
        if check1(row[lb - length : lb], row[lb : lb + length][::-1]):
            res1 += lb * 100
            cnt += 1
        if check2(row[lb - length : lb], row[lb : lb + length][::-1]):
            res2 += lb * 100
            cnt += 1

    for lb in range(1, len(col)):
        length = min(lb, len(col) - lb)
        if check1(col[lb - length : lb], col[lb : lb + length][::-1]):
            res1 += lb
            cnt += 1
        if check2(col[lb - length : lb], col[lb : lb + length][::-1]):
            res2 += lb
            cnt += 1


print(res1)
print(res2)
