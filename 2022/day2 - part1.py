file = open("input.txt")
lines = file.read().splitlines()

# A, X : Rock
# B, Y : Paper
# C, Z : Scissors
POSSIBILITIES = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}
POINTS = {"X": 1, "Y": 2, "Z": 3}

total_score = 0
for line in lines:
    a, b = line.split()
    total_score += POSSIBILITIES[a][b] + POINTS[b]

print(total_score)
