file = open("input.txt")
lines = file.readlines()

gr = ""
for i in range(12): # size of a line
    l = []
    for line in lines:
        l.append(line[i])
    if l.count("0") > l.count("1"): gr += "0"
    else: gr += "1"

er = ""
for b in gr:
    er += str(int(not(bool(int(b)))))

print(int(gr, 2) * int(er, 2))