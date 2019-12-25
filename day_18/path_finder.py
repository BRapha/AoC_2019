from shared.parser import Parser
from collections import deque


def ReadFileToGrid(filename):
    return [list(line.rstrip()) for line in Parser.ReadLines(filename)]


def FindAllNodeCoords(grid):
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] not in ('.', '#'):
                coords.append((i, j))

    return coords


def BuildGraph(grid, node_coords):
    graph = {grid[x][y]: dict() for (x, y) in node_coords}

    def AddNeigborsToGraph(nx, ny):
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

    while node_coords:
        x, y = node_coords.pop()
        AddNeigborsToGraph(x, y)

    return graph


def GenerateGraph(filename):
    grid = ReadFileToGrid(filename)
    node_coords = FindAllNodeCoords(grid)
    return BuildGraph(grid, node_coords)


def FindShortestPath(graph):
    start = graph.pop('@')



if __name__ == '__main__':
    pass