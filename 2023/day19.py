import re
from collections import defaultdict

file = open(r"C:\Users\Epulapp\OneDrive\Dev\Advent-Of-Code\2023\input.txt")
instructions_list, parts = file.read().split("\n\n")
instructions_list = instructions_list.splitlines()
parts = parts.splitlines()
r = re.compile(r"(\w+){(.+)}")
instructions = defaultdict(list)
for inst in instructions_list:
    name, rules = r.match(inst).groups()
    rules = rules.split(",")
    for rule in rules:
        op, res = rule.split(":") if ":" in rule else ("True", rule)
        instructions[name].append((op, res))


def compute(part):
    values = {"x": 0, "m": 0, "a": 0, "s": 0}
    for var in part.strip(r"{}").split(","):
        k, v = var.split("=")
        values[k] = int(v)
    x, m, a, s = values.values()
    current = "in"
    while True:
        if current == "A":
            return sum([x, m, a, s])
        if current == "R":
            break
        for op, res in instructions[current]:
            if eval(op):
                current = res
                break
    return 0


def part1():
    _sum = 0
    for part in parts:
        _sum += compute(part)
    return _sum


def part2():
    pass


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
