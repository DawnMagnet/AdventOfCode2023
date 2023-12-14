def get_ans(seq):
    sseq = [seq]
    res = seq[-1]
    while True:
        cur = []
        allzero = True
        for i in range(len(sseq[-1]) - 1):
            cur.append(sseq[-1][i + 1] - sseq[-1][i])
            if cur[-1] != 0:
                allzero = False
        sseq.append(cur)
        res += cur[-1]
        if allzero:
            break
    return res


# Part 1
res = 0
with open("input_day9.txt", "r") as f:
    for line in f:
        seq = list(map(int, line.split()))
        res += get_ans(seq)
print(res)

# Part 2
res = 0
with open("input_day9.txt", "r") as f:
    for line in f:
        seq = list(map(int, line.split()))
        res += get_ans(seq[::-1])
print(res)
