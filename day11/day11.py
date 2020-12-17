from copy import deepcopy


class SeatOccupationAlgorithmDay11:
    def __init__(self, filename):
        self._map = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        self._map = [list(line) for line in lines]

    def _count_nearby_filled_seats_a(self, x, y):
        count = 0
        for _x in [x - 1, x, x + 1]:
            for _y in [y - 1, y, y + 1]:
                if _x == x and _y == y:
                    continue
                if not self._check_bounds(_x, _y):
                    continue
                try:
                    if self._map[_y][_x] == "#":
                        count += 1
                except IndexError:
                    breakpoint()
        return count

    def _check_seat_can_be_filled_a(self, x, y):
        return self._count_nearby_filled_seats_a(x, y) == 0

    def _check_seat_will_be_left_a(self, x, y):
        return self._count_nearby_filled_seats_a(x, y) >= 4

    def _check_position_needs_changing_a(self, x, y):
        if self._map[y][x] == "L":
            return self._check_seat_can_be_filled_a(x, y)
        elif self._map[y][x] == "#":
            return self._check_seat_will_be_left_a(x, y)
        else:
            return False

    def _toggle(self, seat):
        if seat == "#":
            return "L"
        else:
            return "#"

    def process_once_a(self):
        next = deepcopy(self._map)
        changes = 0
        for y in range(len(self._map)):
            for x in range(len(self._map[y])):
                if self._check_position_needs_changing_a(x, y):
                    changes += 1
                    next[y][x] = self._toggle(next[y][x])
        self._map = next
        print("changed:", changes)
        return changes > 0

    def _check_bounds(self, x, y):
        return y >= 0 and y < len(self._map) and x >= 0 and x < len(self._map[y])

    def _look_in_direction_for_seats(self, x, y, direction_x, direction_y):
        new_x = x + direction_x
        new_y = y + direction_y
        while self._check_bounds(new_x, new_y):
            place = self._map[new_y][new_x]
            if place == "#" or place == "L":
                return place
            new_x = new_x + direction_x
            new_y = new_y + direction_y
        return "."

    def _count_nearby_filled_seats_b(self, x, y):
        count = 0
        for direction_x in [-1, 0, 1]:
            for direction_y in [-1, 0, 1]:
                if direction_x == 0 and direction_y == 0:
                    continue
                seat = self._look_in_direction_for_seats(x, y, direction_x, direction_y)
                if seat == "#":
                    count += 1
        return count

    def _check_seat_can_be_filled_b(self, x, y):
        return self._count_nearby_filled_seats_b(x, y) == 0

    def _check_seat_will_be_left_b(self, x, y):
        return self._count_nearby_filled_seats_b(x, y) >= 5

    def _check_position_needs_changing_b(self, x, y):
        if self._map[y][x] == "L":
            return self._check_seat_can_be_filled_b(x, y)
        elif self._map[y][x] == "#":
            return self._check_seat_will_be_left_b(x, y)
        else:
            return False

    def process_once_b(self):
        next = deepcopy(self._map)
        changes = 0
        for y in range(len(self._map)):
            for x in range(len(self._map[y])):
                if self._check_position_needs_changing_b(x, y):
                    changes += 1
                    next[y][x] = self._toggle(next[y][x])
        self._map = next
        print("changed:", changes)
        return changes > 0

    def _sum_occupied(self):
        return sum(line.count("#") for line in self._map)

    def day_a(self):
        for i in range(1000):
            if not self.process_once_a():
                break
        return self._sum_occupied()

    def day_b(self):
        for i in range(1000):
            if not self.process_once_b():
                break
        return self._sum_occupied()


if __name__ == "__main__":
    d11 = SeatOccupationAlgorithmDay11("input_data.txt")
    print("d11a:", d11.day_a())
    d11 = SeatOccupationAlgorithmDay11("input_data.txt")
    print("d11b:", d11.day_b())