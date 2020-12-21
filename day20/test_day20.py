import unittest
from .day20 import TileMatcherDay20


class TestTileMatcher(unittest.TestCase):
    def test_daya(self):
        d20 = TileMatcherDay20("example_data.txt")
        self.assertEqual(d20.day_a(), 20899048083289)

    def test_dayb(self):
        d20 = TileMatcherDay20("example_data.txt")
        d20.match_edges()
        d20.layout_tiles()
        d20.build_image()
        d20._flip_image_vertically()
        print("top right tile:", d20._ordered_tiles[0][-1].tile_number)
        print("bottom left tile:", d20._ordered_tiles[-1][0].tile_number)
        print("bottom right tile:", d20._ordered_tiles[-1][-1].tile_number)
        expected_tile_order = [
            [2971, 1489, 1171],
            [2729, 1427, 2473],
            [1951, 2311, 3079],
        ]
        self.assertEqual(
            [
                [tile.tile_number for tile in ordered_row]
                for ordered_row in d20._ordered_tiles
            ],
            expected_tile_order,
        )
        # d20._rotate_image_90()
        # d20._rotate_image_90()
        # d20._rotate_image_90()
        # d20._rotate_image_90()
        expected_image = [
            ".#.#..#.##...#.##..#####",
            "###....#.#....#..#......",
            "##.##.###.#.#..######...",
            "###.#####...#.#####.#..#",
            "##.#....#.##.####...#.##",
            "...########.#....#####.#",
            "....#..#...##..#.#.###..",
            ".####...#..#.....#......",
            "#..#.##..#..###.#.##....",
            "#.####..#.####.#.#.###..",
            "###.#.#...#.######.#..##",
            "#.####....##..########.#",
            "##..##.#...#...#.#.#.#..",
            "...#..#..#.#.##..###.###",
            ".#.#....#.##.#...###.##.",
            "###.#...#..#.##.######..",
            ".#.#.###.##.##.#..#.##..",
            ".####.###.#...###.#..#.#",
            "..#.#..#..#.#.#.####.###",
            "#..####...#.#.#.###.###.",
            "#####..#####...###....##",
            "#.##..#..#...#..####...#",
            ".#.###..##..##..####.##.",
            "...###...##...#...#..###",
        ]
        self.maxDiff = None
        for i in range(len(expected_image)):
            self.assertEqual("".join(d20._image[i]), expected_image[i], i)
        self.assertEqual(["".join(image) for image in d20._image], expected_image)
        self.assertEqual(d20.day_b(), 273)
