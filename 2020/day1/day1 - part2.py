file = open("input.txt")

lines = file.readlines()

for i, n in enumerate(lines):  # THIS IS UGLY
    for j, m in enumerate(lines):
        for k, l in enumerate(lines):
            if i == j or j == k or i == k:
                continue
            if n + m + l != 2020:
                continue
            print(n * m * l)

# print([n*m*l for l in lines for m in lines for n in lines if n+m+l==2020][0])
