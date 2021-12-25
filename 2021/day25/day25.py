file = open("input.txt")
seafloor = [list(line.replace("\n", "")) for line in file.readlines()]

def full_copy(table):
    return [line.copy() for line in table]

def move_cucumbers(floor, cucumber, n):
    new_seafloor = full_copy(floor)
    w, h = len(floor[0]), len(floor)
    for y, row in enumerate(floor):
        for x, col in enumerate(row):
            if col == cucumber and floor[(y+n[1]) % h][(x+n[0]) % w] == '.':
                new_seafloor[(y+n[1]) % h][(x+n[0]) % w] = cucumber
                new_seafloor[y][x] = '.'

    return new_seafloor


step = 0
while True:
    step += 1
    new_seafloor = move_cucumbers(seafloor, '>', (1, 0))
    new_seafloor = move_cucumbers(new_seafloor, 'v', (0, 1))

    if seafloor == new_seafloor:
        break

    seafloor = new_seafloor
    del new_seafloor

print(step)