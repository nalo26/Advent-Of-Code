file = open("input.txt")

floor = 0
for i, char in enumerate(file.readline(), 1):
    if char == '(': floor += 1
    if char == ')': floor -= 1
    if floor == -1: break

print(i)