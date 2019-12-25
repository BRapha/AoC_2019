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

    def ExploreNeigbors(nx, ny):
        char = grid[nx][ny]
        visited = {(nx, ny)}
        queue = deque([(nx, ny, 0)])
        while queue:
            x, y, dist = queue.popleft()
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                pi, pj = x + i, y + j
                if pi < len(grid) and pj < len(grid[pi]) and (pi, pj) not in visited:
                    visited.add((pi, pj))
                    content = grid[pi][pj]
                    if content == '.':
                        queue.append((pi, pj, dist + 1))
                    elif content != '#':
                        graph[char][content] = dist + 1

    while node_coords:
        x, y = node_coords.pop()
        ExploreNeigbors(x, y)

    return graph


def GenerateGraph(filename):
    grid = ReadFileToGrid(filename)
    node_coords = FindAllNodeCoords(grid)
    return BuildGraph(grid, node_coords)


def FindShortestPath(graph):
    start = graph.pop('@')



if __name__ == '__main__':
    pass