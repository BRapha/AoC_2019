from day_18 import graph_builder, path_finder
import unittest


class PathFinderTest(unittest.TestCase):
    def test_go_and_absorb(self):
        graph = graph_builder.BuildGraphFromFile('testcase1.txt')
        expected = graph_builder.BuildGraph([['#', 'b', '.', 'A', '.', '.', '.', '@', '#']])
        path_finder.GoAndAbsorbNode(graph, 'a')
        self.assertEqual(expected, graph)

    def test_case_1(self):
        graph = graph_builder.BuildGraphFromFile('testcase1.txt')
        expected_dist = 8
        finder = path_finder.PathFinder(graph)
        self.assertEqual(expected_dist, finder.FindShortestPath())

    def test_case_2(self):
        graph = graph_builder.BuildGraphFromFile('testcase2.txt')
        expected_dist = 86
        finder = path_finder.PathFinder(graph)
        self.assertEqual(expected_dist, finder.FindShortestPath())

    def test_case_3(self):
        graph = graph_builder.BuildGraphFromFile('testcase3.txt')
        expected_dist = 132
        finder = path_finder.PathFinder(graph)
        self.assertEqual(expected_dist, finder.FindShortestPath())

    def test_case_4(self):
        graph = graph_builder.BuildGraphFromFile('testcase4.txt')
        expected_dist = 136
        finder = path_finder.PathFinder(graph)
        self.assertEqual(expected_dist, finder.FindShortestPath())

    def test_case_5(self):
        graph = graph_builder.BuildGraphFromFile('testcase5.txt')
        expected_dist = 81
        finder = path_finder.PathFinder(graph)
        self.assertEqual(expected_dist, finder.FindShortestPath())