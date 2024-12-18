from lib.input import get_input

lines = list(map(int, get_input(2024, 11).splitlines()[0].split()))


def blink(stones: dict[int, int]) -> dict[int, int]:
    res = {}
    for n, qte in stones.items():
        if n == 0:
            res[1] = res.get(1, 0) + qte
        elif len(s := str(n)) % 2 == 0:
            v1 = int(s[: len(s) // 2])
            v2 = int(s[len(s) // 2 :])
            res[v1] = res.get(v1, 0) + qte
            res[v2] = res.get(v2, 0) + qte
        else:
            res[n * 2024] = res.get(n * 2024, 0) + qte
    return res


def compute(blink_amount: int) -> int:
    stones = {n: 1 for n in lines}
    for _ in range(blink_amount):
        stones = blink(stones)
    return sum(stones.values())


def part1():
    return compute(25)


def part2():
    return compute(75)
