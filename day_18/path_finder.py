from day_18 import graph_builder
from copy import deepcopy


def GoAndAbsorbNode(graph, key):
    new_position = graph.pop(key)

    # remove all links to absorbed node
    for k in new_position.keys():
        del graph[k][key]

    old_position = graph.pop('@')
    added_cost = new_position.pop('@')

    # Update '@‘ at new position
    graph['@'] = new_position
    for k, v in old_position.items():
        if k not in graph['@']:
            graph['@'][k] = v + added_cost


    # Update all of '@' neighbors
    for k, v in graph['@'].items():
        graph[k]['@'] = v

    return added_cost


class PathFinder:
    def __init__(self, graph):
        self.cost = None
        self.graph = graph
        self.missing_keys = {key for key in graph.keys() if key.islower()}

    def FindShortestPath(self):
        def ExploreNode(key, cost=0, graph=self.graph, keys=self.missing_keys):
            if key.isupper() and key.lower() in keys:   # if node is a locked door
                return

            if key != '@':
                cost += GoAndAbsorbNode(graph, key)

            # remove key if it exists, because we've now found it
            keys.discard(key)

            if not keys:
                self.cost = cost if self.cost is None or cost < self.cost else self.cost
                return

            for neigh in graph['@'].keys():
                ExploreNode(neigh, cost, deepcopy(graph), keys.copy())

        ExploreNode('@')
        return self.cost


if __name__ == '__main__':
    graph_from_file = graph_builder.BuildGraphFromFile('input.txt')
    finder = PathFinder(graph_from_file)
    print(finder.FindShortestPath())
