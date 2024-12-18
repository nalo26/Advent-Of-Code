from lib.consts import DIR_ANGLE, DIRECTIONS
from lib.input import get_input
from lib.map import Map

map = Map(get_input(2024, 4))

LETTERS = "XMAS"


def test_xmas(pos, direction=None):
    for i in range(1, len(LETTERS)):
        new_pos = (pos.x + i * direction[0], pos.y + i * direction[1])
        if not map.is_in_bounds(new_pos):
            return 0
        if map[new_pos] != LETTERS[i]:
            return 0

    return 1


def part1():
    res = 0
    for pos in map.find_all("X"):
        for card in DIRECTIONS:
            res += test_xmas(pos, card)
    return res


def test_mas(pos):
    l_at_cards = ""

    for card in DIR_ANGLE:
        if not map.is_in_bounds(pos + card):
            return 0
        if map[pos + card] not in ("M", "S"):
            return 0
        l_at_cards += map[pos + card]

    if l_at_cards in ("MMSS", "SMMS", "SSMM", "MSSM"):
        return 1

    return 0


def part2():
    res = 0
    for pos in map.find_all("A"):
        res += test_mas(pos)
    return res
