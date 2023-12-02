file = open("input.txt")
lines = file.read().splitlines()


class Edge:
    def __init__(self, s1, s2, value) -> None:
        self.start = s1
        self.stop = s2
        self.value = value


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.explored = False
        self.in_edges = []
        self.out_edges = []


CARDS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

coords = set()
for line in lines:
    coords.add(tuple(map(int, line.split(","))))

max_x = max(coords, key=lambda c: c[0])[0]
min_x = min(coords, key=lambda c: c[0])[0]
max_y = max(coords, key=lambda c: c[1])[1]
min_y = min(coords, key=lambda c: c[1])[1]
max_z = max(coords, key=lambda c: c[2])[2]
min_z = min(coords, key=lambda c: c[2])[2]

nodes = []
nodes_by_coords = {}
start_coord = None
stop_coord = None
for z in range(min_z - 1, max_z + 2):
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y, z) in coords:
                continue

            node = Node((x, y, z))
            for card in CARDS:
                neigh = nodes_by_coords.get((x + card[0], y + card[1], z + card[2]))
                if neigh is None:
                    continue

                edge_from = Edge(neigh, node, 1)
                node.in_edges.append(edge_from)
                neigh.out_edges.append(edge_from)

                edge_to = Edge(node, neigh, 1)
                node.out_edges.append(edge_to)
                neigh.in_edges.append(edge_to)

            nodes.append(node)
            nodes_by_coords[(x, y, z)] = node


def bfs(start: Node):
    start.explored = True
    queue = [start]
    while queue:
        node = queue.pop(0)
        for edge in node.out_edges:
            if not edge.stop.explored:
                edge.stop.explored = True
                queue.append(edge.stop)


bfs(nodes_by_coords.get((min_x - 1, min_y - 1, min_z - 1)))

count = 0
for coord in coords:
    for card in CARDS:
        neigh = (coord[0] + card[0], coord[1] + card[1], coord[2] + card[2])
        if neigh in coords:
            continue
        if neigh in nodes_by_coords and not nodes_by_coords.get(neigh).explored:
            continue

        count += 1

print(count)
