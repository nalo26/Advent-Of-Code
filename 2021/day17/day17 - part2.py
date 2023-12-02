file = open("input.txt")
x_area, y_area = file.readline()[13:].split(", ")
x_area = tuple(map(int, x_area[2:].split("..")))
y_area = tuple(map(int, y_area[2:].split("..")))


def vel_try(x, y):
    cur_pos = [0, 0]
    cur_vel = [x, y]
    while True:
        cur_pos[0] += cur_vel[0]
        cur_pos[1] += cur_vel[1]
        if cur_vel[0] > 0:
            cur_vel[0] -= 1
        cur_vel[1] -= 1

        if (
            x_area[0] <= cur_pos[0] <= x_area[1]
            and y_area[0] <= cur_pos[1] <= y_area[1]
        ):
            return True

        if cur_pos[0] > x_area[1] or cur_pos[1] < y_area[0]:
            return False


ys = []
for x in range(x_area[1] + 1):
    for y in range(y_area[0], 1000):
        if vel_try(x, y):
            ys.append((x, y))

print(len(ys))
