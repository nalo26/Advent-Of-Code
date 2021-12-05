file = open("input.txt")

res = 0
last = None
for n in file.readlines():
    if last is not None:
        if int(n) > last: res += 1
    last = int(n)

print(res)