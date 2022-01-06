file = open("input.txt")
lines = file.readlines()

tot = 0
for line in lines:
    l, w, h = list(map(int, line.split("x")))
    min_face = min(l*w, w*h, l*h)
    tot += 2*l*w + 2*w*h + 2*h*l + min_face

print(tot)