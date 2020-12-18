class PasswordChecker:
    def __init__(self, filename):
        self._lines = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            self._lines = f.readlines()

    def get_low_high_password_letter(self, line):
        rule, password = line.split(":")
        numbers, letter = rule.strip().split(" ")
        low, high = numbers.split("-")
        password = password.strip()
        return int(low), int(high), password, letter

    def validate_line_a(self, line):
        low, high, password, letter = self.get_low_high_password_letter(line)
        count = password.count(letter)
        return count >= low and count <= high

    def validate_line_b(self, line):
        low, high, password, letter = self.get_low_high_password_letter(line)
        low, high = low - 1, high - 1
        return (password[low] == letter) ^ (password[high] == letter)  # XOR operator

    def check_passwords(self, validator):
        correct_count = 0
        for line in self._lines:
            if validator(line):
                correct_count += 1
        return correct_count

    def day_a(self):
        return self.check_passwords(self.validate_line_a)

    def day_b(self):
        return self.check_passwords(self.validate_line_b)


if __name__ == "__main__":
    d2 = PasswordChecker("input_data.txt")
    print("d2a:", d2.day_a())
    print("d2a:", d2.day_b())
