import unittest
from .day14 import MemoryMakerDay14


class TestDay14(unittest.TestCase):
    def setUp(self):
        self._d14 = MemoryMakerDay14("input_data.txt")

    def test_mask_a(self):
        self.assertEqual(self._d14._apply_mask_a(100, "XXXXXXX1XXXX"), 116)

    def test_mask_b(self):
        indices = self._d14._apply_mask_b(42, "X1001X")
        self.assertEqual(len(indices), 4)
        for index in indices:
            self.assertIn(index, [26, 27, 58, 59])

    def test_mask_b2(self):
        indices = self._d14._apply_mask_b(26, "1X0XX")
        self.assertEqual(len(indices), 8)
        for index in indices:
            self.assertIn(index, [16, 17, 18, 19, 24, 25, 26, 27])