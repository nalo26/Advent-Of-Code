file = open("input.txt")
lines = file.readlines()
plateform = tuple([line.strip() for line in lines])
size = len(plateform)

# North, West, South, East
RELATIVES = [(-1, 0, False), (0, -1, False), (1, 0, True), (0, 1, True)]
NORTH = RELATIVES[0]


def tilt(old_plateform, direction):
    reversed = direction[2]
    plateform = (
        [list(line[::-1]) for line in old_plateform[::-1]] if reversed else [list(line) for line in old_plateform]
    )
    for y, line in enumerate(plateform):
        for x, rock in enumerate(line):
            if rock != "O":
                continue
            new_y, new_x = y, x
            while True:
                new_y += direction[0] if not reversed else -direction[0]
                new_x += direction[1] if not reversed else -direction[1]
                if new_y < 0 or new_y >= size or new_x < 0 or new_x >= size or plateform[new_y][new_x] != ".":
                    new_y -= direction[0] if not reversed else -direction[0]
                    new_x -= direction[1] if not reversed else -direction[1]
                    plateform[y][x] = "."
                    plateform[new_y][new_x] = "O"
                    break
    ret = ["".join(line[::-1]) for line in plateform[::-1]] if reversed else ["".join(line) for line in plateform]
    return tuple(ret)


def calculate_load(plateform):
    load = 0
    for y, line in enumerate(plateform):
        for rock in line:
            if rock == "O":
                load += size - y
    return load


def part1():
    tilted_plateform = tilt(plateform, NORTH)
    return calculate_load(tilted_plateform)


def part2():
    seens = {}
    scores = []
    tilted_plateform = plateform
    for i in range(300):
        for direction in RELATIVES:
            tilted_plateform = tilt(tilted_plateform, direction)
        if tilted_plateform in seens:
            seen_at = seens[tilted_plateform]
            # get the score at the seen time + the number of cycles until the end
            return scores[seen_at - 1 + (1000000000 - seen_at) % (i - seen_at)]
        seens[tilted_plateform] = i
        scores.append(calculate_load(tilted_plateform))


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
