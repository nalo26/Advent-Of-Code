from functools import lru_cache

file = open("input.txt")
lines = file.readlines()


def parse(line):
    card, numbers = line.split(": ")
    card_id = int(card.split(" ")[-1])
    winning, ours = numbers.split(" | ")
    winning = [int(winning[i : i + 2]) for i in range(0, len(winning), 3)]
    ours = [int(ours[i : i + 2]) for i in range(0, len(ours), 3)]
    return card_id, set(winning), set(ours)


def part1():
    _sum = 0
    for line in lines:
        _, winning, ours = parse(line)
        inter = winning & ours
        _sum += 2 ** (len(inter) - 1) if inter else 0
    return _sum


@lru_cache(maxsize=None)
def depth_card(i, line):
    _, winning, ours = parse(line)
    dup = len(winning & ours)
    res = []
    for j in range(dup):
        index = i + j + 1
        res.append(lines[index])
        res.extend(depth_card(index, lines[index]))
    return res


def part2():
    new_lines = lines.copy()
    for i, line in enumerate(lines):
        new_lines.extend(depth_card(i, line))
    return len(new_lines)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
