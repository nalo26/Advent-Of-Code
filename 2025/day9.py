from itertools import combinations

from shapely import Polygon, box

from lib.input import get_input
from lib.map import Position

lines = get_input(2025, 9).splitlines()
red_tiles = [Position(*map(int, line.split(","))) for line in lines]


def part1():
    max_area = 0
    for pos1, pos2 in combinations(red_tiles, 2):
        area = (abs(pos1.x - pos2.x) + 1) * (abs(pos1.y - pos2.y) + 1)
        if area > max_area:
            max_area = area
    return max_area

    # One-liner version:
    # return max((abs(pos1.x - pos2.x) + 1) * (abs(pos1.y - pos2.y) + 1) for pos1, pos2 in combinations(red_tiles, 2))


def part2():
    # Create non-convex polygon of red tiles
    poly = Polygon([(tile.x, tile.y) for tile in red_tiles])

    max_area = 0
    for pos1, pos2 in combinations(red_tiles, 2):
        rect = box(min(pos1.x, pos2.x), min(pos1.y, pos2.y), max(pos1.x, pos2.x), max(pos1.y, pos2.y))
        if not poly.contains(rect):  # Check if tested rectangle is inside the shape formed by red tiles
            continue
        area = (abs(pos1.x - pos2.x) + 1) * (abs(pos1.y - pos2.y) + 1)
        if area > max_area:  # manual area calculation because rect.area is not correct for integer coordinates
            max_area = area
    return max_area

    # One-liner version:
    # return max(
    #     (abs(pos1.x - pos2.x) + 1) * (abs(pos1.y - pos2.y) + 1)
    #     for pos1, pos2 in combinations(red_tiles, 2)
    #     if poly.contains(box(min(pos1.x, pos2.x), min(pos1.y, pos2.y), max(pos1.x, pos2.x), max(pos1.y, pos2.y)))
    # )
