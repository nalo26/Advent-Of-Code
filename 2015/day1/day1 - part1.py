file = open("input.txt")

floor = 0
for char in file.readline():
    if char == '(': floor += 1
    if char == ')': floor -= 1

print(floor)