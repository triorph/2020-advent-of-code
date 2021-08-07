"""Find multiple numbers that sum to 2020 and return their product"""
import itertools
import numpy


class Day1:
    """
    Do the day 1 advent of code challenge.

    a) From a list of numbers, find which 2 add to 2020, and return their product
    b) From a list of numbers, find which 3 add to 2020, and return their product
    """

    def __init__(self, filename):
        self._numbers = []
        self._build_data(filename)

    def _build_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        self._numbers = [int(line) for line in lines]

    def get_values(self, total, quantity):
        """Get the <quantity> numbers in data that sum to total"""
        for numbers in itertools.combinations(self._numbers, quantity):
            if sum(numbers) == total:
                return numbers
        raise ValueError("No data exists to sum to: " + str(quantity))

    def get_multiplication(self, total, quantity):
        """Get the product of <quantity> numbers in data that sum to total"""
        numbers = self.get_values(total, quantity)
        return numpy.product(numbers)


if __name__ == "__main__":
    d1 = Day1("input_data.txt")
    print("d1a:", d1.get_multiplication(2020, 2))
    print("d1b:", d1.get_multiplication(2020, 3))
