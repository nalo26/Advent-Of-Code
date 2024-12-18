from lib.consts import DIR_CROSS
from lib.input import get_input
from lib.map import Position

WIDTH = 71
HEIGHT = 71

lines = get_input(2024, 18).splitlines()
bugs = [Position(*tuple(map(int, line.split(",")))) for line in lines]


class Node:
    def __init__(self, value, pos: Position):
        self.value = value
        self.pos = pos
        self.neighbours: list[Node] = []


nodes = []
nodes_by_coords: dict[Position, Node] = {}
for y in range(HEIGHT):
    for x in range(WIDTH):
        pos = Position(x, y)
        node = Node(1, pos)

        for dir in DIR_CROSS:
            neigh = nodes_by_coords.get(pos + dir)
            if neigh is None:
                continue

            node.neighbours.append(neigh)
            neigh.neighbours.append(node)

        nodes.append(node)
        nodes_by_coords[pos] = node

start = nodes_by_coords.get(Position(0, 0))
stop = nodes_by_coords.get(Position(WIDTH - 1, HEIGHT - 1))


def delete_node(coord: Position):
    node = nodes_by_coords.get(coord)
    for neigh in node.neighbours:
        neigh.neighbours.remove(node)
    nodes_by_coords.pop(coord)
    nodes.remove(node)


def dijkstra(start):
    dist = {node: float("inf") for node in nodes}
    dist[start] = 0
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neigh in node.neighbours:
            if dist[neigh] > dist[node] + neigh.value:
                dist[neigh] = dist[node] + neigh.value
                queue.append(neigh)
    return dist


def part1():
    for bug in bugs[:1024]:
        delete_node(bug)
    return dijkstra(start)[stop]


def part2():
    for bug in bugs[1024:]:
        delete_node(bug)
        if dijkstra(start)[stop] == float("inf"):
            return f"{bug.x},{bug.y}"
