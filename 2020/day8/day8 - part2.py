import sys

file = open("../input.txt")
default = [line.replace("\n", "") for line in file.readlines()]

toChange = [i for i, inst in enumerate(default) if inst.split(" ")[0] in ['jmp', 'nop']]

def exitMethod(acc):
    print(acc)
    sys.exit()


for i in toChange:
    program = default.copy()
    lineToChange = program[i].split(" ")
    lineToChange = f"jmp {lineToChange[1]}" if lineToChange[0] == "nop" else f"nop {lineToChange[1]}"
    program[i] = lineToChange
    
    visitedInst = []
    acc = 0
    i = 0
    while True:
        if i >= len(program): exitMethod(acc)
        inst, arg = program[i].split(" ")
        if i in visitedInst: break
        
        visitedInst.append(i)
        if inst == "nop": i += 1
        if inst == "acc":
            acc += int(arg)
            i += 1
        if inst == "jmp": i += int(arg)