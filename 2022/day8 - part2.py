file = open("input.txt")
lines = file.read().splitlines()
forest = [list(map(int, list(line))) for line in lines]


def getLineScore(line, v):
    score = 0
    for t in line:
        score += 1
        if t >= v:
            break
    return score


def getScenicScore(x, y, v, grid):
    if x in (0, len(grid[0])-1) or y in (0, len(grid)-1):
        return 0
    
    up = getLineScore([l[x] for l in grid[:y]][::-1], v)
    left = getLineScore(grid[y][:x][::-1], v)
    down = getLineScore([l[x] for l in grid[y+1:]], v)
    right = getLineScore(grid[y][x+1:], v)

    return up * left * down * right


scores = set()
for y, line in enumerate(forest):
    for x, tree in enumerate(line):
        score = getScenicScore(x, y, tree, forest)
        scores.add(score)

print(max(scores))