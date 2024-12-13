import re

import numpy as np
from scipy.optimize import linprog

from lib.input import get_input
from lib.map import Position

COST = [3, 1]


class Machine:
    def __init__(self, A: Position, B: Position, prize: Position):
        self.A = A
        self.B = B
        self.prize = prize


lines = get_input(2024, 13).split("\n\n")
machines: list[Machine] = []
for m in lines:
    A = Position(*tuple(map(int, re.search(r"A: X\+(\d+), Y\+(\d+)", m).groups())))
    B = Position(*tuple(map(int, re.search(r"B: X\+(\d+), Y\+(\d+)", m).groups())))
    prize = Position(*tuple(map(int, re.search(r"Prize: X=(\d+), Y=(\d+)", m).groups())))
    machines.append(Machine(A, B, prize))


def find_minimum_cost(machine: Machine, bounds=None):
    A = np.array([[machine.A.x, machine.B.x], [machine.A.y, machine.B.y]])
    b = np.array([machine.prize.x, machine.prize.y])

    x0_bounds = (0, bounds)
    x1_bounds = (0, bounds)

    res = linprog(COST, A_eq=A, b_eq=b, bounds=[x0_bounds, x1_bounds], method="highs")

    def check_op(a, b):
        return (
            machine.A.x * a + machine.B.x * b == machine.prize.x
            and machine.A.y * a + machine.B.y * b == machine.prize.y
        )

    if not res.success:
        raise ValueError("No solution found")

    a, b = np.round(res.x).astype(int)
    if not check_op(a, b):
        raise ValueError("No solution found")

    # [3 * a + b] constraint pre-calculated by the solver
    return np.round(res.fun).astype(int)


def compute(bounds, mult):
    res = 0
    for machine in machines:
        machine.prize += (mult, mult)
        try:
            res += find_minimum_cost(machine, bounds=bounds)
        except ValueError:
            pass
    return res


def part1():
    return compute(100, 0)


def part2():
    return compute(None, 10000000000000)
