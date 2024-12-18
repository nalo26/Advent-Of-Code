from lib.input import get_input

lines = get_input(2024, 1).splitlines()

l1, l2 = [], []
for line in lines:
    _line = line.split()
    l1.append(int(_line[0]))
    l2.append(int(_line[1]))


def part1():
    res = 0
    for a, b in zip(sorted(l1), sorted(l2)):
        res += abs(a - b)
    return res


def part2():
    res = 0
    for _id in l1:
        res += _id * l2.count(_id)
    return res
