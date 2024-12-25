from lib.input import get_input

lines = get_input(2024, 25).split("\n\n")
locks = []
keys = []
for line in lines:
    lock = list(zip(*line.splitlines()[::-1]))  # rotate 90
    numbers = [line.count("#") - 1 for line in lock]
    if lock[0][-1] == "#":  # lock
        locks.append(numbers)
    else:  # "." key
        keys.append(numbers)


def part1():
    found = 0
    for lock in locks:
        for key in keys:
            if any(a + b > 5 for a, b in zip(lock, key)):
                continue
            found += 1
    return found


def part2():
    return None  # no part 2 on 25th
