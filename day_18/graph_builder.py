from shared.parser import Parser
from collections import deque


def ReadFileToGrid(filename):
    return [list(line.rstrip()) for line in Parser.ReadLines(filename)]


def IterNodesInGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col]
            if char not in ('.', '#'):
                yield row, col, char


def BuildGraph(grid):
    graph = {}

    def FindNeighbourNodes(r, c):
        visited = {(r, c)}
        queue = deque([(r, c, 0)])
        while queue:
            _row, _col, _dist = queue.popleft()
            for row_i, col_j in ((_row+1, _col), (_row-1, _col), (_row, _col+1), (_row, _col-1)):
                if row_i < len(grid) and col_j < len(grid[row_i]) and (row_i, col_j) not in visited:
                    visited.add((row_i, col_j))
                    char_i = grid[row_i][col_j]
                    if char_i == '.':
                        queue.append((row_i, col_j, _dist + 1))
                    elif char_i != '#':
                        graph[grid[r][c]][char_i] = _dist + 1

    for row, col, char in IterNodesInGrid(grid):
        graph[char] = dict()
        FindNeighbourNodes(row, col)

    return graph


def BuildGraphFromFile(filename):
    grid = ReadFileToGrid(filename)
    return BuildGraph(grid)
