file = open("input.txt")
nbList = list(map(int, file.readlines()[0].split(",")))


def process(nbList, n):
    lastSpoke = -1
    mostRecentSpokeBeforeThen = -1
    for i, v in enumerate(nbList[::-1]):
        if v == n:
            if lastSpoke == -1:
                lastSpoke = len(nbList) - i
                continue
            if mostRecentSpokeBeforeThen == -1:
                mostRecentSpokeBeforeThen = len(nbList) - i
                break
    else:
        return 0
    return lastSpoke - mostRecentSpokeBeforeThen


turns = 2020
for i in range(len(nbList), turns):
    nbList.append(process(nbList, nbList[-1]))

print(nbList[-1])
