file = open("input.txt")
sequence = list(map(int, file.read().splitlines()))


class N:
    def __init__(self, v):
        self.v = v


sequence = [N(v) for v in sequence]
base = sequence.copy()

for n in base:
    i = sequence.index(n)
    sequence.pop(i)
    sequence.insert((i + n.v) % len(sequence), n)

values = [1000, 2000, 3000]
start = 0
for i, n in enumerate(sequence):
    if n.v == 0:
        start = i
        break

print(sum(sequence[(start + v) % len(sequence)].v for v in values))
