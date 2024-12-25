import re
from operator import and_, or_, xor

from lib.input import get_input

OPERATORS = {"AND": and_, "OR": or_, "XOR": xor}


lines = get_input(2024, 24).split("\n\n")

reg = {}
for line in lines[0].splitlines():
    r, v = line.split(": ")
    reg[r] = bool(int(v))

ops = {}
zs = []
for line in lines[1].splitlines():
    a, op, b, r = re.match(r"(.+) (.+) (.+) -> (.+)", line).groups()
    ops[r] = (a, OPERATORS.get(op), b)
    if r.startswith("z"):
        zs.append(r)


def calc(r: str):
    if r in reg:
        return reg[r]
    a, op, b = ops.get(r)
    return op(calc(a), calc(b))


def part1():
    z_res = ""
    for z in sorted(zs, reverse=True):
        z_res += str(int(calc(z)))  # convert bool to bin
    return int(z_res, 2)  # convert bin to int


def part2():
    # Found by hand, see day24p2.txt
    pass
