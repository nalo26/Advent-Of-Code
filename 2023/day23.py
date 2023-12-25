import sys

file = open("input.txt")
lines = file.read().splitlines()

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.neighbours = []


CARDS = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}


def parse_part1():
    nodes = []
    nodes_by_coords = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "#>v<^":
                continue

            node = Node(x, y)
            for n, card in CARDS.items():
                if 0 <= (x + card[0]) < len(lines[0]) and 0 <= (y + card[1]) < len(lines):
                    match (lines[y + card[1]][x + card[0]], n):
                        case (">", "R") | ("<", "L") | ("^", "U") | ("v", "D"):
                            neigh = nodes_by_coords.get((x + card[0] * 2, y + card[1] * 2))
                            if neigh:
                                node.neighbours.append(neigh)
                        case (">", "L") | ("<", "R") | ("^", "D") | ("v", "U"):
                            neigh = nodes_by_coords.get((x + card[0] * 2, y + card[1] * 2))
                            if neigh:
                                neigh.neighbours.append(node)
                        case _:
                            neigh = nodes_by_coords.get((x + card[0], y + card[1]))
                            if neigh:
                                node.neighbours.append(neigh)
                                neigh.neighbours.append(node)

            nodes.append(node)
            nodes_by_coords[(x, y)] = node

    start = nodes_by_coords[(lines[0].index("."), 0)]
    stop = nodes_by_coords[(lines[-1].index("."), len(lines) - 1)]
    return nodes, start, stop


def parse_part2():
    nodes = []
    nodes_by_coords = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                continue

            node = Node(x, y)
            for card in CARDS.values():
                if 0 <= (x + card[0]) < len(lines[0]) and 0 <= (y + card[1]) < len(lines):
                    neigh = nodes_by_coords.get((x + card[0], y + card[1]))
                    if neigh:
                        node.neighbours.append(neigh)
                        neigh.neighbours.append(node)

            nodes.append(node)
            nodes_by_coords[(x, y)] = node

    start = nodes_by_coords[(lines[0].index("."), 0)]
    stop = nodes_by_coords[(lines[-1].index("."), len(lines) - 1)]
    return nodes, start, stop


def dijkstra(nodes, start, stop):
    dist = {node: 0 for node in nodes}
    backtrace = {start: None}

    def recursive_dijkstra(node, _visited):
        visited = _visited.copy()
        for neigh in node.neighbours:
            distance = dist[node] + abs(neigh.x - node.x) + abs(neigh.y - node.y)
            if neigh not in visited and dist[neigh] < distance:
                dist[neigh] = distance
                visited.add(neigh)
                backtrace[neigh] = node
                recursive_dijkstra(neigh, visited)

    recursive_dijkstra(start, {start})
    return dist, backtrace


def part1():
    nodes, start, stop = parse_part1()
    return dijkstra(nodes, start, stop)[0][stop]


def part2():
    nodes, start, stop = parse_part2()
    res, backtrace = dijkstra(nodes, start, stop)

    print(res.values())

    poss = set()
    current = stop
    while True:
        poss.add((current.x, current.y))
        # print(current.x, current.y)
        current = backtrace[current]
        if current is None:
            break

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (j, i) in poss:
                print("O", end="")
            else:
                print(lines[i][j], end="")
        print()
    return res[stop]


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
