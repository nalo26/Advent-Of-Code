from lib.consts import DIR_CROSS
from lib.input import get_input
from lib.map import Map

# map = Map([list(line) for line in get_input(2024, 12).splitlines()])
map = Map([list(line) for line in get_input(True).splitlines()])


def evaluate_region(pos, val, visited=None):
    if visited is None:
        visited = set()
    if not map.is_in_bounds(pos) or map[pos] != val:
        return 0, 1, visited
    if pos in visited:
        return 0, 0, visited

    visited.add(pos)
    area = 1
    perimeter = 0
    for dir in DIR_CROSS:
        a, p, _ = evaluate_region(pos + dir, val, visited)
        area += a
        perimeter += p
    return area, perimeter, visited


def part1():
    res = 0
    visited = set()
    for pos, val in map:
        if pos in visited:
            continue
        a, p, v = evaluate_region(pos, val)
        res += a * p
        visited |= v
    return res


def part2():
    pass
