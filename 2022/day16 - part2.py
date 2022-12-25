import re
from functools import cache


file = open("input.txt")
lines = file.read().splitlines()
valves = {}


@cache
def compute1(opened, minutes, current):
    if minutes <= 0:
        return 0

    best = 0
    curr = valves.get(current)
    for neigh in curr.get("neighs"):
        best = max(best, compute1(opened, minutes - 1, neigh))

    if current not in opened and curr.get("rate") > 0 and minutes > 0:
        opened = set(opened)
        opened.add(current)
        minutes -= 1
        nsum = minutes * curr.get("rate")

        for neigh in curr.get("neighs"):
            best = max(best, nsum + compute1(frozenset(opened), minutes - 1, neigh))
        
    return best

@cache
def compute2(opened, minutes, current):
    if minutes <= 0:
        return compute1(opened, 26, "AA")

    best = 0
    curr = valves.get(current)
    for neigh in curr.get("neighs"):
        best = max(best, compute2(opened, minutes - 1, neigh))

    if current not in opened and curr.get("rate") > 0 and minutes > 0:
        opened = set(opened)
        opened.add(current)
        minutes -= 1
        nsum = minutes * curr.get("rate")

        for neigh in curr.get("neighs"):
            best = max(best, nsum + compute2(frozenset(opened), minutes - 1, neigh))
        
    return best


for line in lines:
    match = re.search("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", line)
    name, rate, neighs = match.groups()
    rate = int(rate)
    neighs = neighs.split(", ")

    valves[name] = {"rate": rate, "neighs": neighs}

print(compute2(frozenset(), 26, "AA"))
