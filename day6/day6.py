class Day6:
    def __init__(self, filename):
        self.groups = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        group = []
        for line in lines:
            if line.strip() == "":
                self.groups.append(group)
                group = []
            else:
                group.append(line.strip())
        self.groups.append(group)

    def _calc_group_a(self):
        ret = []
        for group in self.groups:
            _val = set()
            for answers in group:
                _val.update(list(answers))
            ret.append(_val)
        return ret

    def sum_group_data_a(self):
        sum = 0
        for group in self._calc_group_a():
            sum += len(group)
        return sum

    def _calc_group_b(self):
        ret = []
        for group in self.groups:
            _val = None
            for answers in group:
                if _val is None:
                    _val = set(list(answers))
                else:
                    _val = _val.intersection(set(list(answers)))
            ret.append(_val)
        return ret

    def sum_group_data_b(self):
        sum = 0
        for group in self._calc_group_b():
            sum += len(group)
        return sum


if __name__ == "__main__":
    d6 = Day6("input_data.txt")
    print("d6a:", d6.sum_group_data_a())
    print("d6b:", d6.sum_group_data_b())
