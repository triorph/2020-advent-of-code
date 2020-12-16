class Day9XMASCode:
    def __init__(self, filename):
        self._data = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            self._data = [int(line) for line in f.readlines()]

    def _check_line_at_index(self, index):
        previous_25 = self._data[index - 25 : index]
        value = self._data[index]
        for i, num_1 in enumerate(previous_25[:-1]):
            for j, num_2 in enumerate(previous_25[i + 1 :]):
                if num_1 + num_2 == value:
                    return True
        return False

    def check_first_fail(self):
        for index in range(26, len(self._data)):
            if not self._check_line_at_index(index):
                return self._data[index]
        return None

    def find_contiguous_range_equals(self, failure_number):
        for i in range(len(self._data)):
            sum = self._data[i]
            for j, val in enumerate(self._data[i + 1 :]):
                sum += val
                if sum > failure_number:
                    break
                elif sum == failure_number:
                    return max(self._data[i : i + j + 1]) + min(
                        self._data[i : i + j + 1]
                    )


if __name__ == "__main__":
    d9 = Day9XMASCode("input_data.txt")
    failure_number = d9.check_first_fail()
    print("d9a:", d9.check_first_fail())
    print("d9b:", d9.find_contiguous_range_equals(failure_number))
