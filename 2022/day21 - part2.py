from sympy import Symbol, sympify
from sympy.solvers import solve

file = open("input.txt")
lines = file.read().splitlines()

operations = {}
for line in lines:
    name, op = line.split(": ")
    operations[name] = op


def compute(name):
    op = operations[name]
    if len(op.split()) == 1:
        return op
    a, o, b = op.split()
    if name == "root":
        return compute(a) + o + compute(b)
    return "(" + compute(a) + o + compute(b) + ")"


operations["humn"] = "x"
root = operations["root"].split()
operations["root"] = root[0] + " = " + root[2]
x = Symbol("x")
eq = compute("root").split("=")
eq = eq[0] + "-" + eq[1]
print(solve(sympify(eq))[0])
