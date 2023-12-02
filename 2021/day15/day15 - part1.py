file = open("input.txt")

maze = []
for line in file.readlines():
    maze.append(list(map(int, line.replace("\n", ""))))


def minCost(maze, end_row, end_col):
    tc = [[0 for x in range(len(maze[0]))] for x in range(len(maze))]

    for i in range(1, end_row + 1):
        tc[i][0] = tc[i - 1][0] + maze[i][0]

    for j in range(1, end_col + 1):
        tc[0][j] = tc[0][j - 1] + maze[0][j]

    for i in range(1, end_row + 1):
        for j in range(1, end_col + 1):
            tc[i][j] = min(tc[i - 1][j], tc[i][j - 1]) + maze[i][j]

    return tc[end_row][end_col]


print(minCost(maze, len(maze) - 1, len(maze[-1]) - 1) - 1)
