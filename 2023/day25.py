import networkx as nx

file = open("input.txt")
lines = file.read().splitlines()

g = nx.Graph()
for line in lines:
    comp_from, neighbor = line.split(": ")
    for comp in neighbor.split():
        g.add_edge(comp_from, comp)


def part1():
    _, partitions = nx.stoer_wagner(g)
    return len(partitions[0]) * len(partitions[1])


print("Part 1:", part1())
file.close()
