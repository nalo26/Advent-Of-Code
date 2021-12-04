import sys

class Board:
    def __init__(self):
        self.grid = []
        self.rows = []
        self.cols = []
        self.coords = []
        
    def draw(self, value):
        for i, row in enumerate(self.grid):
            if value in row:
                r, c = i, row.index(value)
                self.rows.append(r)
                self.cols.append(c)
                self.coords.append((r, c))
                return self.checkVictory(value, r, c)
            
    def checkVictory(self, value, row_val, col_val):
        if self.rows.count(row_val) == 5 or self.cols.count(col_val) == 5:
            _sum = 0
            for y, row in enumerate(self.grid):
                for x, col in enumerate(row):
                    if (y, x) not in self.coords: _sum += col
            return _sum * value
        
        return None
        
    
file = open("input.txt")
lines = file.readlines()

draw = list(map(int, lines[0].split(",")))
boards = []

# parsing each board
for board_i in range(2, len(lines), 6): # step by step each board
    board = Board()
    for grid_line in lines[board_i:][:5]:
        # parsing each str row to int list
        board.grid.append(
            [int(grid_line[i:i+3]) for i in range(0, len(grid_line), 3)]
        )
    boards.append(board)
        
# making the draws
for d in draw:
    for board in boards:
        victory = board.draw(d)
        if victory is None: continue
        print(victory)
        sys.exit()