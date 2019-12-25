from shared.parser import Parser
from collections import deque


def ReadFileToGrid(filename):
    return [list(line.rstrip()) for line in Parser.ReadLines(filename)]


def BuildGraph(grid):
    graph = {}

    def IterNodesInGrid():
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                c = grid[x][y]
                if c not in ('.', '#'):
                    yield x, y, c

    def FindNeighbourNodes(nx, ny):
        visited = {(nx, ny)}
        queue = deque([(nx, ny, 0)])
        while queue:
            x, y, dist = queue.popleft()
            for pi, pj in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if pi < len(grid) and pj < len(grid[pi]) and (pi, pj) not in visited:
                    visited.add((pi, pj))
                    char = grid[pi][pj]
                    if char == '.':
                        queue.append((pi, pj, dist + 1))
                    elif char != '#':
                        graph[grid[nx][ny]][char] = dist + 1

    for x, y, c in IterNodesInGrid():
        graph[c] = dict()
        FindNeighbourNodes(x, y)

    return graph


def GenerateGraph(filename):
    grid = ReadFileToGrid(filename)
    return BuildGraph(grid)


def FindShortestPath(graph):
    start = graph.pop('@')



if __name__ == '__main__':
    pass