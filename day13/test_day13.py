import unittest
from .day13 import Day13


class TestCRT(unittest.TestCase):
    def test_chinese_remainder_theorem(self):
        a = [2, 3, 2]
        n = [3, 5, 7]
        ret = Day13.calc_chinese_remainder(a, n)
        self.assertEqual(ret, 23)

    def test_other_example(self):
        a = [1, 4, 6]
        n = [3, 5, 7]
        self.assertEqual(Day13.calc_chinese_remainder(a, n), 34)

    def test_given_example(self):
        a = [0, 13 - 1, 59 - 4, 31 - 6, 19 - 7]
        n = [7, 13, 59, 31, 19]
        self.assertEqual(Day13.calc_chinese_remainder(a, n), 1068781)

    def test_calc_b(self):
        d13 = Day13("input_data.txt")
        d13._data = [(0, 7), (1, 13), (4, 59), (6, 31), (7, 19)]
        self.assertEqual(d13.get_calc_b(), 1068781)

    def test_calc_b_2(self):
        d13 = Day13("input_data.txt")
        d13._data = [(0, 17), (2, 13), (3, 19)]
        self.assertEqual(d13.get_calc_b(), 3417)

    def test_calc_b_3(self):
        d13 = Day13("input_data.txt")
        d13._data = [(0, 67), (1, 7), (2, 59), (3, 61)]
        self.assertEqual(d13.get_calc_b(), 754018)

    def test_calc_b_4(self):
        d13 = Day13("input_data.txt")
        d13._data = [(0, 67), (2, 7), (3, 59), (4, 61)]
        self.assertEqual(d13.get_calc_b(), 779210)

    def test_calc_b_5(self):
        d13 = Day13("input_data.txt")
        d13._data = [(0, 67), (1, 7), (3, 59), (4, 61)]
        self.assertEqual(d13.get_calc_b(), 1261476)

    def test_calc_b_6(self):
        d13 = Day13("input_data.txt")
        d13._data = [(0, 1789), (1, 37), (2, 47), (3, 1889)]
        self.assertEqual(d13.get_calc_b(), 1202161486)