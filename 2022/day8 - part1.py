file = open("input.txt")
lines = file.read().splitlines()
forest = [list(map(int, list(line))) for line in lines]


def isVisible(x, y, v, grid):
    if x in (0, len(grid[0]) - 1) or y in (0, len(grid) - 1):
        return True

    up = all(l[x] < v for l in grid[:y])
    left = all(t < v for t in grid[y][:x])
    down = all(l[x] < v for l in grid[y + 1 :])
    right = all(t < v for t in grid[y][x + 1 :])

    return up or left or down or right


count = 0
for y, line in enumerate(forest):
    for x, tree in enumerate(line):
        count += int(isVisible(x, y, tree, forest))

print(count)
