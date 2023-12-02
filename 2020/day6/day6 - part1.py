file = open("input.txt")
content = file.read()

lines = content.split("\n\n")

res = []
for line in lines:
    questions = {}
    for char in line:
        if char == "\n":
            continue
        questions[char] = 1
    res.append(sum(questions.values()))

print(sum(res))

# print(sum([len(set(i.replace('\n', ''))) for i in open("input.txt").read().split("\n\n")]))
