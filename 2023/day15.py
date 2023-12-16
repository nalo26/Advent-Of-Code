import re
from collections import OrderedDict
from contextlib import suppress

file = open("input.txt")
instructions = file.readlines()[0].strip().split(",")


def hash(string):
    value = 0
    for char in string:
        value = ((value + ord(char)) * 17) % 256
    return value


def part1():
    _sum = 0
    for inst in instructions:
        _sum += hash(inst)
    return _sum


def part2():
    boxes = [OrderedDict() for _ in range(256)]
    get_parts = re.compile(r"(\w+)([-=])(\d*)")
    for inst in instructions:  # compute instructions
        parts = get_parts.match(inst)
        name, op = parts.group(1), parts.group(2)
        name_hash = hash(name)
        if op == "=":
            boxes[name_hash][name] = int(parts.group(3))
        else:
            with suppress(KeyError):
                del boxes[name_hash][name]

    power = 0
    for i, box in enumerate(boxes, 1):  # calculate total power
        for j, focal in enumerate(box.values(), 1):
            power += i * j * focal
    return power


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
