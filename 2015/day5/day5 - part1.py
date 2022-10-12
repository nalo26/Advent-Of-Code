file = open("input.txt")
lines = file.readlines()

VOWELS = "aeiou"
FORBIDEN = ("ab", "cd", "pq", "xy")

nice = 0
for line in lines:
    line = line.replace("\n", "")
    if sum(line.count(x) for x in VOWELS) < 3: continue
    if len([i for i in range(len(line[:-1])) if line[i] == line[i+1]]) < 1: continue 
    if any(x in line for x in FORBIDEN): continue

    nice += 1

print(nice)