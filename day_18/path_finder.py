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


def ExploreNeigbors(grid, graph, node):
    nx, ny, char = node
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


def BuildGraph(grid, nodes):
    graph = dict()
    while nodes:
        x, y = nodes.pop()
        char = grid[x][y]
        graph[char] = dict()
        ExploreNeigbors(grid, graph, (x, y, char))

    return graph


def GenerateGraph(filename):
    grid = ReadFileToGrid(filename)
    nodes = FindAllNodes(grid)
    return BuildGraph(grid, nodes)


def FindShortestPath(graph):
    start = graph.pop('@')



if __name__ == '__main__':
    pass