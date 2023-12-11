file = open("input.txt")
lines = file.readlines()


def get_galaxies():
    galaxies = []
    for i, row in enumerate(lines):
        for j, col in enumerate(row):
            if col == "#":
                galaxies.append((i, j))
    return galaxies


def expand():
    expanded_rows, expanded_cols = [], []
    for i, row in enumerate(lines):
        if len(set(row.strip())) == 1 and row[0] == ".":
            expanded_rows.append(i)
            continue

    for j in range(len(lines[0].strip())):
        col = "".join([lines[i][j] for i in range(len(lines))])
        if len(set(col)) == 1 and col[0] == ".":
            expanded_cols.append(j)
            continue

    return expanded_rows, expanded_cols


def distance(exp, galaxy1, galaxy2, exp_rows, exp_cols):
    exp_y = sum(exp - 1 for r in exp_rows if min(galaxy1[0], galaxy2[0]) <= r <= max(galaxy1[0], galaxy2[0]))
    exp_x = sum(exp - 1 for c in exp_cols if min(galaxy1[1], galaxy2[1]) <= c <= max(galaxy1[1], galaxy2[1]))
    y = abs(galaxy1[0] - galaxy2[0])
    x = abs(galaxy1[1] - galaxy2[1])
    return (y + exp_y) + (x + exp_x)


def calculate(expansion):
    _sum = 0
    galaxies = get_galaxies()
    expanded_rows, expanded_cols = expand()
    for g, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[g:]:
            if galaxy1 == galaxy2:
                continue
            _sum += distance(expansion, galaxy1, galaxy2, expanded_rows, expanded_cols)
    return _sum


def part1():
    return calculate(2)


def part2():
    return calculate(1000000)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
