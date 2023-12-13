file = open("input.txt")
patterns = file.read().split("\n\n")


def check_mirror(pattern: list, length: int, reverse: bool):
    for i in range(1, length):  # mirror iterator
        for check in range(1, length):  # will exit when reaching edge of pattern
            fid, sid = i - check, i + check - 1
            if fid < 0 or sid >= length:
                return i
            first = "".join(line[fid] for line in pattern) if reverse else pattern[fid]
            second = "".join(line[sid] for line in pattern) if reverse else pattern[sid]
            if first != second:
                break
    return 0


def comp(string1, string2):
    return {i for i, (a, b) in enumerate(zip(string1, string2)) if a != b}


def check_mirror2(pattern: list, length: int, reverse: bool):
    for i in range(1, length):  # mirror iterator
        checks = []
        for check in range(1, length):  # will exit when reaching edge of pattern
            fid, sid = i - check, i + check - 1
            if fid < 0 or sid >= length:
                if len(checks) == 1:
                    return i
                continue
            first = "".join(line[fid] for line in pattern) if reverse else pattern[fid]
            second = "".join(line[sid] for line in pattern) if reverse else pattern[sid]
            checks.extend(comp(first, second))
            if len(checks) > 1:
                break
    return 0


def compute(method):
    _sum = 0
    for pattern in patterns:
        pattern = pattern.split("\n")
        row = method(pattern, len(pattern), False)
        col = method(pattern, len(pattern[0]), True)
        _sum += row * 100 + col
    return _sum


def part1():
    return compute(check_mirror)


def part2():
    return compute(check_mirror2)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
