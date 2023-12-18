file = open("input.txt")
layout = [line.strip() for line in file.readlines()]

WIDTH, HEIGHT = len(layout[0]), len(layout)
SLASH = {(0, 1): (-1, 0), (0, -1): (1, 0), (1, 0): (0, -1), (-1, 0): (0, 1)}
ANTI_SLASH = {(0, 1): (1, 0), (0, -1): (-1, 0), (1, 0): (0, 1), (-1, 0): (0, -1)}
OPPOSITE = {(0, 1): (0, -1), (0, -1): (0, 1), (1, 0): (-1, 0), (-1, 0): (1, 0)}


def move(pos, dir, taken_spliters=None):
    if taken_spliters is None:
        taken_spliters = set()
    visited = set()
    while True:
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        if not 0 <= pos[0] < len(layout) or not 0 <= pos[1] < len(layout[pos[0]]):
            return visited
        visited.add(pos)

        match layout[pos[0]][pos[1]]:
            case "|":
                if dir in ((1, 0), (-1, 0)):  # UP or DOWN
                    continue  # PASS THROUGH
                # split into two directions
                if (pos, dir) in taken_spliters:
                    return visited
                taken_spliters |= {(pos, dir), (pos, OPPOSITE[dir])}
                return visited | move(pos, (1, 0), taken_spliters) | move(pos, (-1, 0), taken_spliters)
            case "-":
                if dir in ((0, 1), (0, -1)):  # LEFT or RIGHT
                    continue  # PASS THROUGH
                # split into two directions
                if (pos, dir) in taken_spliters:
                    return visited
                taken_spliters |= {(pos, dir), (pos, OPPOSITE[dir])}
                return visited | move(pos, (0, 1), taken_spliters) | move(pos, (0, -1), taken_spliters)
            case "/":
                dir = SLASH[dir]  # rotate
            case "\\":
                dir = ANTI_SLASH[dir]  # rotate
            case ".":
                continue


def part1():
    visited = move((0, -1), (0, 1))
    return len(visited)


def part2():
    energized = set()
    for top in range(WIDTH):
        energized.add(len(move((-1, top), (1, 0))))
    for left in range(HEIGHT):
        energized.add(len(move((left, -1), (0, 1))))
    for bottom in range(WIDTH):
        energized.add(len(move((HEIGHT, bottom), (-1, 0))))
    for right in range(HEIGHT):
        energized.add(len(move((right, WIDTH), (0, -1))))
    return max(energized)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
