file = open("input.txt")
lines = file.readlines()

ALGORITHM = lines[0][:-1]
picture = lines[2:]

NEIGHBOORS = [(-1, -1),(0, -1),(1, -1),(-1, 0),(0, 0),(1, 0),(-1, 1),(0, 1),(1, 1)]


def draw_border(picture, border_width, char):
    border = char*border_width
    for i, line in enumerate(picture):
        picture[i] = border + line.replace("\n", "") + border

    for _ in range(border_width):
        picture.insert(0, char * len(picture[0]))
        picture.append(char * len(picture[0]))

    return picture


def process(picture, void_char='.'):
    picture = draw_border(picture, 2, void_char)
    res = []
    for row in range(1, len(picture) - 1):
        new_row = ""
        for col in range(1, len(picture[row]) - 1):
            values = ""
            for x, y in NEIGHBOORS:
                values += picture[row + y][col + x]
            values = values.replace(".", "0").replace("#", "1")
            index = int(values, 2)
            new_row += ALGORITHM[index]
        res.append(new_row)
    return res


picture = process(picture)
picture = process(picture, ALGORITHM[0])

res = 0
for row in picture:
    res += row.count("#")

print(res)