file = open("input.txt")

res = 0
for entry in file.readlines():
    line = entry.split(" ")
    pos = list(map(int, line[0].split("-")))
    letter = line[1][0]
    pwd = line[2]
    
    if (pwd[pos[0]-1] == letter) ^ (pwd[pos[1]-1] == letter): res += 1
    
print(res)