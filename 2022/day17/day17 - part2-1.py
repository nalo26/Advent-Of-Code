from tqdm import tqdm


file = open("input.txt")
pattern = file.read().splitlines()[0]


class Rock:
    rocks = [
        [0, 1, 2, 3],
        [1, 4, 5, 6, 9],
        [2, 6, 8, 9, 10],
        [0, 4, 8, 12],
        [0, 1, 4, 5],
    ]

    def __init__(self, _type: int, x=2, y=0):
        self.x = x
        self.y = y
        self.type = Rock.rocks[_type]


class Chamber:
    def __init__(self) -> None:
        self.height = 0
        self.width = 7
        self.field = []
        self.current_rock = -1
        self.rock = None
        self.switch_rock()

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j not in self.rock.type:
                    continue
                if (
                    i + self.rock.y > self.height - 1
                    or j + self.rock.x > self.width - 1
                    or j + self.rock.x < 0
                    or self.field[i + self.rock.y][j + self.rock.x] > 0
                ):
                    intersection = True
                    break
        return intersection

    def go_down(self):
        self.rock.y += 1
        if self.intersects():
            self.rock.y -= 1
            h = self.height - self.field.count([0] * self.width)
            self.freeze()
            print((self.height - self.field.count([0] * self.width)) - h, end=",")
            self.switch_rock()
            return False
        return True

    def go_side(self, dx):
        old_x = self.rock.x
        self.rock.x += dx
        if self.intersects():
            self.rock.x = old_x

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.rock.type:
                    self.field[i + self.rock.y][j + self.rock.x] = 1

    def switch_rock(self):
        self.current_rock = (self.current_rock + 1) % len(Rock.rocks)
        self.rock = Rock(self.current_rock)

        empty_lines = self.field.count([0] * self.width)
        # empty_space + height_rock - empty_lines
        to_add = 3 + max(self.rock.type) // 4 + 1 - empty_lines
        if to_add < 0:
            self.rock.y = abs(to_add)
            return

        for _ in range(to_add):
            self.field.insert(0, [0] * self.width)
            self.height += 1

        self.field = self.field[:1000]


chamber = Chamber()
pattern_index = -1
for turn in tqdm(range(100000)):
    while True:
        pattern_index += 1
        instruction = pattern[pattern_index % len(pattern)]
        chamber.go_side(1 if instruction == ">" else -1)
        if not chamber.go_down():
            break

# print(chamber.height - chamber.field.count([0] * chamber.width))
