import numpy
import itertools


class Conway3DSimulatorDay17a:
    def __init__(self, filename):
        self._start_data = numpy.zeros([1, 8, 8])
        self._old_data = numpy.zeros([1, 8, 8])
        self._new_data = numpy.zeros([1, 8, 8])
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        self._start_data = numpy.zeros([1, len(lines), len(lines[0].strip())])
        for i, line in enumerate(lines):
            for j, ch in enumerate(line.strip()):
                if ch == "#":
                    self._start_data[0, i, j] = 1
        self._old_data = self._start_data
        self._new_data = self._old_data

    def _validate_pos(self, x, y, z):
        return (
            x >= 0
            and x < self._old_data.shape[2]
            and y >= 0
            and y < self._old_data.shape[1]
            and z >= 0
            and z < self._old_data.shape[0]
        )

    def _get_value_at(self, x, y, z):
        if self._validate_pos(x, y, z):
            return self._old_data[z, y, x]
        else:
            return 0

    def _count_neighbours(self, x, y, z):
        count = 0
        for z_mod, y_mod, x_mod in itertools.product([-1, 0, 1], repeat=3):
            if z_mod == y_mod == x_mod == 0:
                continue
            count += self._get_value_at(x + x_mod, y + y_mod, z + z_mod)
        return count

    def _pos_should_be_high(self, x, y, z):
        current_val = self._get_value_at(x, y, z)
        num_neighbours = self._count_neighbours(x, y, z)
        return (
            current_val
            and num_neighbours in [2, 3]
            or not current_val
            and num_neighbours == 3
        )

    def iterate_once(self):
        new_shape = list(self._old_data.shape)
        for i in range(3):
            new_shape[i] = new_shape[i] + 2

        self._new_data = numpy.zeros(new_shape)
        for z, y, x in itertools.product(
            range(new_shape[0]), range(new_shape[1]), range(new_shape[2])
        ):
            x_trans, y_trans, z_trans = x - 1, y - 1, z - 1
            if self._pos_should_be_high(x_trans, y_trans, z_trans):
                self._new_data[z, y, x] = 1
        self._old_data = self._new_data

    def day_a(self):
        for _ in range(6):
            self.iterate_once()

        return self._new_data.sum()


if __name__ == "__main__":
    d17 = Conway3DSimulatorDay17("input_data.txt")
    print("D17a:", d17.day_a())