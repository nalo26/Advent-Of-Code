file = open("input.txt")

res = 0
for entry in file.readlines():
    line = entry.split(" ")
    mi, ma = line[0].split("-")
    letter = line[1][0]
    pwd = line[2]

    count = 0
    for l in pwd:
        if l == letter:
            count += 1
    if int(mi) <= count <= int(ma):
        res += 1

print(res)
