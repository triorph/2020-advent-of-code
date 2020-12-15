class PasswordChecker:
    def __init__(self):
        pass

    def validate_line(self, line):
        rule, password = line.split(":")
        numbers, letter = rule.strip().split(" ")
        low, high = numbers.split("-")
        password = password.strip()
        low = int(low) - 1
        high = int(high) - 1
        return (password[low] == letter) ^ (password[high] == letter)  # XOR operator

    def check_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        correct_count = 0
        for line in lines:
            if self.validate_line(line):
                correct_count += 1

        print(f"counted {correct_count} correct passwords")


if __name__ == "__main__":
    PasswordChecker().check_file("input_data.txt")
