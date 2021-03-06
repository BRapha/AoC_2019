from day_18 import graph_builder
import unittest


class GraphBuilderTest(unittest.TestCase):

    def test_iter_nodes(self):
        grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', 'b', '.', 'A', '.', '@', '.', 'a', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#']]

        expected = [(1, 1, 'b'), (1, 3, 'A'), (1, 5, '@'), (1, 7, 'a')]
        result = [node for node in graph_builder.IterNodesInGrid(grid)]
        self.assertEqual(expected, result)

    def test_grid(self):
        expected_grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                         ['#', 'b', '.', 'A', '.', '@', '.', 'a', '#'],
                         ['#', '#', '#', '#', '#', '#', '#', '#', '#']]
        grid = graph_builder.ReadFileToGrid("testcase1.txt")
        self.assertEqual(expected_grid, grid)

    def test_graph(self):
        grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', 'b', '.', 'A', '.', '@', '.', 'a', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#']]
        expected_graph = {"@": {"a": 2, "A": 2}, "a": {"@": 2}, "A": {"@": 2, "b": 2}, "b": {"A": 2}}
        graph = graph_builder.BuildGraph(grid)
        self.assertEqual(expected_graph, graph)

    def test_graph_intersect(self):
        grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                ['#', 'b', '.', 'A', '.', '@', '.', 'a', '#'],
                ['#', '#', '#', '#', '.', '#', '#', '#', '#'],
                ['#', '#', '#', '#', 'B', '#', '#', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '#']]
        expected_graph = {"@": {"a": 2, "A": 2, "B": 3}, "a": {"@": 2}, "A": {"@": 2, "b": 2, "B": 3}, "b": {"A": 2},
                          "B": {"@": 3, "A": 3}}
        graph = graph_builder.BuildGraph(grid)
        self.assertEqual(expected_graph, graph)

    def test_graph_wo_borders(self):
        grid = [['#', 'b', '.', 'A', '.', '@', '.', 'a', '#']]
        expected_graph = {"@": {"a": 2, "A": 2}, "a": {"@": 2}, "A": {"@": 2, "b": 2}, "b": {"A": 2}}
        graph = graph_builder.BuildGraph(grid)
        self.assertEqual(expected_graph, graph)
