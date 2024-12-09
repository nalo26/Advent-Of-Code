from tqdm import tqdm

from lib.input import get_input

diskmap = list(map(int, list(get_input(2024, 9).splitlines()[0])))


def find_first_diff_data(values, data):
    try:
        return next(idx for idx, value in enumerate(values) if value != data)
    except StopIteration:
        return None


def consecutives(values, index):
    return find_first_diff_data(values[index:], values[index]) or len(values) - index


class Disk:
    def __init__(self, diskmap: list[int]):
        self.data_length = 0
        self.memory = self.uncompress(diskmap)

    def uncompress(self, diskmap: list[int]) -> list[int]:
        memory = []
        id = 0
        for i, c in enumerate(diskmap):
            if i % 2 == 0:  # file
                memory.extend([id] * c)
                self.data_length += c
                id += 1
            else:  # free space
                memory.extend([None] * c)
        return memory

    def fragment(self):
        while (pt_null := self.memory.index(None)) < self.data_length:
            pt_data = len(self.memory) - find_first_diff_data(reversed(self.memory), None) - 1
            self.memory[pt_null] = self.memory[pt_data]
            self.memory[pt_data] = None

    def fragment_block(self):
        for val in tqdm(range(self.memory[-1], -1, -1)):
            pt_data = self.memory.index(val)
            data_size = consecutives(self.memory, pt_data)
            pt_null, null_size = 0, 0
            try:
                while True:  # search for big enough free space
                    pt_null = self.memory.index(None, pt_null + null_size)
                    if pt_null > pt_data:
                        raise ValueError
                    null_size = consecutives(self.memory, pt_null)
                    if null_size >= data_size:
                        break
            except ValueError:  # not enough free space at better place
                continue
            self.memory[pt_null : pt_null + data_size] = [val] * data_size
            self.memory[pt_data : pt_data + data_size] = [None] * data_size

    def checksum(self):
        return sum(i * c for i, c in enumerate(self.memory) if c is not None)


def part1():
    disk = Disk(diskmap)
    disk.fragment()
    return disk.checksum()


def part2():
    disk = Disk(diskmap)
    disk.fragment_block()
    return disk.checksum()
