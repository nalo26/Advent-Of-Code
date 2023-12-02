file = open("input.txt")

res = 0
for line in file.readlines():
    inp, out = line.replace("\n", "").split(" | ")
    inp = inp.split(" ")
    out = out.split(" ")
    for o in out:
        if len(o) in (2, 4, 3, 7):
            res += 1

print(res)
