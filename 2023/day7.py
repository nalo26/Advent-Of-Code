from collections import Counter, defaultdict

file = open("input.txt")
lines = file.readlines()


def calculate_hand_strenght(hand, joker=False):
    count = Counter(hand)
    mc = count.most_common(5)
    if joker and "J" in hand:
        rep = mc[0][0] if mc[0][0] != "J" else (mc[1][0] if len(mc) > 1 else "A")
        hand = hand.replace("J", rep)
        count = Counter(hand)
        mc = count.most_common(5)
    match mc[0][1]:
        case 5:
            return 7  # Five of a kind
        case 4:
            return 6  # Four of a kind
        case 3:
            # Full house //  Three of a kind
            return 5 if mc[1][1] == 2 else 4
        case 2:
            # Two pairs     //      One pair
            return 3 if mc[1][1] == 2 else 2
        case 1:
            return 1  # High card
    return 0  # Should never happen


def compare_hands(hand1, hand2, cards):
    """
    return 1 if hand1 is stronger than hand2
    return 0 if hand1 is equal to hand2
    return -1 if hand1 is weaker than hand2
    """
    for a, b in zip(hand1, hand2):
        if a == b:
            continue
        return 1 if cards.index(a) > cards.index(b) else -1
    return 0


def calculate(cards, joker=False):
    strenghts = defaultdict(list)
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        strenghts[calculate_hand_strenght(hand, joker)].append((hand, bid))

    ordened_hands = []
    for i in range(7, 0, -1):
        if i not in strenghts:
            continue
        hands = strenghts[i]
        local_ordened_hands = []
        for hand, bid in hands:
            for j in range(len(local_ordened_hands)):
                if compare_hands(hand, local_ordened_hands[j][0], cards) == 1:
                    local_ordened_hands.insert(j, (hand, bid))
                    break
            else:
                local_ordened_hands.append((hand, bid))
        ordened_hands.extend(local_ordened_hands)

    _sum = 0
    for i, (_, score) in enumerate(ordened_hands[::-1], 1):
        _sum += i * score
    return _sum


def part1():
    cards = "23456789TJQKA"
    return calculate(cards)


def part2():
    cards = "J23456789TQKA"
    return calculate(cards, True)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
