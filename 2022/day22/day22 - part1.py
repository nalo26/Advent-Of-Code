import re


file = open("input.txt")
lines = file.read().splitlines()

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

instruction = re.findall("[LR]|\d+", lines[-1])
map = lines[:-2]
l = max(len(row) for row in map)
map = [row + " " * (l - len(row)) for row in map]


def goForward(pos, dir):
    x, y = pos
    dir = DIRECTIONS[dir]
    nx, ny = x + dir[0], y + dir[1]
    if 0 <= ny < len(map) and 0 <= nx < len(map[ny]):
        if map[ny][nx] == ".":
            return (nx, ny), True
        if map[ny][nx] == "#":
            return pos, False

    # out of map of empty space
    if dir[0] != 0:  # R or L
        if dir[0] == 1:  # R
            p, w = map[ny].index("."), map[ny].index("#") if "#" in map[ny] else float(
                "inf"
            )
            if p < w:
                return (p, ny), True
        else:  # L
            p, w = map[ny].rindex("."), map[ny].rindex("#") if "#" in map[ny] else -1
            if p > w:
                return (p, ny), True

    else:  # D or U
        line = "".join(col[nx] for col in map)
        if dir[1] == 1:  # D
            p, w = line.index("."), line.index("#") if "#" in line else float("inf")
            if p < w:
                return (nx, p), True
        else:  # U
            p, w = line.rindex("."), line.rindex("#") if "#" in line else -1
            if p > w:
                return (nx, p), True

    return pos, False


direction = 0
position = (map[0].index("."), 0)
for i in instruction:
    if i.isdigit():
        for _ in range(int(i)):
            position, hasmoved = goForward(position, direction)
            if not hasmoved:
                break
    else:
        d = 1 if i == "R" else -1
        direction = (direction + d) % 4

print(1000 * (position[1] + 1) + 4 * (position[0] + 1) + direction)
