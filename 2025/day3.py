from lib.input import get_input

lines = get_input(2025, 3).splitlines()


def run(x: int):
    _sum = 0
    for bank in lines:
        bank = list(map(int, bank))
        istart, istop = 0, len(bank) - (x - 1)  # init window : 0 to len - (x - 1)
        res = 0
        for p in range(x):
            window = bank[istart:istop]
            high = max(window)  # find max on current window
            istop += 1  # move window one step right
            istart += window.index(high) + 1  # cut left side to the max value
            res += high * 10 ** ((x - 1) - p)  # compute result with power of 10 for position
        _sum += res
    return _sum


def part1():
    return run(2)


def part2():
    return run(12)
