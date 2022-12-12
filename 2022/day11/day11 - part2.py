from math import prod


file = open("input.txt")
lines = file.read().splitlines()


class Monkey:
    def __init__(self, id, items, op, divider, true, false) -> None:
        self.id = id
        self.items = items
        self.operation = op
        self.divider = divider
        self.target_true = true
        self.target_false = false
        self.inspect = 0

    def __repr__(self) -> str:
        return f"Monkey {self.id}: {', '.join(map(str, self.items))}"


monkeys = []

for i in range(0, len(lines), 7):
    m_id = int(lines[i].split()[1][:-1])
    items = list(map(int, lines[i + 1].split(": ")[1].split(", ")))
    op = lines[i + 2].split(": ")[1].split(" = ")[1]
    div = int(lines[i + 3].split(": ")[1].split()[-1])
    m_true = int(lines[i + 4].split()[-1])
    m_false = int(lines[i + 5].split()[-1])

    monkeys.append(Monkey(m_id, items, op, div, m_true, m_false))

mod = 1
for monkey in monkeys:
    mod *= monkey.divider

for _ in range(10000):
    for m in monkeys:
        for i, item in enumerate(m.items):
            m.inspect += 1
            m.items[i] = eval(m.operation.replace("old", str(item)))
            m.items[i] %= mod
            monkeys[
                m.target_true if m.items[i] % m.divider == 0 else m.target_false
            ].items.append(m.items[i])
        m.items = []

inspects = [m.inspect for m in monkeys]
inspects.sort()
print(prod(inspects[::-1][:2]))
