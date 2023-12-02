file = open("input.txt")
lines = file.readlines()


def pretty_print(table):
    for row in table:
        for col in row:
            print("#" if col == 1 else " ", end=" ")
        print()


max_x = 0
max_y = 0
points = []
folds = []
for line in lines:
    line = line.replace("\n", "")

    if line == "":
        continue
    if line.startswith("fold"):
        axe, ind = line[11:].split("=")
        folds.append((axe, int(ind)))
    else:
        x, y = list(map(int, line.split(",")))
        points.append((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

sheet = []
for y in range(max_y + 1):
    line = [0] * (max_x + 1)
    sheet.append(line)

for x, y in points:
    sheet[y][x] = 1


def fold_y(sheet, ind):
    for y, row in enumerate(sheet[ind + 1 :]):
        for x, col in enumerate(row):
            sheet[ind - y - 1][x] = int(1 in (col, sheet[ind - y - 1][x]))
    return sheet[:ind]


def fold_x(sheet, ind):
    new_sheet = []
    for y, row in enumerate(sheet):
        for x, col in enumerate(row[ind + 1 :]):
            sheet[y][ind - x - 1] = int(1 in (col, sheet[y][ind - x - 1]))
        new_sheet.append(sheet[y][:ind])
    return new_sheet


for axe, ind in folds:
    if axe == "y":
        sheet = fold_y(sheet, ind)
    if axe == "x":
        sheet = fold_x(sheet, ind)

pretty_print(sheet)
