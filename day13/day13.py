import numpy


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

    @classmethod
    def calc_chinese_remainder(cls, a, n):
        sum = 0
        prod = numpy.product(n)
        for _a, _n in zip(a, n):
            p = int(prod / _n)
            sum += _a * cls.calc_modular_inverse(p, _n) * p
        return int(sum) % prod

    @classmethod
    def calc_modular_inverse(cls, a, b):
        x, y = cls.calc_extended_gcd(a, b)
        if (a * x) % b == 1:
            return x
        else:
            raise RuntimeError("No modular inverse for a mod b", a, b)

    @classmethod
    def calc_extended_gcd(cls, a, b):
        if b == 0:
            return (1, 0)
        else:
            q = int(a / b)
            r = a % b
            s, t = cls.calc_extended_gcd(b, r)
            return (t, s - q * t)

    def get_calc_b(self):
        """
        looking for values where minute - i % bus_id == 0 for every minute and bus_id
        can be solved using chinese remainder theorem

        this is equivalent to solving X in the chinese remainder theorem, where
        x = (bus_id - minute) % bus_id
        """
        a = []
        n = []
        data = sorted(self._data, reverse=True, key=lambda x: x[1])[0:9]
        for (
            minute,
            bus_id,
        ) in data:
            a.append((bus_id - int(minute)) % bus_id)
            n.append(int(bus_id))
        x = self.calc_chinese_remainder(a, n)
        self._validate_number(x, data)
        return x

    def _validate_number(self, x, data):
        """Complain if the number we generated gives us the wrong results"""
        incorrections = []
        for minute, bus_id in data:
            if (x + minute) % bus_id != 0:
                incorrections.append(
                    "x + {} % {} = {}".format(minute, bus_id, (x + minute) % bus_id)
                )
        print(incorrections)
        if len(incorrections) > 0:
            raise Exception("Incorrect number generated for this dataset")


if __name__ == "__main__":
    d13 = Day13("input_data.txt")
    print("d13a:", d13.get_calc_a())
    print("d13b: ", d13.get_calc_b())
