import unittest
from day_2 import int_computer


class TestIntComputer(unittest.TestCase):
    def test_reading(self):
        self.assertEqual([1, 0, 0, 0, 99], int_computer.parse_sequence("1,0,0,0,99"))

    def test_addition_flag(self):
        expected = [2, 0, 0, 0, 99]
        outcome = [1, 0, 0, 0, 99]
        int_computer.transform(outcome)
        self.assertEqual(expected, outcome)

    def test_multiplication_flag(self):
        expected = [2, 3, 0, 6, 99]
        outcome = [2, 3, 0, 3, 99]
        int_computer.transform(outcome)
        self.assertEqual(expected, outcome)

    def test_break_flag(self):
        expected = [99, 3, 0, 3, 99]
        outcome = [99, 3, 0, 3, 99]
        int_computer.transform(outcome)
        self.assertEqual(expected, outcome)

    def test_multi_sequence(self):
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        outcome = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        int_computer.transform(outcome)
        self.assertEqual(expected, outcome)