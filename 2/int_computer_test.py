import unittest
from int_computer import IntComputer


class TestIntComputer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.computer = IntComputer("mock")

    def test_reading(self):
        self.assertEqual([1, 0, 0, 0, 99], self.computer.parse_sequence("1,0,0,0,99"))

    def test_addition_flag(self):
        IntComputer.evaluate('1,0,0,0,99')

