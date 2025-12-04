from lib.input import get_input
from lib.map import Map

lines = get_input(2025, 4)

CARDS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def get_accessible_paper(diagram: Map):
    for paper_pos in diagram.find_all("@"):
        empty = 0
        for card in CARDS:
            check_pos = paper_pos + card
            if not diagram.is_in_bounds(check_pos) or diagram[check_pos] == ".":
                empty += 1
        if empty > 4:
            yield paper_pos


def part1():
    return len(list(get_accessible_paper(Map(lines))))


def part2():
    diagram = Map(lines)
    res = 0
    while True:
        accessible_papers = list(get_accessible_paper(diagram))
        if not accessible_papers:
            break
        res += len(accessible_papers)
        for pos in accessible_papers:
            diagram[pos] = "."
    return res
