import unittest
from day_3 import distance_calculator


class TestDistanceCalculator(unittest.TestCase):
    def test_case_1(self):
        first = "R8,U5,L5,D3"
        second = "U7,R6,D4,L4"
        expected_dist = 6
        manhattan_dist = distance_calculator.GetClosestIntersection(first, second)
        self.assertEqual(expected_dist, manhattan_dist)