file = open("input.txt")
pairs = file.read().split("\n\n")


def compute_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, int) and isinstance(right, list):
        return compute_order([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compute_order(left, [right])

    # both list
    for l, r in zip(left, right):
        r = compute_order(l, r)
        if r:
            return r
    return len(left) - len(right)


count = 0
for i, pair in enumerate(pairs, 1):
    left, right = tuple(map(eval, pair.split("\n")))
    if compute_order(left, right) < 0:
        count += i

print(count)
