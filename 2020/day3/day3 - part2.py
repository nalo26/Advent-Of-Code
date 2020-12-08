import math

file = open("input.txt")
lines = [line.strip('\n') for line in file.readlines()]

maxX = len(lines[0])
maxY = len(lines)-1
slopesList = [(1,1),(3,1),(5,1),(7,1),(1,2)]
res = []
for slope in slopesList:
    x = 0
    y = 0
    resSlope = 0
    while (y < maxY):
        y += slope[1]
        x = (x+slope[0])%maxX
        if lines[y][x] == "#":
            resSlope +=1
    res.append(resSlope)
print(math.prod(res))
