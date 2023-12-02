file = open("input.txt")
lines = file.readlines()

reactor = set()
for line in lines:
    state, coords = line.replace("\n", "").split(" ")
    x, y, z = coords.split(",")
    x = tuple(map(int, x.split("=")[1].split("..")))
    y = tuple(map(int, y.split("=")[1].split("..")))
    z = tuple(map(int, z.split("=")[1].split("..")))
    if x[0] < -50 or x[1] > 50:
        break

    state = state == "on"

    for _x in range(x[0], x[1] + 1):
        for _y in range(y[0], y[1] + 1):
            for _z in range(z[0], z[1] + 1):
                if state:
                    reactor.add((_x, _y, _z))
                else:
                    if (_x, _y, _z) in reactor:
                        reactor.remove((_x, _y, _z))

print(len(reactor))
