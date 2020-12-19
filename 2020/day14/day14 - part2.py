file = open("input.txt")
lines = [line.replace("\n", "") for line in file.readlines()]

mask = ""
mem = {}

def processAdress(address, mask):
    binAddr = bin(address)[2:]
    binAddr = list('0'*(len(mask) - len(binAddr)) + binAddr)
    newAddr = []
    for a, m in zip(binAddr, mask):
        newAddr.append(a if m == "0" else m)
    res = []
    countX = newAddr.count("X")
    for i in range(2**countX):
        binVal = bin(i)[2:]
        binVal = list('0'*(countX - len(binVal)) + binVal)
        tmpAddr = newAddr.copy()
        indexOfBinVal = 0
        for j in range(len(newAddr)):
            if newAddr[j] == "X":
                tmpAddr[j] = binVal[indexOfBinVal]
                indexOfBinVal += 1
        res.append(str(int("".join(tmpAddr), 2)))
    return res


for line in lines:
    if line.startswith("mask"): mask = line.split(" = ")[-1]
    else:
        addr, val = line.split(" = ")
        val = int(val)
        addr = int(addr.replace("mem[", "").replace("]", ""))
        for a in processAdress(addr, mask):
            mem[a] = val
    
print(sum(list(map(int, mem.values()))))