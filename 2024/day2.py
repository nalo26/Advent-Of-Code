from lib.input import get_input

lines = get_input(2024, 2).splitlines()


def check_valid(report):
    # check if continuoulsy increasing or decreasing
    _sorted = sorted(report)
    if not (_sorted == report or _sorted[::-1] == report):
        return False

    # check if differences between levels are in [1, 3]
    difs = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    if any(x == 0 or x > 3 for x in difs):
        return False
    return True


def part1():
    res = 0
    for report in lines:
        report = list(map(int, report.split()))
        if check_valid(report):
            res += 1
    return res


def part2():
    res = 0
    for report in lines:
        report = list(map(int, report.split()))
        if check_valid(report):
            res += 1
            continue

        # if not valid, try removing one level at a time
        for i in range(len(report)):
            if check_valid(report[:i] + report[i + 1 :]):
                res += 1
                break

    return res
