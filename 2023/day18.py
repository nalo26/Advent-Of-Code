from tqdm import trange

file = open("input.txt")
lines = file.read().splitlines()

DIRECTIONS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
DIR_IND = ["R", "D", "L", "U"]


def capacity(borders):
    cubes = 0
    for y in trange(min(borders, key=lambda x: x[1])[1], max(borders, key=lambda x: x[1])[1] + 1):
        is_in = False
        for x in range(min(borders, key=lambda x: x[0])[0], max(borders, key=lambda x: x[0])[0] + 1):
            if is_in and (x, y) not in borders:
                cubes += 1
                continue

            if (x, y) in borders:
                cubes += 1
                if (x, y + 1) in borders:
                    is_in = not (is_in)
    return cubes


def trace(instructions):
    current_pos = (0, 0)
    visited = set()
    for dir, count in instructions:
        for _ in range(count):
            current_pos = (current_pos[0] + DIRECTIONS[dir][0], current_pos[1] + DIRECTIONS[dir][1])
            visited.add(current_pos)
    return capacity(visited)


def part1():
    instructions = []
    for line in lines:
        dir, count = line.split()[:-1]
        instructions.append((dir, int(count)))

    return trace(instructions)


def part2():  # too slow!
    instructions = []
    for line in lines:
        color = line.split()[-1].strip("(#)")
        dir = DIR_IND[int(color[-1])]
        count = int(color[:-1], 16)
        instructions.append((dir, count))

    return trace(instructions)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
