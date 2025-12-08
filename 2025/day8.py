from functools import reduce
from operator import mul

from networkx import Graph, connected_components

from lib.input import get_input

lines = get_input(2025, 8).splitlines()

# Create a graph from node positions
graph = Graph()
for line in lines:
    x, y, z = map(int, line.split(","))
    graph.add_node((x, y, z))

# Add edges with weights based on Euclidean distance
for node1 in graph.nodes:
    for node2 in graph.nodes:
        if node1 != node2:
            dist = ((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2 + (node1[2] - node2[2]) ** 2) ** 0.5
            graph.add_edge(node1, node2, weight=dist)

# Sort edges by weight to get the X shortest connections
edges = sorted(graph.edges(data=True), key=lambda x: x[2]["weight"])


def part1():
    connected_graph = graph.copy()
    connected_graph.clear_edges()

    for i in range(1000):
        # Add the edge to the connected graph
        connected_graph.add_edge(edges[i][0], edges[i][1])

    # Get the subgraphs of the connected graph
    subgraphs = sorted(connected_components(connected_graph), key=len, reverse=True)
    # Product of the sizes of the three largest subgraphs
    return reduce(mul, [len(sg) for sg in subgraphs[:3]])


def part2():
    connected_graph = graph.copy()
    connected_graph.clear_edges()

    for edge in edges:
        connected_graph.add_edge(edge[0], edge[1])
        # Check if the graph is fully connected
        subgraph = list(connected_components(connected_graph))
        if len(subgraph) == 1:
            # Return product of x-coordinates of connecting nodes
            return edge[0][0] * edge[1][0]
