import re

from lib.input import get_input

lines = get_input(2024, 3)
regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def part1():
    res = 0
    for find in re.findall(regex, lines):
        res += int(find[0]) * int(find[1])
    return res


def part2():
    res = 0
    for donts in lines.split("do()"):
        # ignore disable instruction parts, keeping only the do() parts
        instr = donts.split("don't()")[0]
        for find in re.findall(regex, instr):
            res += int(find[0]) * int(find[1])
    return res
