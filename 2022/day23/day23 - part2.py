from enum import Enum

file = open("input.txt")
lines = file.read().splitlines()


class Card(Enum):
    NORTH = ((0, -1), (-1, -1), (1, -1))
    SOUTH = ((0, 1), (-1, 1), (1, 1))
    WEST = ((-1, 0), (-1, -1), (-1, 1))
    EAST = ((1, 0), (1, -1), (1, 1))
    ALL = ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))


class Elf:
    CARDS = [Card.NORTH, Card.SOUTH, Card.WEST, Card.EAST]

    def __init__(self, x, y) -> None:
        self.coord = (x, y)
        self.simulate_coord = (None, None)

    def simulate_move(self, other_elves):
        if all(
            (self.coord[0] + c[0], self.coord[1] + c[1]) not in other_elves
            for c in Card.ALL.value
        ):
            return (None, None)
        for cards in Elf.CARDS:
            for card in cards.value:
                if (self.coord[0] + card[0], self.coord[1] + card[1]) in other_elves:
                    break
            else:
                self.simulate_coord = (
                    self.coord[0] + cards.value[0][0],
                    self.coord[1] + cards.value[0][1],
                )
                return self.simulate_coord
        return (None, None)

    def move(self, other_elves):
        if (
            None not in self.simulate_coord
            and other_elves.count(self.simulate_coord) == 1
        ):
            self.coord = self.simulate_coord
        self.simulate_coord = (None, None)
        return self.coord


elves = set()
elves_by_coord = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            elf = Elf(x, y)
            elves.add(elf)
            elves_by_coord[(x, y)] = elf

count = 0
while True:
    count += 1
    simulations = []
    for elf in elves:
        simulations.append(elf.simulate_move(elves_by_coord))
    moved = []
    for elf in elves:
        old_coord = elf.coord
        new_coord = elf.move(simulations)
        if old_coord != new_coord:
            elves_by_coord.pop(old_coord)
            elves_by_coord[new_coord] = elf
            moved.append(True)
        else:
            moved.append(False)
    Elf.CARDS.append(Elf.CARDS.pop(0))
    if not any(moved):
        break

print(count)
