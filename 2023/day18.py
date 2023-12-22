from tqdm import trange

file = open("input.txt")
lines = file.read().splitlines()

DIRECTIONS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
DIR_IND = ["R", "D", "L", "U"]


def capacity(borders):
    """
    Ray casting algorithm to count the number of cubes in a 2D space.
    Too slow for part 2.
    """
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


def calculate_area(corners):
    """
    Shoelace formula to calculate the area of a polygon.
    """
    return (
        sum(corners[i][0] * corners[i + 1][1] - corners[i + 1][0] * corners[i][1] for i in range(len(corners) - 1)) // 2
    )


def trace(instructions):
    current_pos = (0, 0)
    last_dir = ""
    corners = [current_pos]
    for dir, count in instructions:
        match last_dir + dir:
            case "UR" | "RU":
                corners.append(current_pos)
            case "RD" | "DR":
                corners.append((current_pos[0] + 1, current_pos[1]))
            case "DL" | "LD":
                corners.append((current_pos[0] + 1, current_pos[1] + 1))
            case "LU" | "UL":
                corners.append((current_pos[0], current_pos[1] + 1))
        current_pos = (current_pos[0] + DIRECTIONS[dir][0] * count, current_pos[1] + DIRECTIONS[dir][1] * count)
        last_dir = dir

    corners.append((0, 0))
    print(corners)
    return calculate_area(corners)

    # visited = set()
    # for dir, count in instructions:
    # for _ in range(count):
    #     current_pos = (current_pos[0] + DIRECTIONS[dir][0], current_pos[1] + DIRECTIONS[dir][1])
    #     visited.add(current_pos)
    # return capacity(visited)


def part1():
    instructions = []
    for line in lines:
        dir, count = line.split()[:-1]
        instructions.append((dir, int(count)))

    return trace(instructions)


def part2():
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
