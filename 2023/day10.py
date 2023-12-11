file = open("input.txt")
lines = file.readlines()
# L └ / J ┘ / 7 ┐ / F ┌


def get_start():
    pos = (None, None)
    for i, line in enumerate(lines):
        if "S" in line:
            pos = (i, line.index("S"))
            break
    if lines[pos[0] + 1][pos[1]] in ("L", "J"):
        pos = (pos[0] + 1, pos[1])
        direction = "down"
    elif lines[pos[0] - 1][pos[1]] in ("7", "F"):
        pos = (pos[0] - 1, pos[1])
        direction = "up"
    elif lines[pos[0]][pos[1] + 1] in ("J", "7"):
        pos = (pos[0], pos[1] + 1)
        direction = "right"
    elif lines[pos[0]][pos[1] - 1] in ("L", "F"):
        pos = (pos[0], pos[1] - 1)
        direction = "left"
    return pos, direction


def go_through(pos, direction):
    path = set()
    path.add(pos)
    while True:
        match lines[pos[0]][pos[1]]:
            case "L":
                direction = "right" if direction == "down" else "up"
            case "J":
                direction = "left" if direction == "down" else "up"
            case "7":
                direction = "left" if direction == "up" else "down"
            case "F":
                direction = "right" if direction == "up" else "down"

        match direction:
            case "up":
                pos = (pos[0] - 1, pos[1])
            case "down":
                pos = (pos[0] + 1, pos[1])
            case "left":
                pos = (pos[0], pos[1] - 1)
            case "right":
                pos = (pos[0], pos[1] + 1)

        path.add((pos[0], pos[1]))
        if lines[pos[0]][pos[1]] == "S":
            return path


def part1():
    pos, direction = get_start()
    path = go_through(pos, direction)

    return len(path) // 2


def part2():
    pos, direction = get_start()
    path = go_through(pos, direction)

    count = 0
    north_char = {"L", "J", "|"}
    for i, line in enumerate(lines):
        is_inside = False
        for j, char in enumerate(line):
            if (i, j) in path:
                if char in north_char:
                    is_inside = not is_inside
            else:
                count += 1 if is_inside else 0
    return count


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
