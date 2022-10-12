import os


def path(path, file):
    return os.sep.join(os.path.abspath(path).split(os.sep)[:-1] + [file])


file = open(path(__file__, "input.txt"))
lines = file.readlines()

lights = [[0 for x in range(1000)] for y in range(1000)]
for line in lines:
    line = line.split()

    index = 2 if line[0] == "turn" else 1

    start = line[index].split(",")
    end = line[index + 2].split(",")
    sx, sy = int(start[0]), int(start[1])
    ex, ey = int(end[0]), int(end[1])

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            if line[0] == "turn":
                if line[1] == "on":
                    lights[y][x] += 1
                else:
                    lights[y][x] = max(0, lights[y][x] - 1)
            else:
                lights[y][x] += 2

print(sum(sum(lights, [])))
