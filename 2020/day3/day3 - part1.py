file = open("input.txt")
lines = [line.strip('\n') for line in file.readlines()]

x = 0
y = 0
maxX = len(lines[0])
res = 0
while (y < len(lines)-1):
    y += 1
    x = (x+3)%maxX
    if lines[y][x] == "#":
        res +=1
print(res)