file = open("input.txt")

fishes = list(map(int, file.read().split(",")))

newGen = []
for i in range(80):
    toAdd = 0
    for fish in fishes:
        if fish == 0:
            newGen.append(6)
            toAdd += 1
        else: newGen.append(fish-1)
    for j in range(toAdd):
        newGen.append(8)
    fishes = newGen.copy()
    del newGen
    newGen = []

print(len(fishes))