file = open("input.txt")
lines = file.read().splitlines()

X_CARDS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
A_CARDS = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

LETTERS = "XMAS"


def test_xmas(x, y, direction=None):
    for i in range(1, len(LETTERS)):
        if not (0 <= x + i * direction[0] < len(lines[y]) and 0 <= y + i * direction[1] < len(lines)):
            return 0
        if lines[y + i * direction[1]][x + i * direction[0]] != LETTERS[i]:
            return 0

    return 1


def part1():
    res = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X":
                for card in X_CARDS:
                    res += test_xmas(x, y, card)
    return res


def test_mas(x, y):
    l_at_cards = ""

    for card in A_CARDS:
        if not (0 <= x + card[0] < len(lines[y]) and 0 <= y + card[1] < len(lines)):
            return 0
        if lines[y + card[1]][x + card[0]] not in ("M", "S"):
            return 0
        l_at_cards += lines[y + card[1]][x + card[0]]

    if l_at_cards in ("MMSS", "SMMS", "SSMM", "MSSM"):
        return 1

    return 0


def part2():
    res = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "A":
                res += test_mas(x, y)
    return res


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
