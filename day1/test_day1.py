#!/usr/bin/env python
"""Test the day1 functions."""
import os

import unittest
from day1.day1 import Day1


class Day1TestCase(unittest.TestCase):
    """
    Test the day 1 code.

    Test data is: 1, 10, 4, 8, 9.
    """

    def setUp(self):
        self._day1 = Day1(
            os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_data.txt")
        )

    def test_sums_2(self):
        for total, values in [
            [11, [1, 10]],
            [14, [10, 4]],
            [18, [10, 8]],
            [12, [4, 8]],
            [17, [8, 9]],
        ]:
            self.assertEqual(sorted(self._day1.get_values(total, 2)), sorted(values))

    def test_sums_3(self):
        for total, values in [
            [15, [1, 10, 4]],
            [22, [10, 4, 8]],
            [13, [1, 4, 8]],
            [14, [1, 4, 9]],
        ]:
            self.assertEqual(sorted(self._day1.get_values(total, 3)), sorted(values))
