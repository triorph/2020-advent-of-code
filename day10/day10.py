import numpy


class JoltChain:
    def __init__(self, filename, jolt_size):
        self._jolt_size = jolt_size
        self._data = None
        self._chains = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        self._data = numpy.array([int(line) for line in lines])

    def _day_a(self):
        self._data = numpy.array(sorted(self._data))
        diffs = self._data[1:] - self._data[:-1]
        print(diffs)
        return (diffs == 1).sum() + 1, (diffs == 3).sum() + 1

    def day_a(self):
        diff_1, diff_3 = self._day_a()
        return diff_1, diff_3, diff_1 * diff_3

    def build_chains_to_end(self, chain, data_group):
        last_val = chain[-1]
        data = numpy.array(data_group)
        bigger = data[data > last_val]
        within = bigger[bigger <= last_val + self._jolt_size]
        chains = []
        if len(within) >= 1:
            for value in within:
                new_chain = chain[:]
                new_chain.extend([value])
                chains.extend(self.build_chains_to_end(new_chain, data_group))
        else:
            chains = [chain]
        return chains

    def day_b(self):
        data = [0]
        data.extend(self._data)
        self._data = sorted(data)
        self.data_groups = []
        data_group = [0]
        for i in range(1, len(self._data)):
            if self._data[i] - self._data[i - 1] == 3:
                data_group.append(self._data[i])
                self.data_groups.append(data_group)
                data_group = [self._data[i]]
            else:
                data_group.append(self._data[i])
        self.data_groups.append(data_group)

        print("data_groups are", self.data_groups)
        ret = []
        for data_group in self.data_groups:
            chains = self.build_chains_to_end([data_group[0]], data_group)
            print("paths through", data_group, chains)
            ret.append(len(chains))

        return numpy.product(ret), ret


if __name__ == "__main__":
    d10 = JoltChain("input_data.txt", 3)
    print("d10a:", d10.day_a())
    print("d10b:", d10.day_b())
