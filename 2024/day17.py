from lib.input import get_input


class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]):
        self.regA = a
        self.regB = b
        self.regC = c
        self.program = program
        self.eip = 0

    def run(self):
        output = []
        while self.eip <= len(self.program) - 1:
            inst, op = self.program[self.eip], self.program[self.eip + 1]
            match inst:
                case 0:  # adv
                    self.regA = self.regA // (2 ** self.combo(op))
                case 1:  # bxl
                    self.regB = self.regB ^ op
                case 2:  # bst
                    self.regB = self.combo(op) % 8
                case 3:  # jnz
                    if self.regA != 0:
                        self.eip = op - 2
                case 4:  # bxc
                    self.regB = self.regB ^ self.regC
                case 5:  # out
                    output.append(self.combo(op) % 8)
                case 6:  # bdv
                    self.regB = self.regA // (2 ** self.combo(op))
                case 7:  # cdv
                    self.regC = self.regA // (2 ** self.combo(op))
            self.eip += 2

        return output

    def combo(self, n: int):
        match n:
            case 4:
                return self.regA
            case 5:
                return self.regB
            case 6:
                return self.regC
            case _:
                return n

    def copy(self):
        return Computer(self.regA, self.regB, self.regC, self.program.copy())


lines = get_input(2024, 17).splitlines()
a = int(lines[0].split(": ")[1])
b = int(lines[1].split(": ")[1])
c = int(lines[2].split(": ")[1])
program = list(map(int, lines[4].split(": ")[1].split(",")))
computer = Computer(a, b, c, program)


def part1():
    comp = computer.copy()
    out = comp.run()
    return ",".join(list(map(str, out)))


def finda(a_octal: list):
    for digit in range(8):
        comp = computer.copy()
        new_a = int("".join(map(str, a_octal)) + str(digit), 8)
        comp.regA = new_a
        out = comp.run()
        if out == computer.program:
            return a_octal + [digit]
        if out[::-1][: len(a_octal) + 1] == computer.program[::-1][: len(a_octal) + 1]:
            if (found := finda(a_octal + [digit])) is not None:
                return found
    return None


def part2():
    res = finda([])
    return int("".join(map(str, res)), 8)
