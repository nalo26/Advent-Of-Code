file = open("input.txt")

x = 0
y = 0
for line in file.readlines():
    instruction, val = line.split(" ")
    if instruction == "forward": x += int(val)
    if instruction == "down": y += int(val)
    if instruction == "up": y -= int(val)

print(x*y)