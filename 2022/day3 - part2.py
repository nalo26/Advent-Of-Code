from string import ascii_letters

file = open("input.txt")
lines = file.read().splitlines()

val = 0
for i in range(0, len(lines), 3):
    a, b, c = (lines[j] for j in range(i, i + 3))
    diff = set(a).intersection(set(b)).intersection(set(c)).pop()
    val += ascii_letters.index(diff) + 1

print(val)
