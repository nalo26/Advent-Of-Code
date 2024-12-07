from operator import add, mul

from lib.input import get_input

lines = get_input(2024, 7).splitlines()
calibrations = {int(line.split(": ")[0]): tuple(map(int, line.split(": ")[1].split())) for line in lines}

ops1 = [add, mul]
ops2 = [add, mul, lambda x, y: int(str(x) + str(y))]  # concat


def find_path(result, calibration, ops):
    new_previous_res = {calibration[0]}
    for i_val, val in enumerate(calibration[1:], 1):
        previous_res = set()
        for prev in new_previous_res:
            for op in ops:
                res = op(prev, val)
                if i_val == len(calibration) - 1 and result == res:
                    return True
                previous_res.add(res)
        new_previous_res = previous_res
    return False


def test_all(ops):
    res = 0
    for test_value, cal in calibrations.items():
        if find_path(test_value, cal, ops):
            res += test_value
    return res


def part1():
    return test_all(ops1)


def part2():
    return test_all(ops2)
