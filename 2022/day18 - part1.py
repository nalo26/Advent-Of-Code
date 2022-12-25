file = open("input.txt")
lines = file.read().splitlines()

CARDS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

coords = set()
for line in lines:
    coords.add(tuple(map(int, line.split(","))))

count = 0
for coord in coords:
    for card in CARDS:
        if (coord[0] + card[0], coord[1] + card[1], coord[2] + card[2]) in coords:
            continue
        count += 1

print(count)
