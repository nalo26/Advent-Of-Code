file = open("input.txt")
lines = file.readlines()

tot = 0
for line in lines:
    l, w, h = list(map(int, line.split("x")))
    min_face = min(l*2+w*2, w*2+h*2, l*2+h*2)
    tot += l*w*h + min_face

print(tot)