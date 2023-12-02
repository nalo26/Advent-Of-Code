file = open("input.txt")
lines = [line.replace("\n", "") for line in file.readlines()]

mask = ""
mem = {}


def processValue(value, mask):
    binVal = bin(value)[2:]
    binVal = list("0" * (len(mask) - len(binVal)) + binVal)
    res = ""
    for n, m in zip(binVal, mask):
        res += n if m == "X" else m
    return int(res, 2)


for line in lines:
    if line.startswith("mask"):
        mask = line.split(" = ")[-1]
    else:
        addr, val = line.split(" = ")
        val = int(val)
        addr = addr.replace("mem[", "").replace("]", "")
        mem[addr] = processValue(val, mask)

# print(mem)
print(sum(list(map(int, mem.values()))))
