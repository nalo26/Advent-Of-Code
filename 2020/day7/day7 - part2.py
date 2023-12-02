file = open("./input.txt")


class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = {}


bags = []
myBag = "shiny gold"


def getBag(name):
    for bag in bags:
        if name == bag.name:
            return bag
    return None


def getContainingAmount(bag):
    res = 0
    for bagName in bag.contains:
        b = getBag(bagName)
        res += bag.contains[bagName]
        res += bag.contains[bagName] * getContainingAmount(b)
    return res


entry = None
for line in file.readlines():
    name, content = line.split("contain ")
    name = " ".join(name.split(" ")[:2])
    newBag = Bag(name)
    bags.append(newBag)
    if name == myBag:
        entry = newBag

    if not "no " in content:
        content = content.split(", ")
        for bag in content:
            curBag = bag.split(" ")
            name = " ".join(curBag[1:3])
            newBag.contains[name] = int(curBag[0])


print(getContainingAmount(entry))
