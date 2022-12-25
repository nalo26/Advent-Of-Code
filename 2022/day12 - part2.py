class Edge:
    def __init__(self, s1, s2, value) -> None:
        self.start = s1
        self.stop = s2
        self.value = value


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.in_edges = []
        self.out_edges = []


CARDS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

file = open("input.txt")
lines = file.read().splitlines()

nodes = []
nodes_by_coords = {}
stop_coords = set()
start_coord = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "a":
            stop_coords.add((x, y)) 
        if c == "E": 
            start_coord = (x, y)
            c = "z"
        node = Node(c)
        for card in CARDS:
            neigh = nodes_by_coords.get((x + card[0], y + card[1]))
            if neigh is None:
                continue

            value = ord(neigh.value) - ord(node.value)
            if value >= -1:
                edge_to = Edge(node, neigh, 1)
                node.out_edges.append(edge_to)
                neigh.in_edges.append(edge_to)
            
            if value <= 1:
                edge_from = Edge(neigh, node, 1)
                node.in_edges.append(edge_from)
                neigh.out_edges.append(edge_from)

        nodes.append(node)
        nodes_by_coords[(x, y)] = node

start = nodes_by_coords[start_coord]


def dijkstra(start):
    dist = {node: float("inf") for node in nodes}
    dist[start] = 0
    queue = [start]
    while queue:
        node = queue.pop(0)
        for edge in node.out_edges:
            if dist[edge.stop] > dist[node] + edge.value:
                dist[edge.stop] = dist[node] + edge.value
                queue.append(edge.stop)
    return dist

dij = dijkstra(start)
print(min(dij.get(nodes_by_coords.get(coord)) for coord in stop_coords))