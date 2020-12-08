file = open("../input.txt")

program = [line.replace("\n", "") for line in file.readlines()]

visitedInst = []
acc = 0
i = 0
while True:
    inst, arg = program[i].split(" ")
    if i in visitedInst: break
    
    visitedInst.append(i)
    if inst == "nop": i += 1
    if inst == "acc":
        acc += int(arg)
        i += 1
    if inst == "jmp": i += int(arg)
    
print(acc)