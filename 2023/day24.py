from itertools import combinations

from sympy import Point, Polygon, Ray
from tqdm import tqdm

file = open("input.txt")
lines = file.read().splitlines()

rays: set[Ray] = set()
for line in lines:
    pos, vel = (list(map(int, a.split(", "))) for a in line.split(" @ "))
    a = Point(pos[:-1])
    b = Point([p + v for p, v in zip(pos, vel)][:-1])
    rays.add(Ray(a, b))


def part1():
    limits = [200000000000000, 400000000000000]
    square = Polygon((limits[0], limits[0]), (limits[0], limits[1]), (limits[1], limits[1]), (limits[1], limits[0]))
    count = 0
    for a, b in tqdm(combinations(rays, 2)):
        inter = a.intersection(b)
        if not inter:
            continue
        if square.encloses_point(inter[0]):
            count += 1
    return count


def part2():
    pass


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
