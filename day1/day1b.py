class Day1B:
    def __init__(self):
        self._numbers = []

    def _read_file(self, filename):
        with open(filename, "r") as f:
            return f.readlines()

    def _get_numbers(self, data):
        for line in data:
            number = int(line)
            self._numbers.append(number)

    def get_values(self, filename, size):
        lines = self._read_file(filename)
        self._get_numbers(lines)
        for i, number in enumerate(self._numbers):
            for j, number_2 in enumerate(self._numbers[i + 1 :]):
                for k, number_3 in enumerate(self._numbers[j + 1 :]):
                    if number + number_2 + number_3 == size:
                        return number, number_2, number_3
        return 0, 0, 0

    def get_multiplication(self, filename, size):
        number_1, number_2, number_3 = self.get_values(filename, size)
        print("Got values", number_1, number_2, number_3)
        print("multiplied to:", number_1 * number_2 * number_3)


if __name__ == "__main__":
    Day1B().get_multiplication("input_data.txt", 2020)
