import sys

file = open("input.txt")
lines = [int(line.replace("\n", "")) for line in file.readlines()]


def isSumOfTwoPreamble(n, preamble):
    for a in preamble:
        for b in preamble:
            if a == b:
                continue
            if a + b == n:
                return True
    return False


invalidNumber = 0
i = 25
for inp in lines[25:]:
    if not isSumOfTwoPreamble(inp, lines[i - 25 :][:25]):
        # print(inp)
        invalidNumber = inp
        break
    i += 1


for i in range(2, len(lines)):
    for n in range(len(lines) - i):
        toCheck = lines[n:][:i]
        if sum(toCheck) == invalidNumber:
            print(i, n, toCheck)
            print(min(toCheck) + max(toCheck))
            sys.exit()
