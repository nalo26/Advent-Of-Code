file = open("input.txt")
LINES = file.readlines()

# oxygen generator rating
lines = LINES.copy()
candidates = lines.copy()

for i in range(12):  # size of a line
    l = []
    for line in lines:
        l.append(line[i])

    if l.count("0") > l.count("1"):
        selected = "0"
    else:
        selected = "1"

    for line in lines:
        if line[i] != selected:
            candidates.remove(line)

    lines = candidates.copy()
    if len(candidates) == 1:
        break

ogr = int(candidates[0], 2)


# CO2 scrubber rating
lines = LINES.copy()
candidates = lines.copy()

for i in range(12):  # size of a line
    l = []
    for line in lines:
        l.append(line[i])

    if l.count("0") > l.count("1"):
        selected = "1"
    else:
        selected = "0"

    for line in lines:
        if line[i] != selected:
            candidates.remove(line)

    lines = candidates.copy()
    if len(candidates) == 1:
        break

co2 = int(candidates[0], 2)

print(ogr * co2)
