from copy import deepcopy


class TileFollower:
    DIR_E = (2.0, 0)
    DIR_W = (-2.0, 0)
    DIR_NE = (1.0, 1.0)
    DIR_NW = (-1.0, 1.0)
    DIR_SE = (1.0, -1.0)
    DIR_SW = (-1.0, -1.0)
    ALL_DIRECTIONS = [DIR_E, DIR_W, DIR_NE, DIR_NW, DIR_SE, DIR_SW]
    ALL_DIRECTIONS_DICT = {
        "e": DIR_E,
        "w": DIR_W,
        "ne": DIR_NE,
        "nw": DIR_NW,
        "se": DIR_SE,
        "sw": DIR_SW,
    }

    def __init__(self, filename):
        self._data = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            self._data = f.readlines()

    def _find_tile_result(self, tile_string):
        position = (0.0, 0.0)
        while len(tile_string) > 0:
            direction, tile_string = self._get_next_direction(tile_string)
            position = (
                position[0] + direction[0],
                position[1] + direction[1],
            )
        return position

    def _get_next_direction(self, tile_string):
        if tile_string[0] in ["e", "w"]:
            return self._get_direction(tile_string[0]), tile_string[1:]
        else:
            return self._get_direction(tile_string[0:2]), tile_string[2:]

    def _get_direction(self, direction_string):
        return self.ALL_DIRECTIONS_DICT[direction_string]

    def _flip(self, value):
        return "black" if value == "white" else "white"

    def _get_tile_results(self):
        tile_results = {}
        for tile_string in self._data:
            tile_string = tile_string.strip()
            tile_result = self._find_tile_result(tile_string)
            tile_results.setdefault(tile_result, "white")
            tile_results[tile_result] = self._flip(tile_results[tile_result])
        return tile_results

    def _count_black_tiles(self, tile_results):
        return list(tile_results.values()).count("black")

    def day_a(self):
        tile_results = self._get_tile_results()
        return self._count_black_tiles(tile_results)

    def _count_black_neighbours(self, tile, old_results):
        count = 0
        for direction in self.ALL_DIRECTIONS:
            new_tile = tile[0] + direction[0], tile[1] + direction[1]
            if new_tile in old_results and old_results[new_tile] == "black":
                count += 1
        return count

    def _expand_tiles_to_consider(self, tile_results):
        original_keys = list(tile_results.keys())
        for tile in original_keys:
            if tile_results[tile] == "white":
                continue
            for direction in self.ALL_DIRECTIONS:
                new_tile = tile[0] + direction[0], tile[1] + direction[1]
                tile_results.setdefault(new_tile, "white")
        return tile_results

    def _next_iteration(self, old_results):
        old_results = self._expand_tiles_to_consider(old_results)
        new_results = deepcopy(old_results)
        for tile in new_results:
            neighbours = self._count_black_neighbours(tile, old_results)
            if old_results[tile] == "black" and (neighbours == 0 or neighbours > 2):
                new_results[tile] = self._flip(old_results[tile])
            elif old_results[tile] == "white" and neighbours == 2:
                new_results[tile] = self._flip(old_results[tile])
        return new_results

    def day_b(self):
        tile_results = self._get_tile_results()
        for i in range(100):
            print(i, ": count is:", self._count_black_tiles(tile_results))
            tile_results = self._next_iteration(tile_results)
        return self._count_black_tiles(tile_results)


if __name__ == "__main__":
    d24 = TileFollower("input_data.txt")
    print("d24a:", d24.day_a())
    print("d24b:", d24.day_b())
