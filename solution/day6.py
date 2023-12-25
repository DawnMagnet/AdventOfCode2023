# Part 1
with open("input_day6.txt", "r") as f:
    t, d = f.readlines()
    t = list(map(int, t[5:].split()))
    d = list(map(int, d[9:].split()))
    data = list(zip(t, d))

res = 1
for a, b in data:
    k = a // 2
    l, r = 0, k
    while l < r:
        mid = (l + r) // 2
        if mid * (a - mid) < b:
            l = mid + 1
        else:
            r = mid
    resd = (k - l + 1) * 2
    if k * 2 == a:
        resd -= 1
    res *= resd
    print((a, b), l, k - l + 1)
print(res)


# Part 2
with open("input_day6.txt", "r") as f:
    t, d = f.readlines()
    t = list(map(int, t[5:].replace(" ", "").split()))
    d = list(map(int, d[9:].replace(" ", "").split()))
    data = list(zip(t, d))

res = 1
for a, b in data:
    k = a // 2
    l, r = 0, k
    while l < r:
        mid = (l + r) // 2
        if mid * (a - mid) < b:
            l = mid + 1
        else:
            r = mid
    resd = (k - l + 1) * 2
    if k * 2 == a:
        resd -= 1
    res *= resd
    print((a, b), l, k - l + 1)
print(res)
