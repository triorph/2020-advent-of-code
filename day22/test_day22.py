import unittest
from .day22 import CardGameDay22


class TestCardGameDay22(unittest.TestCase):
    def test_basic_output(self):
        d22 = CardGameDay22("example_data.txt")
        self.assertEqual(d22._p1_cards[-1], [9, 2, 6, 3, 1])
        self.assertEqual(d22._p2_cards[-1], [5, 8, 4, 7, 10])
        d22._do_one_round_a()
        self.assertEqual(d22._p1_cards[-1], [2, 6, 3, 1, 9, 5])
        self.assertEqual(d22._p2_cards[-1], [8, 4, 7, 10])
        d22._do_one_round_a()
        self.assertEqual(d22._p1_cards[-1], [6, 3, 1, 9, 5])
        self.assertEqual(d22._p2_cards[-1], [4, 7, 10, 8, 2])
        d22._do_one_round_a()
        self.assertEqual(d22._p1_cards[-1], [3, 1, 9, 5, 6, 4])
        self.assertEqual(d22._p2_cards[-1], [7, 10, 8, 2])
        d22._do_one_round_a()
        self.assertEqual(d22._p1_cards[-1], [1, 9, 5, 6, 4])
        self.assertEqual(d22._p2_cards[-1], [10, 8, 2, 7, 3])
        d22.do_all_rounds_a()
        self.assertEqual(d22._p1_cards[-1], [])
        self.assertEqual(d22._p2_cards[-1], [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(d22.day_a(), 306)