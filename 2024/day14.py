import re
from math import prod

from lib.input import get_input
from lib.map import Position

WIDTH = 101
HEIGHT = 103
PATTERN = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")


class Robot:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def move(self):
        self.pos += self.vel
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT

    @property
    def cadran(self):
        if self.pos.x < WIDTH // 2:
            return 0 if self.pos.y < HEIGHT // 2 else 2 if self.pos.y > HEIGHT // 2 else 4
        elif self.pos.x > WIDTH // 2:
            return 1 if self.pos.y < HEIGHT // 2 else 3 if self.pos.y > HEIGHT // 2 else 4
        return 4


lines = get_input(2024, 14).splitlines()
robots = set()
for line in lines:
    numbers = [int(x) for x in PATTERN.match(line).groups()]
    pos = Position(numbers[0], numbers[1])
    vel = Position(numbers[2], numbers[3])
    robots.add(Robot(pos, vel))


def part1():
    res = [0] * 5  # 4 cadran + ignored middles ones
    for _ in range(100):
        for robot in robots:
            robot.move()
    for robot in robots:
        res[robot.cadran] += 1

    return prod(res[:4])


def part2():
    for i in range(10000):
        for robot in robots:
            robot.move()
        if len({robot.pos for robot in robots}) == 500:
            break
    return i + 1 + 100  # part1 offset
