from day_18 import graph_builder, path_finder
import unittest


class PathFinderTest(unittest.TestCase):
    def test_case_1(self):
        graph = graph_builder.BuildGraphFromFile('testcase1.txt')
        expected_dist = 8
        self.assertEqual(expected_dist, path_finder.FindShortestPath(graph))