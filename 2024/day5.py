import networkx as nx

from lib.input import get_input

lines = get_input(2024, 5).split("\n\n")

rules = [tuple(map(int, line.split("|"))) for line in lines[0].splitlines()]
updates = [list(map(int, line.split(","))) for line in lines[1].splitlines()]

invalid_updates = updates.copy()


def part1():
    res = 0
    for update in updates:
        for rule in rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                break
        else:
            invalid_updates.remove(update)  # for part 2
            res += update[len(update) // 2]
    return res


def part2():
    res = 0
    for update in invalid_updates:
        matchin_rules = []
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                matchin_rules.append(rule)
        graph = nx.DiGraph()
        graph.add_edges_from(matchin_rules)
        sorted_updates = list(nx.topological_sort(graph))
        res += sorted_updates[len(sorted_updates) // 2]
    return res
