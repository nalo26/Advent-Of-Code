file = open("input.txt")

x, y, aim = 0, 0, 0
for line in file.readlines():
    instruction, val = line.split(" ")
    if instruction == "forward":
        x += int(val)
        y += aim*int(val)
    if instruction == "down": aim += int(val)
    if instruction == "up": aim -= int(val)

print(x*y)