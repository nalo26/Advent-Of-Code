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
        

for y, line in enumerate(file.readlines()):
    octopuses = []
    for x, o in enumerate(line.replace("\n", "")):
        octopuses.append(Octopus(x, y, int(o)))
    grid.append(octopuses)
    
for step in range(100):
    for line in grid:
        for octo in line:
            octo.increase()
            
    for line in grid:
        for octo in line:
            octo.has_flashed = False
    
print(flashes_count)