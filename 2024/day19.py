from functools import cache

from lib.input import get_input

lines = get_input(2024, 19).split("\n\n")
patterns = lines[0].split(", ")
towels = lines[1].splitlines()


@cache
def trytowel(tofind: str, current: str):
    if tofind == current:
        return 1

    res = 0
    for pattern in patterns:
        if tofind.startswith(current + pattern):
            res += trytowel(tofind, current + pattern)
    return res


def part1():
    res = 0
    for towel in towels:
        res += 1 if trytowel(towel, "") > 0 else 0
    return res


def part2():
    res = 0
    for towel in towels:
        res += trytowel(towel, "")
    return res
