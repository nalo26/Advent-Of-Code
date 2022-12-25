file = open("input.txt")
sequence = list(map(int, file.read().splitlines()))


class N:
    def __init__(self, v):
        self.v = v


key = 811589153
sequence = [N(v * key) for v in sequence]
base = sequence.copy()

for _ in range(10):
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
