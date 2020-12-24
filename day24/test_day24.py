import unittest
from .day24 import TileFollower


class TestDay24(unittest.TestCase):
    def test_day_b(self):
        d24 = TileFollower("example_data.txt")
        tr = d24._get_tile_results()
        expected_black = {0: 10, 1: 15, 2: 12, 3: 25}
        for i in range(5):
            if (i + 1) in expected_black:
                self.assertEqual(expected_black[i], d24._count_black_tiles(tr))
            tr = d24._next_iteration(tr)