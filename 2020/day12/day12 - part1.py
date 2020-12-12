from enum import Enum

file = open("input.txt")
lines = file.readlines()

class Directon(Enum):
    EAST = 0
    SOUTH = 90
    WEST = 180
    NORTH = 270
    
    
hor = 0
ver = 0
ori = Directon.EAST.value

for line in lines:
    action, val = line[0], int(line[1:])
    if action == "N": ver += val
    if action == "S": ver -= val
    if action == "E": hor += val
    if action == "W": hor -= val
    if action == "R": ori = (ori + val) % 360
    if action == "L": ori = (ori - val) % 360
    if action == "F": 
        if ori == Directon.NORTH.value: ver += val
        if ori == Directon.SOUTH.value: ver -= val
        if ori == Directon.EAST.value : hor += val
        if ori == Directon.WEST.value : hor -= val
    # print(line[:-1], "\t", hor, ver, ori)
    
print(abs(ver) + abs(hor))