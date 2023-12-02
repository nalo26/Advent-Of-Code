file = open("input.txt")

lines = file.read()
elves = lines.split("\n\n")[:-1]
cals = [sum(int(cal) for cal in cals.split("\n")) for cals in elves]
cals.sort()
print(sum(cals[-3:]))
