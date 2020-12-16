class MemoryGameDay15:
    def __init__(self, filename):
        self._pattern = []
        self._build_data(filename)
        self._numbers = {}

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        self._pattern = [int(val) for val in lines[0].split(",")]

    def _get_next_number(self, number, current_turn):
        if number not in self._numbers:
            return 0
        else:
            return current_turn - self._numbers[number]

    def _initialise_numbers(self, pattern):
        self._numbers = {}
        for i, val in enumerate(pattern):
            self._numbers[val] = i + 1

    def find_until(self, count):
        pattern = self._pattern.copy()
        self._initialise_numbers(pattern[:-1])
        old_number = number = pattern[-1]
        for current_turn in range(len(pattern), count):
            number = self._get_next_number(old_number, current_turn)
            pattern.append(number)
            self._numbers[old_number] = current_turn
            old_number = number
        print(pattern[:30])
        return number

    def day_a(self):
        return self.find_until(2020)

    def day_b(self):
        return self.find_until(30000000)


if __name__ == "__main__":
    d15 = MemoryGameDay15("input_data.txt")
    print("d15a:", d15.day_a())
    print("d15b:", d15.day_b())
