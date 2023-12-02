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


i = 25
for inp in lines[25:]:
    if not isSumOfTwoPreamble(inp, lines[i - 25 :][:25]):
        print(inp)
        break
    i += 1
