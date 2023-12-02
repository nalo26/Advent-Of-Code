file = open("input.txt")

OPENING = "([{<"
CLOSING = ")]}>"

scores = []
for line in file.readlines():
    stack = []
    skip = False
    for char in line.replace("\n", ""):
        if char in OPENING:
            stack.append(char)
            continue

        expected = CLOSING[OPENING.index(stack[-1])]
        if char != expected:
            skip = True
            break
        stack.pop(-1)

    if len(stack) == 0 or skip:
        continue
    # ending line without closing everything
    score = 0
    for char in stack[::-1]:
        score *= 5
        score += OPENING.index(char) + 1
    scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])
