from lib.input import get_input

lines = get_input(2025, 12).split("\n\n")
presents = []
for present in lines[:-1]:
    presents.append(present.count("#"))


def part1():
    res = 0
    for puzzle in lines[-1].splitlines():
        dimension, gift_count = puzzle.split(": ")
        w, h = map(int, dimension.split("x"))
        gift_count = list(map(int, gift_count.split()))

        # only checking if this could theoretically fit
        # no rotations or anything, good fool
        if sum(presents[i] * n for i, n in enumerate(gift_count)) <= w * h:
            res += 1
    return res


def part2():  # No part2 on last day
    return None
