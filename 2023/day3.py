import re

file = open("input.txt")
default_lines = file.readlines()

SYMBOLS = {"#", "*", "$", "/", "+", "=", "%", "-", "@", "&"}
WIDTH = len(default_lines[0])
HEIGHT = len(default_lines)
CARDS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def extract_number(row, col):
    num_re = re.compile(r"\d+")
    while lines[row][col].isdigit() and col > 0:
        col -= 1
    extracted_num = num_re.search(lines[row], col).group()
    lines[row] = lines[row][:col] + lines[row][col:].replace(extracted_num, "." * len(extracted_num), 1)
    return int(extracted_num)


def extract_numbers(row, col):
    for x, y in CARDS:
        _row, _col = row + x, col + y
        if 0 <= _row < HEIGHT and 0 <= _col < WIDTH:
            if lines[_row][_col].isdigit():
                yield extract_number(_row, _col)


def part1():
    _sum = 0
    symbol_re = re.compile(r"[\#\*\$\/\+\=\-\%\@\&]")
    for i, line in enumerate(lines):
        for match in symbol_re.finditer(line):
            _sum += sum(extract_numbers(i, match.start()))

    return _sum


def part2():
    _sum = 0
    symbol_re = re.compile(r"\*")
    for i, line in enumerate(lines):
        for match in symbol_re.finditer(line):
            gears = list(extract_numbers(i, match.start()))
            if len(gears) == 2:
                _sum += gears[0] * gears[1]

    return _sum


lines = default_lines.copy()
print("Part 1:", part1())
lines = default_lines.copy()
print("Part 2:", part2())
file.close()
