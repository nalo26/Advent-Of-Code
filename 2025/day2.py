from lib.input import get_input

ranges = get_input(2025, 2).split(",")


def run(validate_func):
    _sum = 0
    for rnge in ranges:
        start, stop = map(int, rnge.split("-"))
        rnge = range(start, stop + 1)
        for num in rnge:
            if validate_func(num):
                _sum += num
    return _sum


def part1():
    def is_invalid(num):
        s = str(num)
        return s[0 : len(s) // 2] == s[len(s) // 2 :]

    return run(is_invalid)


def part2():
    def is_invalid(num):
        s = str(num)

        for lgt in range(1, len(s) // 2 + 1):
            splited = [s[i : i + lgt] for i in range(0, len(s), lgt)]
            if all(x == splited[0] for x in splited):
                return True
        return False

    return run(is_invalid)
