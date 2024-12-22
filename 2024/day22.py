from collections import defaultdict

from lib.input import get_input

lines = list(map(int, get_input(2024, 22).splitlines()))


def mix(s: int, n: int) -> int:
    return s ^ n


def prune(n: int) -> int:
    return n % 16777216


def random_nextint(secret: int):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


def part1():
    res = 0
    for secret in lines:
        for _ in range(2000):
            secret = random_nextint(secret)
        res += secret
    return res


def part2():
    all_seq = defaultdict(list)

    for secret in lines:
        last_digit = secret % 10
        dif = []
        seen = set()

        for i in range(2000):
            secret = random_nextint(secret)
            new_digit = secret % 10
            dif.append(new_digit - last_digit)
            last_digit = new_digit

            if i >= 4:  # keeping only last 4 diff digits
                dif.pop(0)
            if i >= 3 and (diftup := tuple(dif)) not in seen:
                all_seq[diftup].append(new_digit)
                seen.add(diftup)

    max_id = max(all_seq, key=lambda k: sum(all_seq.get(k)))
    return sum(all_seq.get(max_id))
