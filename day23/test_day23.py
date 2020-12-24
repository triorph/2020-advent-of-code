import unittest

from .day23 import WeirdCupGame


class TestWeirdCupGame(unittest.TestCase):
    STARTING_INPUT = "389125467"

    def test_day_a(self):
        d23 = WeirdCupGame(self.STARTING_INPUT)
        self.assertEqual(d23.day_a(), "67384529")

    def test_day_b(self):
        d23 = WeirdCupGame(self.STARTING_INPUT)
        self.assertEqual(d23.day_b(), 149245887792)