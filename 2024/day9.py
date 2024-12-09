from lib.input import get_input

diskmap = list(map(int, list(get_input(2024, 9).splitlines()[0])))


class Disk:
    def __init__(self, diskmap: list[int]):
        self.data_length = 0
        self.memory = self.uncompress(diskmap)

    def uncompress(self, diskmap: list[int]) -> list[int]:
        memory = []
        id = 1
        for i, c in enumerate(diskmap):
            if i % 2 == 0:  # file
                memory.extend([id] * c)
                self.data_length += c
                id += 1
            else:  # free space
                memory.extend([0] * c)
        return memory

    def fragment(self):
        while (pt_null := self.memory.index(0)) < self.data_length:
            pt_move = len(self.memory) - self._find_first_diff_data(reversed(self.memory), 0) - 1
            self.memory[pt_null] = self.memory[pt_move]
            self.memory[pt_move] = 0

    def fragment_block(self):
        max_val = max(self.memory)
        for val in range(max_val, 0, -1):
            pt_move = self.memory.index(val)
            data_size = self._consecutives(pt_move)
            pt_null, null_size = 0, 0
            try:
                while True:  # search for big enough free space
                    pt_null = self.memory.index(0, pt_null + null_size)
                    if pt_null > pt_move:
                        raise ValueError
                    null_size = self._consecutives(pt_null)
                    if null_size >= data_size:
                        break
            except ValueError:  # not enough free space at better place
                continue
            self.memory[pt_null : pt_null + data_size] = [val] * data_size
            self.memory[pt_move : pt_move + data_size] = [0] * data_size

    def _find_first_diff_data(self, values, data):
        try:
            return next(idx for idx, value in enumerate(values) if value != data)
        except StopIteration:
            return None

    def _consecutives(self, index):
        return self._find_first_diff_data(self.memory[index:], self.memory[index]) or len(self.memory) - index

    def checksum(self):
        return sum(i * (c - 1) for i, c in enumerate(self.memory) if c != 0)

    def __str__(self):
        def compute(data):
            return str(data - 1) if data != 0 else "."

        return "".join(map(compute, self.memory))


def part1():
    disk = Disk(diskmap)
    disk.fragment()
    return disk.checksum()


def part2():
    disk = Disk(diskmap)
    disk.fragment_block()
    return disk.checksum()
