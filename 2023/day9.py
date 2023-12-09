file = open("input.txt")
lines = file.readlines()
sequences = [list(map(int, line.split())) for line in lines]


def find_diffs(sequence):
    diffs = []
    for i in range(len(sequence) - 1):
        diffs.append(sequence[i + 1] - sequence[i])
    return diffs


def extrapolate_forward(sequence):
    if len(set(sequence)) == 1:
        return sequence[-1]
    return sequence[-1] + extrapolate_forward(find_diffs(sequence))


def extrapolate_backward(sequence):
    if len(set(sequence)) == 1:
        return sequence[0]
    return sequence[0] - extrapolate_backward(find_diffs(sequence))


def extrapolate(f):
    _sum = 0
    for sequence in sequences:
        steps_diff = f(sequence)
        _sum += steps_diff
    return _sum


def part1():
    return extrapolate(extrapolate_forward)


def part2():
    return extrapolate(extrapolate_backward)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
