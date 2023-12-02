import sys

file = open("input.txt")
lines = list(file.readlines())

time = int(lines[0])
bus = list(map(int, lines[1].replace("x,", "").split(",")))

i = time
while True:
    for b in bus:
        if i % b == 0:
            print((i - time) * b)
            sys.exit()
    i += 1
