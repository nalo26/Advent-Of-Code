from ast import literal_eval

file = open("input.txt")
lines = file.readlines()

class Num:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leftmost = self
        self.rightmost = self
        self.left_val = None
        self.right_val = None

    def update_value(self):
        pass

    def __repr__(self):
        return str(self.value)

class Pair:
    def __init__(self, left, right):
        self.parent = None
        self.side = None
        self.left = left
        self.right = right
        self.leftmost = left.leftmost
        self.rightmost = right.rightmost
        self.set_left(left)
        self.set_right(right)

    def set_left(self, left):
        self.left = left
        self.left.parent = self
        self.left.side = 0
        self.leftmost = self.left.leftmost
        self.left.rightmost.right_val = self.right.leftmost

    def set_right(self, right):
        self.right = right
        self.right.parent = self
        self.right.side = 1
        self.rightmost = self.right.rightmost
        self.right.leftmost.left_val = self.left.rightmost

    def update_value(self):
        self.left.update_value()
        self.right.update_value()
        self.leftmost = self.left.leftmost
        self.rightmost = self.right.rightmost
        self.left.rightmost.right_val = self.right.leftmost
        self.right.leftmost.left_val = self.left.rightmost

    def __repr__(self):
        return f"[{self.left}, {self.right}]"


def convert(l):
    if isinstance(l, int): return Num(l)
    return Pair(convert(l[0]), convert(l[1]))

def explode(v, k, depth = 0):
    if isinstance(k, Num): return False
    if isinstance(k.left, Num) and isinstance(k.right, Num) and depth >= 4:
        if k.left.left_val: k.left.left_val.value += k.left.value
        if k.right.right_val: k.right.right_val.value += k.right.value
        if k.side == 0: k.parent.set_left(Num(0))
        else: k.parent.set_right(Num(0))
        v.update_value()
        return True
    return explode(v, k.left, depth+1) or explode(v, k.right, depth+1)

def split(v, k):
    if not isinstance(k, Num): return split(v, k.left) or split(v, k.right)
    if k.value < 10: return False

    if k.side == 0:
        k.parent.set_left(Pair(Num(k.value // 2), Num(-(-k.value // 2))))
    else:
        k.parent.set_right(Pair(Num(k.value // 2), Num(-(-k.value // 2))))
    v.update_value()
    return True

def reduce(l):
    while True:
        if explode(l, l): pass
        elif split(l, l): pass
        else: break

def magnitude(l):
    if isinstance(l, Num): return l.value
    return 3 * magnitude(l.left) + 2 * magnitude(l.right)


sum = None
for line in lines:
    number = convert(literal_eval(line.replace("\n", "")))
    if sum is None:
        sum = number
    else:
        sum = Pair(sum, number)
        reduce(sum)
    # print(sum)


print(magnitude(sum))