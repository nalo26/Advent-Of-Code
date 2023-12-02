file = open("input.txt")

res = []
for line in file.readlines():
    mi, ma = 0, 127
    for char in line[:6]:  # F & B
        if char == "F":
            ma -= (ma - mi) // 2 + 1
        if char == "B":
            mi += (ma - mi) // 2 + 1
    row = mi if line[6] == "F" else ma

    mi, ma = 0, 7
    for char in line[7:]:  # L & R
        if char == "L":
            ma -= (ma - mi) // 2 + 1
        if char == "R":
            mi += (ma - mi) // 2 + 1
    col = mi if line[9] == "L" else ma

    res.append(row * 8 + col)

# print(max(res))

res.sort()
print(res)

last = res[0]
for n in range(1, len(res) - 1):
    if res[n] != last + 1:
        print(res[n] - 1)
    last = res[n]
