file = open("input.txt")
lines = file.read().splitlines()
lines = [list(line) for line in lines]

for y, line in enumerate(lines):
    if "^" in line:
        start_pos = (line.index("^"), y)

CARDS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # UP, RIGHT, DOWN, LEFT


def try_route(map: list[list[str]]) -> set[tuple[int, int]]:
    card_i = 0  # starting looking up
    pos = start_pos
    visited = {(pos, card_i)}
    while True:
        while (
            0 <= pos[1] + CARDS[card_i][1] < len(map)
            and 0 <= pos[0] + CARDS[card_i][0] < len(map[0])
            and map[pos[1] + CARDS[card_i][1]][pos[0] + CARDS[card_i][0]] != "#"
        ):
            pos = (pos[0] + CARDS[card_i][0], pos[1] + CARDS[card_i][1])
            if (pos, card_i) in visited:  # we've been here before
                return None
            visited.add((pos, card_i))

        if not (0 <= pos[1] + CARDS[card_i][1] < len(map) and 0 <= pos[0] + CARDS[card_i][0] < len(map[0])):
            # next step is out of bounds, end of algorithm
            break
        card_i = (card_i + 1) % 4

    return visited


to_test = set()


def part1():
    visited = try_route(lines)
    for pos, _ in visited:
        to_test.add(pos)
    return len(visited)


def part2():
    res = 0
    for x, y in to_test:
        new_map = [line.copy() for line in lines]
        new_map[y][x] = "#"
        if try_route(new_map) is None:
            res += 1
    return res


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
