from typing import List, Tuple


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Position" | Tuple[int, int]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return Position(self.x + other[0], self.y + other[1])

    def __sub__(self, other: "Position" | Tuple[int, int]) -> "Position":
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y)
        return Position(self.x - other[0], self.y - other[1])

    def __iter__(self):
        return iter((self.x, self.y))

    def __repr__(self) -> str:
        return f"Position({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Map[T]:
    def __init__(self, grid: List[List[T]] | str) -> None:
        if isinstance(grid, str):
            grid = [list(line) for line in grid.splitlines()]
        self.grid = grid

    def __getitem__(self, pos: Position | Tuple[int, int]) -> T:
        if isinstance(pos, Position):
            pos = (pos.x, pos.y)
        if not self.is_in_bounds(pos):
            raise IndexError(f"Position {pos} is out of bounds")
        return self.grid[pos[1]][pos[0]]

    def __setitem__(self, pos: Position | Tuple[int, int], value: T) -> None:
        if isinstance(pos, Position):
            pos = (pos.x, pos.y)
        if not self.is_in_bounds(pos):
            raise IndexError(f"Position {pos} is out of bounds")
        self.grid[pos[1]][pos[0]] = value

    # copy method
    def copy(self) -> "Map":
        return Map([row.copy() for row in self.grid])

    def is_in_bounds(self, pos: Position | Tuple[int, int]) -> bool:
        if isinstance(pos, Position):
            pos = (pos.x, pos.y)
        return 0 <= pos[1] < len(self.grid) and 0 <= pos[0] < len(self.grid[0])

    def find(self, value: T) -> Position | None:
        for y, row in enumerate(self.grid):
            if value in row:
                return Position(row.index(value), y)
        return None

    def find_all(self, value: T) -> list[Position]:
        return [Position(x, y) for y, row in enumerate(self.grid) for x, cell in enumerate(row) if cell == value]

    def rotate(self) -> "Map":
        # rotate 90 degrees clockwise
        return Map([row for row in zip(*self.grid[::-1])])

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.grid)

    def __repr__(self) -> str:
        return f"Map({self.grid})"

    def __iter__(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                yield Position(x, y), cell

    @property
    def height(self) -> int:
        return len(self.grid)

    @property
    def width(self) -> int:
        if self.height in (0, 1):
            return 0
        return len(self.grid[0])
