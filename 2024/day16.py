from lib.consts import DIR_CROSS, EAST
from lib.input import get_input
from lib.map import Position


class Node:
    def __init__(self, value, pos: Position):
        self.value = value
        self.pos = pos
        self.neighbours = []


lines = get_input(2024, 16).splitlines()

nodes = []
nodes_by_coords = {}
start, stop = None, None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":  # wall
            continue
        pos = Position(x, y)
        node = Node(1, pos)

        if c == "S":  # start
            start = node
        if c == "E":  # end
            stop = node

        for dir in DIR_CROSS:
            neigh = nodes_by_coords.get(pos + dir)
            if neigh is None:
                continue

            node.neighbours.append(neigh)
            neigh.neighbours.append(node)

        nodes.append(node)
        nodes_by_coords[pos] = node


def dijkstra(start: Node):
    dist = {(start, EAST): 0}
    paths = {(start, EAST): {start}}  # Paths to reach each state, not used in p1
    queue = [(0, start, EAST)]  # (distance, node, direction)

    while queue:
        current_dist, node, prev_dir = queue.pop(0)

        if current_dist > dist[(node, prev_dir)]:
            continue

        for neigh in node.neighbours:
            new_dir = neigh.pos - node.pos
            turn_cost = 1000 if prev_dir != new_dir else 0
            cost = current_dist + neigh.value + turn_cost

            state = (neigh, new_dir)

            if cost < dist.get(state, float("inf")):
                # Found a better path to this state
                dist[state] = cost
                paths[state] = paths[(node, prev_dir)] | {neigh}
                queue.append((cost, neigh, new_dir))
            elif cost == dist.get(state):
                # Found an equally good path to this state
                paths[state] |= paths[(node, prev_dir)] | {neigh}

    return dist, paths


def part1():
    dist, _ = dijkstra(start)
    dists = {node: min(dist.get((node, dir), float("inf")) for dir in DIR_CROSS) for node in nodes}
    return dists[stop]


def part2():
    _, paths = dijkstra(start)
    return min(len(paths[state]) for dir in DIR_CROSS if (state := (stop, dir)) in paths)
