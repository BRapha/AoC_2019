from day_18 import graph_builder


def FindShortestPath(graph):
    needed_keys = {key for key in graph.keys() if key.islower()}
    seen = set()
    cost = 0
    node = graph['@']

    while node:
        for key, weight in node.items():
            if not needed_keys:
                node = None
                break

            if key.isupper() and key.lower() in needed_keys:
                continue

            if key in seen:
                continue

            if key in needed_keys:
                needed_keys.remove(key)

            seen.add(key)
            node = graph[key]
            cost += weight
            break

    return cost


if __name__ == '__main__':
    graph = graph_builder.BuildGraphFromFile('input.txt')
    print(FindShortestPath(graph))
