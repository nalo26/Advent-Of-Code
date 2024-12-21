from tqdm import tqdm

from lib.consts import DIR_CROSS
from lib.input import get_input
from lib.map import Position

lines = get_input(2024, 20).splitlines()


class Node:
    def __init__(self, value, pos: Position):
        self.value = value
        self.pos = pos
        self.neighbours: list[Node] = []


nodes = []
nodes_by_coords: dict[Position, Node] = {}
start = stop = None
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == "#":
            continue
        pos = Position(x, y)
        node = Node(1, pos)
        if cell == "S":
            start = node
        if cell == "E":
            stop = node

        for dir in DIR_CROSS:
            neigh = nodes_by_coords.get(pos + dir)
            if neigh is None:
                continue

            node.neighbours.append(neigh)
            neigh.neighbours.append(node)

        nodes.append(node)
        nodes_by_coords[pos] = node


def dijkstra(start, stop):
    dist = {node: float("inf") for node in nodes}
    dist[start] = 0
    queue = [start]
    backtrace = {start: None}
    while queue:
        node = queue.pop(0)
        for neigh in node.neighbours:
            if dist[neigh] > dist[node] + neigh.value:
                dist[neigh] = dist[node] + neigh.value
                queue.append(neigh)
                backtrace[neigh] = node

    path = []
    current = stop
    while True:
        path.append(current.pos)
        current = backtrace[current]
        if current is None:
            break
    return dist[stop], path[::-1]


def cheat(path: list[Position], distance: int):
    res = 0
    for id_path, pos in enumerate(tqdm(path)):
        for id_shortcut, shortcut in enumerate(path[id_path + 1 :], start=id_path + 1):
            dist = pos.dist(shortcut)
            saved = id_shortcut - id_path - dist
            if dist > distance or saved <= 0:
                continue
            if saved >= 100:
                res += 1
    return res


def part1():
    _, path = dijkstra(start, stop)
    return cheat(path, 2)


def part2():
    _, path = dijkstra(start, stop)
    return cheat(path, 20)
