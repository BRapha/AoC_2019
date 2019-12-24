import unittest
from day_3 import distance_calculator


class TestDistanceCalculator(unittest.TestCase):
    def test_map(self):
        path = "U1,L2,D3,R4"
        expected = ((0, 1), (-1, 1), (-2, 1), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2))
        res = tuple(point for point in distance_calculator.YieldPoints(path))
        self.assertEqual(expected, res)

    def test_intersection(self):
        trail_map = {(0, 1), (-1, 1), (-2, 1), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2)}
        path = "L2"
        expected = 2
        res = distance_calculator.FindClosestIntersection(trail_map, path)
        self.assertEqual(expected, res)

    def test_case_1(self):
        first = "R8,U5,L5,D3"
        second = "U7,R6,D4,L4"
        expected_dist = 6
        manhattan_dist = distance_calculator.GetClosestIntersection(first, second)
        self.assertEqual(expected_dist, manhattan_dist)

    def test_case_2(self):
        first = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        second = "U62,R66,U55,R34,D71,R55,D58,R83"
        expected_dist = 159
        manhattan_dist = distance_calculator.GetClosestIntersection(first, second)
        self.assertEqual(expected_dist, manhattan_dist)

    def test_case_3(self):
        first = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        second = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        expected_dist = 135
        manhattan_dist = distance_calculator.GetClosestIntersection(first, second)
        self.assertEqual(expected_dist, manhattan_dist)