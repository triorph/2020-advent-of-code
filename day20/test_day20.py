import unittest
from copy import deepcopy
from .day20 import TileMatcherDay20, Tile


class TestTile(unittest.TestCase):
    def setUp(self):
        self._tile = Tile(
            [
                "Tile 2311:",
                "..##.#..#.",
                "##..#.....",
                "#...##..#.",
                "####.#...#",
                "##.##.###.",
                "##...#.###",
                ".#.#.#..##",
                "..#....#..",
                "###...#.#.",
                "..###..###",
            ]
        )
        self._original_tile = [
            "..##.#..#.",
            "##..#.....",
            "#...##..#.",
            "####.#...#",
            "##.##.###.",
            "##...#.###",
            ".#.#.#..##",
            "..#....#..",
            "###...#.#.",
            "..###..###",
        ]
        self._original_edges = deepcopy(self._tile.edges)

    def test_rotate_left(self):
        self._tile.rotate_270()
        self.assertEqual(self._tile.edges["w"], ".#..#.##..")
        self.assertEqual(self._tile.edges["s"], ".#####..#.")
        self.assertEqual(self._tile.edges["e"], "###..###..")
        self.assertEqual(self._tile.edges["n"], "...#.##..#")
        self.assertEqual(
            self._tile.tile,
            [
                "...#.##..#",
                "#.#.###.##",
                "....##.#.#",
                "....#...#.",
                "#.##.##...",
                ".##.#....#",
                "#..##.#..#",
                "#..#...###",
                ".#.####.#.",
                ".#####..#.",
            ],
        )

    def test_180(self):
        self._tile.rotate_180()
        self.assertEqual(self._tile.edges["n"], self._original_edges["s"][::-1])
        self.assertEqual(self._tile.edges["s"], self._original_edges["n"][::-1])
        self.assertEqual(self._tile.edges["w"], self._original_edges["e"][::-1])
        self.assertEqual(self._tile.edges["e"], self._original_edges["w"][::-1])

    def test_rotate_right(self):
        self._tile.rotate_90()
        self.assertEqual(self._tile.edges["w"], "..###..###")
        self.assertEqual(self._tile.edges["s"], "#..##.#...")
        self.assertEqual(self._tile.edges["e"], "..##.#..#.")
        self.assertEqual(self._tile.edges["n"], ".#..#####.")
        self.assertEqual(
            self._tile.tile,
            [
                ".#..#####.",
                ".#.####.#.",
                "###...#..#",
                "#..#.##..#",
                "#....#.##.",
                "...##.##.#",
                ".#...#....",
                "#.#.##....",
                "##.###.#.#",
                "#..##.#...",
            ],
        )


class TestTileMatcher(unittest.TestCase):
    def test_daya(self):
        d20 = TileMatcherDay20("example_data.txt")
        self.assertEqual(d20.day_a(), 20899048083289)

    def test_built_image(self):
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
        print(len(d20._image), len(d20._image[0]))
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
        print(len(expected_image), len(expected_image[1]))
        self.maxDiff = None
        for i in range(len(expected_image)):
            self.assertEqual("".join(d20._image[i]), expected_image[i], i)
        self.assertEqual(["".join(image) for image in d20._image], expected_image)

    def test_day_b_count(self):
        d20 = TileMatcherDay20("example_data.txt")
        self.assertEqual(d20.day_b(), 273)
