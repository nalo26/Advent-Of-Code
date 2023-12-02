import re

from tqdm import tqdm

file = open("input.txt")
lines = file.read().splitlines()


def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


sensors = {}
distances = set()
xs = set()
for line in lines:
    match = re.search(
        "Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line
    )
    sx, sy, bx, by = tuple(map(int, match.groups()))
    sensors[(sx, sy)] = (bx, by)
    distances.add(dist((sx, sy), (bx, by)))
    xs |= {sx, bx}

row = 2000000
count = 0
for x in tqdm(range(min(xs) - max(distances), max(xs) + max(distances))):
    if (x, row) in set(sensors.values()):
        continue
    for sensor, beacon in sensors.items():
        if dist(sensor, (x, row)) <= dist(sensor, beacon):
            count += 1
            break

print(count)
