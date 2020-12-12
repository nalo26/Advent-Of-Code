file = open("input.txt")
lines = file.readlines()

def rotate(value, hor, ver):
    if value == 90:  return  ver,  -hor
    if value == 180: return -hor, -ver
    if value == 270: return -ver,  hor
    return hor, ver


hor_wp = 10
ver_wp = 1
hor_ship = 0
ver_ship = 0

for line in lines:
    action, val = line[0], int(line[1:])
    if action == "N": ver_wp += val
    if action == "S": ver_wp -= val
    if action == "E": hor_wp += val
    if action == "W": hor_wp -= val
    if action == "R": hor_wp, ver_wp = rotate(val, hor_wp, ver_wp)
    if action == "L": hor_wp, ver_wp = rotate((360-val)%360, hor_wp, ver_wp)
    if action == "F": 
        hor_ship += hor_wp * val
        ver_ship += ver_wp * val
    # print(line[:-1], "\tship:", hor_ship, ver_ship, ", waypoint:", hor_wp, ver_wp)
    
print(abs(ver_ship) + abs(hor_ship))