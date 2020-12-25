class CryptoHackerDay25:
    DIVISOR_A = 20201227

    def __init__(self, filename):
        self._public_keys = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        self._public_keys = [int(line.strip()) for line in lines]

    def _get_next_transform(self, value, subject_number):
        return (value * subject_number) % self.DIVISOR_A

    def find_private_key(self, subject_number, public_key):
        value = 1
        for loop in range(10000000):  # hopefully a sensible maximum counter
            value = self._get_next_transform(value, subject_number)
            if value == public_key:
                return loop + 1
        raise RuntimeError("No loop found")

    def find_encryption_value(self, subject_number, loop_count):
        value = 1
        for _ in range(loop_count):
            value = self._get_next_transform(value, subject_number)
        return value

    def day_a(self):
        private_key_1 = self.find_private_key(7, self._public_keys[0])
        return self.find_encryption_value(self._public_keys[1], private_key_1)


if __name__ == "__main__":
    d25 = CryptoHackerDay25("input_data.txt")
    print("d25a:", d25.day_a())