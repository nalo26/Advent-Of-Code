file = open("input.txt")
lines = file.readlines()

paths = []
maxX, maxY = 0, 0
for line in lines: # determine size of ocean
    start, end = line.split(" -> ")
    x1, y1 = list(map(int, start.split(",")))
    x2, y2 = list(map(int, end.split(",")))
    paths.append((x1, y1, x2, y2))
    if x1 > maxX: maxX = x1 
    if x2 > maxX: maxX = x2
    if y1 > maxY: maxY = y1
    if y2 > maxY: maxY = y2
    
ocean = []
for y in range(maxY+1): # initializing the ocean
    line = []
    for x in range(maxX+1):
        line.append(0)
    ocean.append(line)

for path in paths: # filling the ocean
    x1, y1, x2, y2 = path
    
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            ocean[y][x1] += 1
        continue
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            ocean[y1][x] += 1
        continue
    
    if x1 < x2:
        y = y1
        if y1 < y2: y_inc = 1
        else: y_inc = -1
    else:
        y = y2
        if y1 < y2: y_inc = -1
        else: y_inc = 1
    for x in range(min(x1, x2), max(x1, x2)+1):
        ocean[y][x] += 1
        y += y_inc

res = 0
for row in ocean:
    for col in row:
        if col >= 2: res += 1
    
print(res)