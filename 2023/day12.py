from tqdm import tqdm

file = open("input.txt")
lines = file.readlines()


def match(field, qte):
    in_group = False
    new_qte = []
    count = 0
    for elem in field:
        if elem == "#" and not in_group:
            in_group = True
        if elem == "#":
            count += 1
        if elem == "." and in_group:
            in_group = False
            new_qte.append(count)
            count = 0
    if in_group:
        new_qte.append(count)
    return new_qte == qte


def part1():
    count = 0
    for line in tqdm(lines):
        field, qte = line.split(" ")
        qte = list(map(int, qte.split(",")))
        unknown = [i for i, elem in enumerate(field) if elem == "?"]
        target = 2 ** len(unknown)
        for b in range(target):
            for i, pos in enumerate(unknown):
                field = field[:pos] + ("#" if ((b >> i) & 1) else ".") + field[pos + 1 :]
            if match(field, qte):
                count += 1
    return count


def part2():  # too slow!
    count = 0
    for line in tqdm(lines):
        field, qte = line.split(" ")
        field = "?".join([field] * 5)
        qte = list(map(int, qte.split(","))) * 5
        unknown = [i for i, elem in enumerate(field) if elem == "?"]
        target = 2 ** len(unknown)
        for b in tqdm(range(target)):
            for i, pos in enumerate(unknown):
                field = field[:pos] + ("#" if ((b >> i) & 1) else ".") + field[pos + 1 :]
            if match(field, qte):
                count += 1
    return count


# print("Part 1:", part1())
print("Part 2:", part2())
file.close()
