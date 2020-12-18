import unittest
from .day18 import LeftToRightArithmaticDay18


class TestArithmatic(unittest.TestCase):
    def test_day_a_examples(self):
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_a("2 * 3 + (4 * 5)"), 26
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_a(
                "5 + (8 * 3 + 9 + 3 * 4 * 3)"
            ),
            437,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_a(
                "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
            ),
            12240,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_a(
                "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
            ),
            13632,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_a(
                "1 + (2 * 3) + (4 * (5 + 6))"
            ),
            51,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_a("1 + 2 * 3 + 4 * 5 + 6"), 71
        )

    def test_day_b_examples(self):
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_b("2 * 3 + (4 * 5)"), 46
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_b(
                "5 + (8 * 3 + 9 + 3 * 4 * 3)"
            ),
            1445,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_b(
                "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
            ),
            669060,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_b(
                "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
            ),
            23340,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_b(
                "1 + (2 * 3) + (4 * (5 + 6))"
            ),
            51,
        )
        self.assertEqual(
            LeftToRightArithmaticDay18.calculate_equation_b("1 + 2 * 3 + 4 * 5 + 6"),
            231,
        )
