class Mapper:
    def __init__(self, filename):
        self._map_data = []
        self._width = 0
        self._height = 0
        self.build_map(filename)

    def build_map(self, filename):
        with open(filename, "r") as f:
            self._map_data = f.readlines()
        self._height = len(self._map_data)
        self._width = len(self._map_data[0].strip())

    def get_coordinate(self, x, y):
        x = x % self._width
        try:
            return self._map_data[y][x]
        except IndexError:
            print("index error at", x, y, self._height)

    def count_trees(self, start_pos, delta):
        tree_count = 0
        pos = (start_pos[0], start_pos[1])
        while pos[1] < self._height:
            tree_count += self.get_coordinate(*pos) == "#"
            pos = (pos[0] + delta[0], pos[1] + delta[1])
        print(f"Counted {tree_count} trees")
        return tree_count

    def multiply_tree_counts(self, start_pos, deltas):
        multiply = 1
        for delta in deltas:
            multiply *= self.count_trees(start_pos, delta)
        return multiply

    def day_a(self):
        return self.multiply_tree_counts((0, 0), [(3, 1)])

    def day_b(self):
        deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return self.multiply_tree_counts((0, 0), deltas)


if __name__ == "__main__":
    d3 = Mapper("input_data.txt")
    print("d3a:", d3.day_a())
    print("d3b:", d3.day_b())