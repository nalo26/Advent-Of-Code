file = open("input.txt")
lines = file.read().splitlines()

# A, X : Rock
# B, Y : Paper
# C, Z : Scissors
POSSIBILITIES = {
    "A": {"A": 3, "B": 6, "C": 0},
    "B": {"A": 0, "B": 3, "C": 6},
    "C": {"A": 6, "B": 0, "C": 3},
}
POINTS = {"A": 1, "B": 2, "C": 3}

total_score = 0
for line in lines:
    a, i = line.split()
    b = None
    match i:
        case "X":  # loose
            b = list(POSSIBILITIES[a].keys())[list(POSSIBILITIES[a].values()).index(0)]
        case "Y":  # draw
            b = a
        case "Z":  # win
            b = list(POSSIBILITIES[a].keys())[list(POSSIBILITIES[a].values()).index(6)]
    total_score += POSSIBILITIES[a][b] + POINTS[b]

print(total_score)
