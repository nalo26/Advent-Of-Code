from lib.consts import DIR_CROSS, D, L, R, U
from lib.input import get_input
from lib.map import Map, Position

map = Map([list(line) for line in get_input(2024, 12).splitlines()])


def get_shape(map, start_pos: Position, check_val: bool, value):
    shape = set()

    def get_region(pos: Position):
        if pos in shape:
            return
        if isinstance(map, Map) and not map.is_in_bounds(pos) or isinstance(map, list) and pos not in map:
            return
        if check_val and map[pos] != value:
            return

        shape.add(pos)
        for dir in DIR_CROSS:
            get_region(pos + dir)

    get_region(start_pos)
    return shape


def perimeter(shape: set[Position]):
    res = 0
    for s in shape:
        for dir in DIR_CROSS:
            if s + dir not in shape:
                res += 1
    return res


def sides(shape: set[Position]):
    min_x = min(p.x for p in shape)
    max_x = max(p.x for p in shape)
    min_y = min(p.y for p in shape)
    max_y = max(p.y for p in shape)

    def count_edges(shapes):
        visited = set()
        for pos in shapes:
            if pos in visited:
                continue
            shape = get_shape(shapes, pos, False, None)
            yield shape
            visited.update(shape)

    sides = 0
    for dir in (U, D):
        for y in range(min_y, max_y + 1):
            edges = []
            for x in range(min_x, max_x + 1):
                pos = Position(x, y)
                if pos not in shape:
                    continue
                if pos + dir not in shape:
                    edges.append(pos)
            sides += len(list(count_edges(edges)))

    for dir in (L, R):
        for x in range(min_x, max_x + 1):
            edges = []
            for y in range(min_y, max_y + 1):
                pos = Position(x, y)
                if pos not in shape:
                    continue
                if pos + dir not in shape:
                    edges.append(pos)
            sides += len(list(count_edges(edges)))

    return sides


def area(shape: set[Position]):
    return len(shape)


def get_shapes():
    visited = set()
    for pos, val in map:
        if pos in visited:
            continue
        shape = get_shape(map, pos, True, val)
        yield shape
        visited.update(shape)


def part1():
    res = 0
    for shape in get_shapes():
        res += area(shape) * perimeter(shape)
    return res


def part2():
    res = 0
    for shape in get_shapes():
        res += area(shape) * sides(shape)
    return res
