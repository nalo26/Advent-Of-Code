import networkx as nx

from lib.input import get_input

lines = [tuple(line.split("-")) for line in get_input(2024, 23).splitlines()]
graph = nx.Graph(lines)


def part1():
    res = 0
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) != 3:
            continue
        if any(n.startswith("t") for n in clique):
            res += 1
    return res


def part2():
    # find longest clique (all connected subgraph), sort, join
    return ",".join(sorted(max(nx.find_cliques(graph), key=len)))
