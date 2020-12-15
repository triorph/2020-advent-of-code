import unittest
from .day5 import BinaryPlaneDecoder


class TestDay5BinaryPlaneDecoder(unittest.TestCase):
    def _assert_decoded_equal(self, line, expected):
        self.assertEqual(BinaryPlaneDecoder.decode_line(line), expected)

    def test_basic_examples(self):
        self._assert_decoded_equal("FBFBBFFRLR", (44, 5, 357))
        self._assert_decoded_equal("BFFFBBFRRR", (70, 7, 567))
        self._assert_decoded_equal("FFFBBBFRRR", (14, 7, 119))
        self._assert_decoded_equal("BBFFBBFRLL", (102, 4, 820))
