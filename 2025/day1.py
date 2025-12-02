from collections import deque

from lib.input import get_input

lines = get_input(2025, 1).splitlines()


def part1():
    dial = 50
    count = 0
    for inst in lines:
        rot, num = inst[0], int(inst[1:])
        if rot == "L":
            dial = (dial - num) % 100
        else:
            dial = (dial + num) % 100
        if dial == 0:
            count += 1
    return count


def part2():
    dial = deque(range(100))
    dial.rotate(-50)
    count = 0
    for inst in lines:
        rot, num = inst[0], int(inst[1:])
        rot = 1 if rot == "L" else -1
        for _ in range(num):  # oh no
            dial.rotate(rot)
            if dial[0] == 0:
                count += 1
    return count
