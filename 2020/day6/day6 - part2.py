file = open("input.txt")
content = file.read()

lines = content.split("\n\n")

res = []
for line in lines:
    ppl = len(line.split('\n'))
    questions = {}
    for char in line:
        if char == "\n": continue
        try: questions[char] += 1
        except KeyError: questions[char] = 1
    res.append(len([i for i in questions.values() if i == ppl]))

print(sum(res))