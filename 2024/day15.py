from lib.consts import D, L, R, U
from lib.input import get_input
from lib.map import Map, Position

dir = {"^": U, ">": R, "v": D, "<": L}
extension = {"#": "##", "O": "[]", ".": "..", "@": "@."}

lines = get_input(2024, 15).split("\n\n")

instructions = [dir.get(d) for d in lines[1].replace("\n", "")]


def can_move(map: Map, pos: Position, dir: Position, moved: set[Position]):
    target = pos + dir
    if target in moved:
        return True
    moved.add(target)
    match map[target]:
        case ".":
            return True
        case "#":
            return False
        case "O":
            return can_move(map, target, dir, moved)
        case "[":
            return can_move(map, target, dir, moved) and can_move(map, target + R, dir, moved)
        case "]":
            return can_move(map, target, dir, moved) and can_move(map, target + L, dir, moved)
    return False


def make_move(map: Map, pos: Position, dir: Position, moved: set[Position]):
    target = pos + dir
    if target in moved:
        return
    moved.add(target)
    match map[target]:
        case "#":
            return
        case "O":
            make_move(map, target, dir, moved)
        case "[":
            make_move(map, target, dir, moved)
            make_move(map, target + R, dir, moved)
        case "]":
            make_move(map, target, dir, moved)
            make_move(map, target + L, dir, moved)
    move_to(map, pos, target)


def move_to(map: Map, f: Position, t: Position):
    map[f], map[t] = map[t], map[f]


def try_move(map: Map, pos: Position, dir: Position):
    target = pos + dir
    match map[target]:
        case "." | "@":
            return target
        case "#":
            return pos
        case "O" | "[" | "]":
            if can_move(map, pos, dir, set()):
                make_move(map, pos, dir, set())
                return target
            return pos


def value(map: Map, box: str):
    return sum(b.x + 100 * b.y for b in map.find_all(box))


def part1():
    map = Map([list(line) for line in lines[0].split("\n")])
    robot = map.find("@")
    map[robot] = "."
    for inst in instructions:
        robot = try_move(map, robot, inst)

    return value(map, "O")


def part2():
    map = Map([list("".join(extension.get(char) for char in line)) for line in lines[0].split("\n")])
    robot = map.find("@")
    map[robot] = "."
    for inst in instructions:
        robot = try_move(map, robot, inst)

    return value(map, "[")
