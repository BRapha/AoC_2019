from day_18 import path_finder
import unittest


class TestPathFinder(unittest.TestCase):

    def test_grid(self):
        expected_grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                         ['#', 'b', '.', 'A', '.', '@', '.', 'a', '#'],
                         ['#', '#', '#', '#', '#', '#', '#', '#', '#']]
        grid = path_finder.ReadFileToGrid("testcase1.txt")
        self.assertEqual(expected_grid, grid)

    def test_find_at(self):
        grid = path_finder.ReadFileToGrid("testcase1.txt")
        expected_coords = [(1, 1), (1, 3), (1, 5), (1, 7)]
        coords = path_finder.FindAllNodes(grid)
        self.assertEqual(expected_coords, coords)

    def test_graph(self):
        expected_graph = {"@": {"a": 2, "A": 2}, "a": {"@": 2}, "A": {"@": 2, "b": 2}, "b": {"A": 2}}
        graph = path_finder.GenerateGraph("testcase1.txt")
        self.assertEqual(expected_graph, graph)
