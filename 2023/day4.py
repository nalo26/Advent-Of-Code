file = open("input.txt")
lines = file.readlines()


def parse(line):
    card, numbers = line.split(": ")
    card_id = int(card.split(" ")[-1])
    winning, ours = numbers.split(" | ")
    return card_id, set(map(int, winning.split())), set(map(int, ours.split()))


def part1():
    _sum = 0
    for line in lines:
        _, winning, ours = parse(line)
        inter = winning & ours
        _sum += 2 ** (len(inter) - 1) if inter else 0
    return _sum


def part2():
    cards = {}
    for line in lines:
        card_id, winning, ours = parse(line)
        wins = winning & ours
        cards[card_id] = [1, len(wins)]

    for card_id, (count, wins) in cards.items():
        for i in range(wins):
            cards[card_id + i + 1][0] += count

    return sum(map(lambda x: x[0], cards.values()))


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
