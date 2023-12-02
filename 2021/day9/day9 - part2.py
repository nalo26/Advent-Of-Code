file = open("input.txt")
lines = file.readlines()

heightmap = []
for line in lines:
    heightmap.append(list(map(int, line.replace("\n", ""))))

lowpoints = []
for y, line in enumerate(heightmap):  # determining lowest points
    for x, n in enumerate(line):
        if y > 0 and n >= heightmap[y - 1][x]:
            continue  # up
        try:
            if n >= heightmap[y + 1][x]:
                continue  # down
        except IndexError:
            pass
        if x > 0 and n >= heightmap[y][x - 1]:
            continue  # left
        try:
            if n >= heightmap[y][x + 1]:
                continue  # right
        except IndexError:
            pass
        lowpoints.append((x, y))


for i, line in enumerate(heightmap):
    heightmap[i] = [n if n == 9 else 0 for n in line]

sizes = []
for col, row in lowpoints:
    locSize = 0
    toVisit = []
    try:
        if heightmap[row + 1][col] != 9:
            toVisit.append((col, row + 1))
    except IndexError:
        pass
    if row > 0 and heightmap[row - 1][col] != 9:
        toVisit.append((col, row - 1))
    try:
        if heightmap[row][col + 1] != 9:
            toVisit.append((col + 1, row))
    except IndexError:
        pass
    if col > 0 and heightmap[row][col - 1] != 9:
        toVisit.append((col - 1, row))
    while len(toVisit) > 0:
        _toVisit = []
        for x, y in toVisit:
            locSize += 1  # count the cell
            heightmap[y][x] += 1  # set cell as visited

            try:
                if heightmap[y + 1][x] == 0 and (x, y + 1) not in _toVisit:
                    _toVisit.append((x, y + 1))
            except IndexError:
                pass
            if y > 0 and heightmap[y - 1][x] == 0 and (x, y - 1) not in _toVisit:
                _toVisit.append((x, y - 1))
            try:
                if heightmap[y][x + 1] == 0 and (x + 1, y) not in _toVisit:
                    _toVisit.append((x + 1, y))
            except IndexError:
                pass
            if x > 0 and heightmap[y][x - 1] == 0 and (x - 1, y) not in _toVisit:
                _toVisit.append((x - 1, y))
        toVisit = _toVisit.copy()
        del _toVisit
    sizes.append(locSize)

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
