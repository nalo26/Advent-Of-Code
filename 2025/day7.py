from functools import cache

from lib.input import get_input
from lib.map import Map, Position

lines = get_input(2025, 7)
tachyon = Map(lines)


@cache
def splitter(pos: Position):
    while True:
        pos += (0, 1)  # downward
        if not tachyon.is_in_bounds(pos):
            return set()  # reached the end of the tachyon, no new splitter
        if tachyon[pos] == "^":  # ray cast split, new splitter encountered
            return splitter(pos - (1, 0)) | splitter(pos + (1, 0)) | {pos}


@cache
def timeline(pos: Position):
    while True:
        pos += (0, 1)
        if not tachyon.is_in_bounds(pos):
            return 1  # reached the end of a timeline
        if tachyon[pos] == "^":  # timeline split
            return timeline(pos - (1, 0)) + timeline(pos + (1, 0))


def part1():
    start = tachyon.find("S")
    return len(splitter(start))


def part2():
    start = tachyon.find("S")
    return timeline(start)
