import re
from math import lcm

file = open("input.txt")
lines = file.readlines()
rotations = lines[0].strip(" \r\n")
lines = lines[2:]

INDEXES = {"L": 0, "R": 1}


line_re = re.compile(r"(\w+) = \((\w+), (\w+)\)")
graph = {}
for line in lines:
    target, left, right = line_re.match(line).groups()
    graph[target] = (left, right)


def part1():
    current = "AAA"
    steps = 0
    while current != "ZZZ":
        current = graph[current][INDEXES[rotations[steps % len(rotations)]]]
        steps += 1
    return steps


def part2():
    currents = []
    for steps in graph.keys():
        if steps.endswith("A"):
            currents.append(steps)
    # Bruteforce wouldn't work here, as the loop seems to goes on forever
    # However, we can get the lenght of each loop (as there is not intersection)
    # and then get the LCM of all the loops to get the answer
    steps = []
    for start in currents:
        step = 0
        current = start
        while not current.endswith("Z"):
            current = graph[current][INDEXES[rotations[step % len(rotations)]]]
            step += 1
        steps.append(step)
    return lcm(*steps)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
