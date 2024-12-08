from lib.input import get_input
from lib.map import Map

raw_input = get_input(2024, 8)
map = Map(raw_input)

antennas = set(raw_input.replace("\n", "").replace(".", ""))


def iterate_antennas(map):
    for char in antennas:
        all_pos = map.find_all(char)
        if len(all_pos) < 2:
            continue
        for pos1 in all_pos:
            for pos2 in all_pos:
                if pos1 == pos2:
                    continue
                yield pos1, pos2


def part1():
    antinodes = set()
    for p1, p2 in iterate_antennas(map):
        anode1 = p1 + (p1 - p2)
        if map.is_in_bounds(anode1):
            antinodes.add(anode1)
        anode2 = p2 + (p2 - p1)
        if map.is_in_bounds(anode2):
            antinodes.add(anode2)

    return len(antinodes)


def part2():
    antinodes = set()
    for p1, p2 in iterate_antennas(map):
        anode1 = p1
        while map.is_in_bounds(anode1):
            antinodes.add(anode1)
            anode1 += p1 - p2
        anode2 = p2
        while map.is_in_bounds(anode2):
            antinodes.add(anode2)
            anode2 += p2 - p1

    return len(antinodes)
