from lib.consts import DIR_CROSS
from lib.input import get_input
from lib.map import Map

map = Map([[int(c) for c in row] for row in get_input(2024, 10).splitlines()])


def find_way(current_pos, heads=None):
    if heads is None:
        heads = []
    if map[current_pos] == 9:
        heads.append(current_pos)
        return heads
    for dir in DIR_CROSS:
        new_pos = current_pos + dir
        if map.is_in_bounds(new_pos) and map[new_pos] == map[current_pos] + 1:
            find_way(new_pos, heads)
    return heads


def part1():
    res = 0
    for trailhead in map.find_all(0):
        res += len(set(find_way(trailhead)))
    return res


def part2():
    res = 0
    for trailhead in map.find_all(0):
        res += len(find_way(trailhead))
    return res
