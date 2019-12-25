from shared.parser import Parser
from collections import deque


def ReadFileToGrid(filename):
    return [list(line.rstrip()) for line in Parser.ReadLines(filename)]


def FindAllNodes(grid):
    nodes = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] not in ('.', '#'):
                nodes.append((i, j))

    return nodes


def BuildGraph(grid, nodes):
    graph = dict()
    while nodes:
        nx, ny = nodes.pop()
        node = grid[nx][ny]
        graph[node] = dict()
        visited = {(nx, ny)}
        queue = deque([(nx, ny, 0)])
        while queue:
            x, y, dist = queue.popleft()
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                pi, pj = x+i, y+j
                if pi < len(grid) and pj < len(grid[pi]) and (pi, pj) not in visited:
                    visited.add((pi, pj))
                    content = grid[pi][pj]
                    if content == '.':
                        queue.append((pi, pj, dist+1))
                    elif content != '#':
                        graph[node][content] = dist+1

    return graph


def GenerateGraph(filename):
    grid = ReadFileToGrid(filename)
    nodes = FindAllNodes(grid)
    return BuildGraph(grid, nodes)


if __name__ == '__main__':
    pass