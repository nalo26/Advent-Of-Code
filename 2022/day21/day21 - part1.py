from operator import add, sub, mul, truediv

file = open("input.txt")
lines = file.read().splitlines()

operators = {"+": add, "-": sub, "*": mul, "/": truediv}
operations = {}
for line in lines:
    name, op = line.split(": ")
    operations[name] = op


def compute(name):
    op = operations[name]
    if op.isdigit():
        return int(op)
    a, o, b = op.split()
    return int(operators[o](compute(a), compute(b)))


print(compute("root"))
