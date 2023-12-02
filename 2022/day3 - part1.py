from string import ascii_letters

file = open("input.txt")
lines = file.read().splitlines()

val = 0
for line in lines:
    a, b = line[: len(line) // 2], line[len(line) // 2 :]
    diff = set(a).intersection(set(b)).pop()
    val += ascii_letters.index(diff) + 1

print(val)
