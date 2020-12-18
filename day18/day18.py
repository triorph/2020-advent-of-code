"""Day 18: calculate maths left to right, or with alternate operator precedence"""


class LeftToRightArithmaticDay18:
    def __init__(self, filename):
        self._equations = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            self._equations = f.readlines()

    @staticmethod
    def _get_next_value(line, current_index):
        for i in range(current_index, len(line)):
            if line[i] in [str(c) for c in range(10)]:
                next_index = line[i:].find(" ")
                if next_index == -1:
                    return len(line) + 1, int(line[i:])
                else:
                    return next_index + i, int(line[i : next_index + i])

    @staticmethod
    def _get_next_operator(line, current_index):
        for i in range(current_index, len(line)):
            if line[i] in ["+", "*"]:
                return i, line[i]
        return len(line) + 1, None

    @staticmethod
    def _find_matching_bracket_index(line, first_bracket):
        bracket_depth = 1
        for i in range(first_bracket + 1, len(line)):
            if line[i] == "(":
                bracket_depth += 1
            if line[i] == ")":
                bracket_depth -= 1
            if bracket_depth == 0:
                return i
        raise RuntimeError("No matching bracket found for " + line[first_bracket:])

    @classmethod
    def _do_brackets_a(cls, line):
        first_bracket = line.find("(")
        matching_bracket = cls._find_matching_bracket_index(line, first_bracket)
        bracket_result = cls.calculate_equation_a(
            line[first_bracket + 1 : matching_bracket]
        )
        return (
            line[0:first_bracket] + str(bracket_result) + line[matching_bracket + 1 :]
        )

    @classmethod
    def calculate_equation_a(cls, line):
        """Calculate a line of brackets first, and then left to right"""
        while "(" in line:
            line = cls._do_brackets_a(line)
        return cls._basic_eval(line)

    @staticmethod
    def _do_additions(line):
        first_plus = line.find("+")
        left_number_index = line[: first_plus - 1].rfind(" ")
        if left_number_index == -1:
            left_number_index = 0
        else:
            left_number_index += 1
        left_number = int(line[left_number_index : first_plus - 1])
        right_number_index = line[first_plus + 2 :].find(" ")
        if right_number_index != -1:
            right_number_index += first_plus + 2
        else:
            right_number_index = len(line)
        right_number = int(line[first_plus + 1 : right_number_index])
        return (
            line[:left_number_index]
            + str(left_number + right_number)
            + line[right_number_index:]
        )

    @classmethod
    def _do_brackets_b(cls, line):
        first_bracket = line.find("(")
        matching_bracket = cls._find_matching_bracket_index(line, first_bracket)
        bracket_result = cls.calculate_equation_b(
            line[first_bracket + 1 : matching_bracket]
        )
        return (
            line[0:first_bracket] + str(bracket_result) + line[matching_bracket + 1 :]
        )

    @classmethod
    def _basic_eval(cls, line):
        current_index = next_val = current_val = operator = 0
        current_index, current_val = cls._get_next_value(line, 0)
        while current_index < len(line):
            current_index, operator = cls._get_next_operator(line, current_index)
            current_index, next_val = cls._get_next_value(line, current_index)
            if operator == "+":
                current_val += next_val
            else:  # operator == "*"
                current_val *= next_val
        return current_val

    @classmethod
    def calculate_equation_b(cls, line):
        """Calculate a line using a method of brackets before additions before multiplication"""
        while "(" in line:
            line = cls._do_brackets_b(line)
        while "+" in line:
            line = cls._do_additions(line)
        return cls._basic_eval(line)

    def day_a(self):
        """Get the sum of all math results for style a calculations"""
        return sum([self.calculate_equation_a(line) for line in self._equations])

    def day_b(self):
        """Get the sum of all math results for style b calculations"""
        return sum([self.calculate_equation_b(line) for line in self._equations])


if __name__ == "__main__":
    d18 = LeftToRightArithmaticDay18("input_data.txt")
    print("d18a:", d18.day_a())
    print("d18b:", d18.day_b())
