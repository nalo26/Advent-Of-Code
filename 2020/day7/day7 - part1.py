file = open("./input.txt")


class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = {}
        self.canContainsMine = False


bags = []
myBag = "shiny gold"


def getBag(name):
    for bag in bags:
        if name == bag.name:
            return bag
    return None


def doesBagContains(bag):
    if bag.canContainsMine:
        return True
    for b in bag.contains:
        if doesBagContains(getBag(b)):
            return True
    return False


for line in file.readlines():
    name, content = line.split("contain ")
    name = name.split(" ")[:2]
    newBag = Bag(" ".join(name))
    bags.append(newBag)

    if not "no " in content:
        content = content.split(", ")
        for bag in content:
            curBag = bag.split(" ")
            name = " ".join(curBag[1:3])
            if name == myBag:
                newBag.canContainsMine = True
            newBag.contains[name] = int(curBag[0])

res = 0
for bag in bags:
    if doesBagContains(bag):
        res += 1

print(res)
