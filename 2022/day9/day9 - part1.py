file = open("input.txt")
lines = file.read().splitlines()


def calculate_tail(t, h, m):
    xd = abs(h[0] - t[0])
    yd = abs(h[1] - t[1])
    if xd < 2 and yd < 2:
        return t

    if xd == 2 and t[1] == h[1]:
        return [t[0] + m[0], t[1]]

    if yd == 2 and t[0] == h[0]:
        return [t[0], t[1] + m[1]]

    return [h[0] + m[0]*-1, h[1] + m[1]*-1]


head = [0, 0]
tail = head.copy()
tail_positions = set()
tail_positions.add(tuple(tail))
move = (0, 0)
for line in lines:
    side, step = line.split()
    step = int(step)

    match side:
        case 'R': move = (1, 0)
        case 'U': move = (0, 1)
        case 'L': move = (-1, 0)
        case 'D': move = (0, -1)

    for _ in range(step):
        head[0] += move[0]
        head[1] += move[1]
        tail = calculate_tail(tail, head, move)
        tail_positions.add(tuple(tail))

print(len(tail_positions))