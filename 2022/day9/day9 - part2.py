file = open("input.txt")
lines = file.read().splitlines()

def calculate_tail(t, h, m):
    xd = abs(h[0] - t[0])
    yd = abs(h[1] - t[1])
    if xd < 2 and yd < 2:
        return (0, 0)

    if xd == 2 and t[1] == h[1]:
        return (m[0], 0)

    if yd == 2 and t[0] == h[0]:
        return (0, m[1])

    if 0 not in m: return m
    return ((h[0] + m[0] * -1) - t[0], (h[1] + m[1] * -1) - t[1])


head = [0, 0]
tails = [head.copy() for _ in range(9)]
tails_positions = set()
tails_positions.add(tuple(tails[-1]))
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
        last_motion = move
        for i in range(len(tails)):
            tmp_head = head if i == 0 else tails[i-1]
            motion = calculate_tail(tails[i], tmp_head, last_motion)
            last_motion = motion
            tails[i] = [tails[i][0] + motion[0], tails[i][1] + motion[1]]
        tails_positions.add(tuple(tails[-1]))

print(len(tails_positions))