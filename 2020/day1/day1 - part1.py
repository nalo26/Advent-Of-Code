file = open("input.txt")

lines = file.readlines()

for i, n in enumerate(lines):  # THIS IS UGLY
    for j, m in enumerate(lines):
        if i == j:
            continue
        if n + m != 2020:
            continue
        print(n * m)

# print([n*m for m in lines for n in lines if n+m==2020][0])
