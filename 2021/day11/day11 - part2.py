file = open("input.txt")

grid = []
neighbors = [(+1, 0), (-1, 0), (0, +1), (0, -1), (+1, +1), (-1, -1), (+1, -1), (-1, +1)]
flashes_count = 0

class Octopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.has_flashed = False
        
    def increase(self):
        global flashes_count
        if self.has_flashed: return
        
        self.energy += 1
        if self.energy > 9:
            self.energy = 0
            self.has_flashed = True
            flashes_count += 1
        
            for x, y in neighbors:
                n_x = self.x + x
                n_y = self.y + y
                if n_x < 0 or n_x > len(grid[self.y])-1 or n_y < 0 or n_y > len(grid)-1: continue
                grid[n_y][n_x].increase()
    
    def __repr__(self):
        return str(self.energy)


def pretty_print(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print()
    print()
        

for y, line in enumerate(file.readlines()):
    # grid.append(list(map(int, line.replace("\n", ""))))
    octopuses = []
    for x, o in enumerate(line.replace("\n", "")):
        octopuses.append(Octopus(x, y, int(o)))
    grid.append(octopuses)

step = 0
while True:
    step += 1
    for line in grid:
        for octo in line:
            octo.increase()
    
    flash_sum = 0
    for line in grid:
        for octo in line:
            flash_sum += octo.energy
            octo.has_flashed = False
    
    if flash_sum == 0:
        break
    
print(step)