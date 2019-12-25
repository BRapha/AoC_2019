from shared.parser import Parser
from collections import deque

def ReadFileToGrid(filename):
    return [list(line.rstrip()) for line in Parser.ReadLines(filename)]


def FindAt(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                return i, j


def ExploreGraph(grid, x, y):
    visited = {(x, y)}
    nodes = deque([(x, y)])
    graph = dict()
    while nodes:
        px, py = nodes.popleft()
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            pi, pj = px+i, py+j
            if pi < len(grid) and pj < len(grid[pi]) and (pi, pj) not in visited:
                visited.add((pi, pj))
                s = grid[pi][pj]
                if s != '#':
                    nodes.append((pi, pj))
                    print(s)

    return graph


def GenerateGraph(filename):
    grid = ReadFileToGrid(filename)
    x, y = FindAt(grid)
    return ExploreGraph(grid, x, y)


if __name__ == '__main__':
    pass