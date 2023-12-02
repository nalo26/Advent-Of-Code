import re

file = open("input.txt")
lines = file.read().splitlines()

i = 0
stack_lines = []
while True:
    line = lines[i]
    if line.startswith(" 1"):
        break
    stack_lines.append(line)
    i += 1

stack_lines = [stack_lines[i][1::4] for i in range(len(stack_lines[0]) // 4)]
stacks = [[] for _ in range(len(stack_lines[0]))]
for i in range(len(stack_lines[0])):
    for line in stack_lines:
        if line[i] == " ":
            continue
        stacks[i].append(line[i])

for line in lines[i + 2 :]:
    match = re.search("move (\d*) from (\d*) to (\d*)", line)
    qte, i_s, i_e = tuple(map(int, match.groups()))
    for _ in range(qte):
        stacks[i_e - 1].insert(0, stacks[i_s - 1].pop(0))

print("".join((a[0] for a in stacks)))
