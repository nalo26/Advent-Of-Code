from collections import Counter

file = open("input.txt")
fishes = Counter(map(int, file.read().split(",")))

for i in range(256):
    newGen = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    toAdd = 0
    for fish, val in fishes.items():
        if val == 0: continue
        if fish == 0:
            newGen[6] += val
            newGen[8] += val
        else: newGen[fish-1] += val
    fishes = newGen.copy()
    del newGen

print(sum(list(fishes.values())))