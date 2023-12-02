file = open("input.txt")
seats = [list(line.replace("\n", "")) for line in file.readlines()]
last = [row[:] for row in seats]

floor = "."
empty = "L"
occupied = "#"


def isOccupied(seats, x, y):
    if x < 0 or y < 0:
        return False
    try:
        return seats[y][x] == occupied
    except IndexError:
        return False


def isEmpty(seats, x, y):
    if x < 0 or y < 0:
        return True
    try:
        return seats[y][x] != occupied
    except IndexError:
        return True


def shouldBeOccupied(seats, x, y):
    toTry = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    return len(
        [test for test in toTry if not isOccupied(seats, x + test[0], y + test[1])]
    ) == len(toTry)


def shouldBeEmpty(seats, x, y):
    toTry = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    return (
        len([test for test in toTry if not isEmpty(seats, x + test[0], y + test[1])])
        >= 4
    )


def showMap(seats):
    for line in seats:
        print("".join(line))
    print()


while True:
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if last[y][x] == floor:
                continue
            if last[y][x] == empty:
                seats[y][x] = occupied if shouldBeOccupied(last, x, y) else empty
            if last[y][x] == occupied:
                seats[y][x] = empty if shouldBeEmpty(last, x, y) else occupied
    # showMap(seats)
    if last == seats:
        break
    last = [row[:] for row in seats]


res = 0
for seat in seats:
    res += len([s for s in seat if s == occupied])

print(res)
