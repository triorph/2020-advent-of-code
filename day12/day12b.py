class Day12ShipNavigatorB:
    def __init__(self, filename):
        self._direction = "E"
        self._pos = (0, 0)
        self._waypoint = (10, 1)
        self._instructions = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            self._instructions = f.readlines()

    def _rotate_right(self, amount):
        amount = int(amount)
        while amount > 0:
            amount -= 90
            self._rotate_right_once()

    def _rotate_right_once(self):
        self._waypoint = [self._waypoint[1], -self._waypoint[0]]

    def _rotate_left(self, amount):
        amount = int(amount)
        while amount > 0:
            amount -= 90
            self._rotate_left_once()

    def _rotate_left_once(self):
        self._waypoint = [-self._waypoint[1], self._waypoint[0]]

    def _go_east(self, amount):
        amount = int(amount)
        self._waypoint = (self._waypoint[0] + amount, self._waypoint[1])

    def _go_west(self, amount):
        amount = int(amount)
        self._waypoint = (self._waypoint[0] - amount, self._waypoint[1])

    def _go_north(self, amount):
        amount = int(amount)
        self._waypoint = (self._waypoint[0], self._waypoint[1] + amount)

    def _go_south(self, amount):
        amount = int(amount)
        self._waypoint = (self._waypoint[0], self._waypoint[1] - amount)

    def _go_forward(self, amount):
        amount = int(amount)
        self._pos = (
            self._pos[0] + self._waypoint[0] * amount,
            self._pos[1] + self._waypoint[1] * amount,
        )

    def process_line(self, line):
        command = line[0]
        amount = line[1:]
        func = {
            "F": self._go_forward,
            "R": self._rotate_right,
            "L": self._rotate_left,
            "N": self._go_north,
            "S": self._go_south,
            "E": self._go_east,
            "W": self._go_west,
        }
        func[command](amount)

    def _get_manhattan_distance(self):
        return abs(self._pos[0]) + abs(self._pos[1])

    def follow_movements_a(self):
        self._pos = [0, 0]
        self._direction = "E"
        for line in self._instructions:
            self.process_line(line)
        return self._get_manhattan_distance()


if __name__ == "__main__":
    d12 = Day12ShipNavigatorB("input_data.txt")
    print("D12b:", d12.follow_movements_a())