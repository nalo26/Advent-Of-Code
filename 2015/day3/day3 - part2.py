file = open("input.txt")
moves = file.readline()

sx, sy = 0, 0
rx, ry = 0, 0
positions = {(0,0)}
for i, move in enumerate(moves):
    if i%2 == 0:
        if move == "^": sy -= 1
        if move == "v": sy += 1
        if move == ">": sx += 1
        if move == "<": sx -= 1
        positions.add((sx,sy))
    else:
        if move == "^": ry -= 1
        if move == "v": ry += 1
        if move == ">": rx += 1
        if move == "<": rx -= 1
        positions.add((rx,ry))

print(len(positions))