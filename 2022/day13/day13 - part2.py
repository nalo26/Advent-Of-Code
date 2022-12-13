import functools

file = open("input.txt")
packets = list(map(eval, file.read().replace("\n\n", "\n").split("\n")))
packets.extend([[[2]], [[6]]])


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


packets = sorted(packets, key=functools.cmp_to_key(compute_order))
for p in packets:
    print(p)

print((packets.index([[2]])+1) * (packets.index([[6]])+1))