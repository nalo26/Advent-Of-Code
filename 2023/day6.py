file = open("input.txt")
lines = file.readlines()


def race_wins(time, dist):
    wins = 0
    for hold_time in range(time):
        distance = (time - hold_time) * hold_time
        if distance > dist:
            wins += 1
    return wins


def part1():
    times = list(map(int, lines[0].split(":")[1].strip().split()))
    distances = list(map(int, lines[1].split(":")[1].strip().split()))
    races = [(times[i], distances[i]) for i in range(len(times))]
    prod = 1
    for time, dist in races:
        prod *= race_wins(time, dist)
    return prod


def part2():
    time = int("".join(lines[0].split(":")[1].strip().split()))
    distance = int("".join(lines[1].split(":")[1].strip().split()))
    return race_wins(time, distance)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
