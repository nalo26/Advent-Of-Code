file = open("input.txt")
lines = file.read().splitlines()

count = 0
for line in lines:
    a, b = line.split(",")
    a = tuple(map(int, a.split("-")))
    b = tuple(map(int, b.split("-")))
    if a[0] <= b[0] and a[1] >= b[1] or b[0] <= a[0] and b[1] >= a[1]:
        count += 1

    # Another method, inspired by the 2nd part of today's exercise:
    # start1, stop1 = tuple(map(int, a.split("-")))
    # start2, stop2 = tuple(map(int, b.split("-")))
    # range1 = range(start1, stop1+1)
    # range2 = range(start2, stop2+1)
    # ovrlp = set(range1) & set(range2)
    # if len(ovrlp) in (len(range1), len(range2)):
    #     count += 1

print(count)
