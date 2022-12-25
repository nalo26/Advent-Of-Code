file = open("input.txt")

lines = file.read().splitlines()


def incrementCycle(cycle, x, row):
    cycle += 1
    if cycle != 1 and cycle % 40 == 1:
        row += 1
    lit = cycle % 40 in range(x, x+3)
    return cycle, row, "#" if lit else "."


x = 1
cycle = 0
row = 0
screen = ["" for _ in range(6)]
for i, line in enumerate(lines, 1):
    cycle, row, px = incrementCycle(cycle, x, row)
    screen[row] += px
    if line.startswith("addx"):
        cycle, row, px = incrementCycle(cycle, x, row)
        x += int(line.split()[1])
        screen[row] += px

print("\n".join(screen))
