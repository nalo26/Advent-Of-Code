from lib.consts import DIR_CROSS
from lib.input import get_input
from lib.map import Map

map = Map(get_input(2024, 6))
start_pos = map.find("^")


def try_route(map: Map) -> set[tuple[int, int]]:
    card_i = 0  # starting looking up
    pos = start_pos
    visited = {(pos, card_i)}
    while True:
        while map.is_in_bounds(pos + DIR_CROSS[card_i]) and map[pos + DIR_CROSS[card_i]] != "#":
            pos += DIR_CROSS[card_i]
            if (pos, card_i) in visited:  # we've been here before
                return None
            visited.add((pos, card_i))

        if not map.is_in_bounds(pos + DIR_CROSS[card_i]):
            # next step is out of bounds, end of algorithm
            break
        card_i = (card_i + 1) % 4

    return visited


to_test = set()


def part1():
    visited = try_route(map)
    for pos, _ in visited:
        to_test.add(pos)
    return len(to_test)


def part2():
    res = 0
    for x, y in to_test:
        new_map = map.copy()
        new_map[x, y] = "#"
        if try_route(new_map) is None:
            res += 1
    return res
