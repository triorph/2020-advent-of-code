import unittest
from .day15 import MemoryGameDay15


class TestDay15(unittest.TestCase):
    def setUp(self):
        self._d15 = MemoryGameDay15("input_data.txt")

    def test_132(self):
        self._d15._pattern = [1, 3, 2]
        self.assertEqual(self._d15.day_a(), 1)
        self.assertEqual(self._d15.day_b(), 2578)

    def test_213(self):
        self._d15._pattern = [2, 1, 3]
        self.assertEqual(self._d15.day_a(), 10)
        # self.assertEqual(self._d15.day_b(), 3544142)

    def test_123(self):
        self._d15._pattern = [1, 2, 3]
        self.assertEqual(self._d15.day_a(), 27)
        # self.assertEqual(self._d15.day_b(), 261214)

    def test_231(self):
        self._d15._pattern = [2, 3, 1]
        self.assertEqual(self._d15.day_a(), 78)
        # self.assertEqual(self._d15.day_b(), 6895259)

    def test_321(self):
        self._d15._pattern = [3, 2, 1]
        self.assertEqual(self._d15.day_a(), 438)
        # self.assertEqual(self._d15.day_b(), 18)

    def test_312(self):
        self._d15._pattern = [3, 1, 2]
        self.assertEqual(self._d15.day_a(), 1836)
        # self.assertEqual(self._d15.day_b(), 372)

    def test_036(self):
        self._d15._pattern = [0, 3, 6]
        # self.assertEqual(self._d15.day_b(), 175594)