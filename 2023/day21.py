file = open("input.txt")
lines = file.read().splitlines()


class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.neighbours = []


CARDS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

start_coords = None
nodes = []
nodes_by_coords = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            continue
        if c == "S":
            start_coords = (x, y)

        node = Node(x, y)
        for card in CARDS:
            neigh = nodes_by_coords.get((x + card[0], y + card[1]))
            if neigh is None:
                continue

            node.neighbours.append(neigh)
            neigh.neighbours.append(node)

        nodes.append(node)
        nodes_by_coords[(x, y)] = node

start = nodes_by_coords[start_coords]


def discover(start, steps):
    queue = set()
    queue.add(start)
    for _ in range(steps):
        queue = {neigh for node in queue for neigh in node.neighbours}
    return queue


def part1():
    return len(discover(start, 64))


def part2():
    pass


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
