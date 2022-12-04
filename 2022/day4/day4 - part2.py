file = open("input.txt")
lines = file.read().splitlines()

count = 0
for line in lines:
    a, b = line.split(",")
    start1, stop1 = tuple(map(int, a.split("-")))
    start2, stop2 = tuple(map(int, b.split("-")))
    ovrlp = set(range(start1, stop1+1)) & set(range(start2, stop2+1))
    if len(ovrlp) != 0:
        count += 1

print(count)
