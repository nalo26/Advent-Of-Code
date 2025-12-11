from functools import cache

from lib.input import get_input

lines = get_input(2025, 11).splitlines()
servers = {}
for line in lines:
    target, others = line.split(": ")
    servers[target] = set(others.split())


@cache
def count_routes(start_server):
    if start_server == "out":
        return 1

    return sum(count_routes(conn) for conn in servers[start_server])


@cache
def check_routes(start_server, target=0):
    if start_server in ("dac", "fft"):
        target += 1
    if start_server == "out":
        return 1 if target == 2 else 0

    return sum(check_routes(conn, target) for conn in servers[start_server])


def part1():
    return count_routes("you")


def part2():
    return check_routes("svr")
