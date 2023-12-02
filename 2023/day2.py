from collections import defaultdict
from functools import reduce
import operator

file = open("input.txt")
lines = file.readlines()

REQUIRED_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse(line: str):
    game, cubes = line.strip().split(": ")
    game_id = int(game.split(" ")[1])
    cubes_sub = cubes.split("; ")
    cubes_res = []
    for cube_sub in cubes_sub:
        cube_amounts = defaultdict(int)
        cubes = cube_sub.split(", ")
        for cube in cubes:
            amount, color = cube.split(" ")
            cube_amounts[color] = int(amount)
        cubes_res.append(cube_amounts)

    return game_id, cubes_res


def part1():
    _sum = 0
    for line in lines:
        game, cubes = parse(line)
        for cube in cubes:
            if any(cube[color] > REQUIRED_CUBES[color] for color in REQUIRED_CUBES):
                break
        else:
            _sum += game
    return _sum


def part2():
    power = 0
    for line in lines:
        _, cubes = parse(line)
        # get max amount of each color
        minimals = [max(cube[color] for cube in cubes) for color in REQUIRED_CUBES]
        # multiply them
        power += reduce(operator.mul, minimals, 1)
    return power


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
