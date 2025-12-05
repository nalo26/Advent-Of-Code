from lib.input import get_input

database = get_input(2025, 5).split("\n\n")
fresh_ingredients_ranges = [tuple(map(int, line.split("-"))) for line in database[0].splitlines()]
available_ingredients = list(map(int, database[1].splitlines()))


def part1():
    fresh = 0
    for ingredient in available_ingredients:
        if any(s <= ingredient <= e for (s, e) in fresh_ingredients_ranges):
            fresh += 1
    return fresh


def part2():
    res = 0
    ranges = sorted(fresh_ingredients_ranges)
    current = -1
    for start, end in ranges:
        if current >= start:
            start = current + 1
        if start <= end:
            res += end - start + 1
        current = max(current, end)
    return res
