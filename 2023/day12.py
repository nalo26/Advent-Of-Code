# Credits for the recursive logic:
# https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/

from functools import cache

file = open("input.txt")
lines = file.readlines()


def can_fit(fields, groups):
    group = groups[0]
    field_group = fields[:group].replace("?", "#")
    if "." in field_group or len(field_group) != group:
        return 0

    if len(fields) == group:
        # We're on the last group of field
        if len(groups) == 1:
            return 1
        return 0

    if fields[group] in "?.":
        # if the next group is not the same as this one
        return calc(fields[group + 1 :], groups[1:])

    return 0


@cache
def calc(fields, groups):
    if not groups:
        if "#" in fields:
            return 0  # Damaged field left that can't fit in groups
        return 1  # All fields filled

    if not fields:
        return 0  # Can't fit all groups in field

    spring = fields[0]
    rest = fields[1:]

    match spring:
        case "#":
            return can_fit(fields, groups)
        case ".":
            return calc(rest, groups)
        case "?":
            return calc("." + rest, groups) + calc("#" + rest, groups)


def part1():
    count = 0
    for line in lines:
        fields, groups = line.split(" ")
        groups = tuple(map(int, groups.split(",")))
        count += calc(fields, groups)
    return count


def part2():
    count = 0
    for line in lines:
        fields, groups = line.split(" ")
        fields = "?".join([fields] * 5)
        groups = tuple(map(int, groups.split(","))) * 5
        count += calc(fields, groups)
    return count


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
