file = open("input.txt")

line = file.read()

p_size = 14

for i in range(len(line)-(p_size-1)):
    if len(set(line[i:i+p_size])) == p_size:
        print(i+p_size)
        break