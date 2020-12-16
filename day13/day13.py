import tqdm


class Day13:
    def __init__(self, filename):
        self._data = []
        self._start_time = 0
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        self._start_time = int(lines[0])
        self._data = [
            (i, int(l)) for i, l in enumerate(lines[1].split(",")) if l != "x"
        ]

    def _time_to_wait(self, bus_id, from_time):
        return (0 - from_time) % bus_id

    def get_shortest_bus_id(self):
        shortest_time = self._start_time
        shortest_bus_id = 0
        for i, bus_id in self._data:
            if (
                bus_time := self._time_to_wait(bus_id, self._start_time)
            ) < shortest_time:
                shortest_bus_id = bus_id
                shortest_time = bus_time
        return shortest_bus_id, shortest_time

    def get_calc_a(self):
        ret = self.get_shortest_bus_id()
        return ret[0] * ret[1]

    def _multiply_values(self):
        mult = 1
        for i, bus_id in self._data:
            mult *= bus_id
        return mult

    def _get_max(self):
        max_val = 0
        max_i = 0
        for i, bus_id in self._data:
            if bus_id > max_val:
                max_val = bus_id
                max_i = i
        return i, max_val

    def get_calc_b(self):
        """
        looking for values where minute - i % bus_id == 0 for every minute and bus_id
        """
        max_ticks = self._multiply_values()
        jump_index, jump_size = self._get_max()
        for i in tqdm.tqdm(range(0, max_ticks, jump_size)):
            ticks = i + jump_index
            found = True
            for minute, bus_id in self._data:
                if (i + minute) % bus_id != 0:
                    found = False
                    break
            if found:
                return i


if __name__ == "__main__":
    d13 = Day13("input_data.txt")
    print("d13a:", d13.get_calc_a())
    print("d13b: ", d13.get_calc_b())
