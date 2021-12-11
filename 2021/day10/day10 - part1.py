file = open("input.txt")

OPENING = "{([<"
CLOSING = "})]>"
SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}

score = 0
for line in file.readlines():
    stack = []
    for char in line.replace("\n",""):
        if char in OPENING:
            stack.append(char)
            continue

        expected = CLOSING[OPENING.index(stack[-1])]
        if char != expected:
            score += SCORES[char]
            break
        stack.pop(-1)
    
print(score)