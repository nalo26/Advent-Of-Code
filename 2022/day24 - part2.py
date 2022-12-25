file = open("input.txt")
lines = file.read().splitlines()


CARDS = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
board = [list(line) for line in lines]

start = (0, 0)
for y, c in enumerate(board[0]):
    if c == ".":
        start = (0, y)
        break

end = (0, 0)
for y, c in enumerate(board[-1]):
    if c == ".":
        end = (len(board) - 1, y)
        break

blizzards = []
walls = set()
for y, row in enumerate(board):
    for x, cell in enumerate(row):
        if cell in "><v^":
            blizzards.append((cell, (y, x)))
        elif cell == "#":
            walls.add((y, x))
walls.add((-1, start[1]))
walls.add((end[0] + 1, end[1]))


def get_blizzards(board, blizz):
    new_blizzards = []
    for b in blizz:
        pos = b[1]
        if b[0] == ">":
            pos = (pos[0], pos[1] + 1)
        elif b[0] == "<":
            pos = (pos[0], pos[1] - 1)
        elif b[0] == "^":
            pos = (pos[0] - 1, pos[1])
        elif b[0] == "v":
            pos = (pos[0] + 1, pos[1])

        if pos in walls:
            if b[0] == ">":
                pos = (pos[0], 1)
            elif b[0] == "<":
                pos = (pos[0], len(board[0]) - 2)
            elif b[0] == "^":
                pos = (len(board) - 2, pos[1])
            elif b[0] == "v":
                pos = (1, pos[1])

        new_blizzards.append((b[0], pos))
    return new_blizzards


def compute(board, start, end, blizzards, walls):
    states = {start}
    time = 0
    while end not in states:
        time += 1

        new_states = set()
        blizzards = get_blizzards(board, blizzards)
        blizzard_set = set(b for _, b in blizzards)
        for curr in states:
            pot = {(curr[0] + dy, curr[1] + dx) for (dy, dx) in CARDS}
            new_states |= pot - blizzard_set - walls

        states = new_states

    return (time, blizzards)


a, blizzards = compute(board, start, end, blizzards, walls)
b, blizzards = compute(board, end, start, blizzards, walls)
c, blizzards = compute(board, start, end, blizzards, walls)

print(a + b + c)
