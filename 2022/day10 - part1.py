file = open("input.txt")

lines = file.read().splitlines()

signals = [40 * i + 20 for i in range(6)]


def incrementCycle(cycle, x):
    cycle += 1
    if cycle in signals:
        return cycle, x
    return cycle, None


x = 1
cycle = 0
flags = []
for i, line in enumerate(lines, 1):
    flag1, flag2 = None, None
    cycle, flag1 = incrementCycle(cycle, x)
    if line.startswith("addx"):
        x += int(line.split()[1])
        cycle, flag2 = incrementCycle(cycle, x)
    flag = flag1 or flag2
    if flag is not None:
        flags.append(flag)

print(sum(signals[i] * flags[i] for i in range(len(signals))))
