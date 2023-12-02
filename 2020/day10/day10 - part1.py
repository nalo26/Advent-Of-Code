file = open("input.txt")
lines = [int(line.replace("\n", "")) for line in file.readlines()]
lines.sort()

values = [1] * 3

last = lines[0]
for v in lines[1:]:
    values[(v - last) - 1] += 1
    last = v

print(values[0] * values[2])
