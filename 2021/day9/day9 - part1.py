file = open("input.txt")
lines = file.readlines()

heightmap = []
for line in lines:
    heightmap.append(list(map(int, line.replace('\n', ''))))

risk = 0
for y, line in enumerate(heightmap):
    for x, n in enumerate(line):
        if y > 0 and n >= heightmap[y-1][x]: continue # up
        try:
            if n >= heightmap[y+1][x]: continue # down
        except IndexError: pass
        if x > 0 and n >= heightmap[y][x-1]: continue # left
        try:
            if n >= heightmap[y][x+1]: continue # right
        except IndexError: pass
        risk += n + 1

print(risk)