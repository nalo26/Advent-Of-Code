file = open("input.txt")
moves = file.readline()

x, y = 0, 0
positions = {(x, y)}
for move in moves:
    if move == "^":
        y -= 1
    if move == "v":
        y += 1
    if move == ">":
        x += 1
    if move == "<":
        x -= 1
    positions.add((x, y))

print(len(positions))
