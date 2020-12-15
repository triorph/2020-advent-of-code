class Day1A:
    def __init__(self):
        self._less_than = []
        self._greater_than = []

    def _read_file(self, filename):
        with open(filename, "r") as f:
            return f.readlines()

    def _split_by_size(self, data, size):
        for line in data:
            number = int(line)
            if number not in self._less_than and number <= size:
                self._less_than.append(number)
            elif number >= size:
                self._greater_than.append(number)

    def get_values(self, filename, size):
        lines = self._read_file(filename)
        self._split_by_size(lines, int(size / 2))
        for number in self._less_than:
            for number_2 in self._greater_than:
                if number + number_2 == size:
                    return number, number_2
        return 0, 0

    def get_multiplication(self, filename, size):
        number_1, number_2 = self.get_values(filename, size)
        print("Got values", number_1, number_2)
        print("multiplied to:", number_1 * number_2)


if __name__ == "__main__":
    Day1A().get_multiplication("input_data.txt", 2020)
