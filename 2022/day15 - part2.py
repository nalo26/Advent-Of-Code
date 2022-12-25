import re
from tqdm import tqdm


file = open("input.txt")
lines = file.read().splitlines()

def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def show(_map):
    xs = sorted([a[0] for a in _map])
    ys = sorted([a[1] for a in _map])
    # print(xs[0], ys[0])
    for y in range(ys[0], ys[-1]+1):
        for x in range(xs[0], xs[-1]+1):
            if (x, y) in _map:
                print("#",end="")
            else:
                print(".",end="")
        print()
    # print(xs[-1], ys[-1])


pos = set()
for line in lines:
    match = re.search("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line)
    sx, sy, bx, by = tuple(map(int, match.groups()))
    distance = dist((sx, sy), (bx, by))
    for y in range(-distance, distance + 1):
        d = (distance-abs(y))
        pos |= {(x, sy+y) for x in range(sx-d, sx+d+1)}
show(pos)

m = 20
for y in range(m+1):
    for x in range(m+1):
        if (x, y) not in pos:
            print(x, y)
            # print(x * m + y)
            exit(0)
