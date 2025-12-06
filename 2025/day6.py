from functools import reduce
from operator import add, mul

from lib.input import get_input

lines = get_input(2025, 6).splitlines()


OPERATORS = {"+": add, "*": mul}


def part1():
    result = 0
    # Using zip to group columns together
    for col in zip(*(line.split() for line in lines)):
        values = map(int, col[:-1])  # Convert all lines (except last (operator)) to int
        op = OPERATORS[col[-1]]  # Dynamic operator selection
        result += reduce(lambda x, y: op(x, y), values)  # Apply operation cumulatively
    return result

    # One liner version:
    # return sum(
    #     reduce(lambda x, y: OPERATORS[col[-1]](x, y), map(int, col[:-1]))
    #     for col in zip(*(line.split() for line in lines))
    # )


def part2():
    result = 0
    # Identify operator positions in the last line
    i_ops = [i for i, op in enumerate(lines[-1]) if op != " "]
    i_ops.append(len(lines[-1]) + 1)  # Last column handling
    for j in range(len(i_ops) - 1):
        # Extract column width based on operator positions
        cur_i_op = i_ops[j]
        next_i_op = i_ops[j + 1] - 1

        # Get operator for current column
        op = OPERATORS[lines[-1][cur_i_op]]

        # Get column values from each line based on column width computed above
        values = [line[cur_i_op:next_i_op] for line in lines[:-1]]
        # Reverse column (top to bottom) and convert to int
        col_values = [int("".join(v)) for v in zip(*values)]

        result += reduce(lambda x, y: op(x, y), col_values)
    return result
