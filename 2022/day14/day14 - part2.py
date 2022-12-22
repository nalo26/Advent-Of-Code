file = open("input.txt")
lines = file.read().splitlines()

X_CARDS = [0, -1, 1]


def can_fall(start, walls, lowest):
    pos = list(start)
    while True:
        walls |= {(pos[0] + c, lowest + 2) for c in X_CARDS}
        for cards in X_CARDS:
            if (pos[0] + cards, pos[1] + 1) not in walls:
                pos = [pos[0] + cards, pos[1] + 1]
                break
        else:
            walls.add(tuple(pos))
            return pos != list(start)


walls = set()
ys = set()
for line in lines:
    points = line.split(" -> ")
    for i, point in enumerate(points[:-1]):
        x1, y1 = tuple(map(int, point.split(",")))
        x2, y2 = tuple(map(int, points[i + 1].split(",")))
        ys |= {y1, y2}
        if x1 == x2:
            walls |= {(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)}
        else:
            walls |= {(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)}

start = (500, 0)
count = 1
while can_fall(start, walls, max(ys)):
    count += 1

print(count)
