import unittest
from day2.day2 import PasswordChecker
import os.path


class Day2TestCase(unittest.TestCase):
    def setUp(self):
        self._day2 = PasswordChecker(
            os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_data.txt")
        )

    def test_validate_line_a(self):
        """Tests the validate password function for part a"""
        for line, is_valid in [
            ["1-3 a: hestloaa", True],
            ["2-4 b: by the way what is up babeby", True],
            ["2-2 c: hello chris", False],
            ["1-3 a: abaaaa", False],
            ["2-4 b: obabbbbbbb", False],
            ["2-2 c: ace", False],
        ]:
            self.assertEqual(self._day2.validate_line_a(line), is_valid, line)

    def test_validate_line_b(self):
        """Tests the validate password function for part b"""
        for line, is_valid in [
            ["1-3 a: hestloaa", False],
            ["2-4 b: by the way what is up babeby", False],
            ["2-2 c: hello chris", False],
            ["1-3 a: abcaaa", True],
            ["2-4 b: owabbbbbbb", True],
            ["2-3 c: ace", True],
            ["1-3 a: aba", False],
        ]:
            self.assertEqual(self._day2.validate_line_b(line), is_valid, line)

    def test_password_checker_day2a(self):
        """Test the password checker function gets the correct number of valid passwords for day 2a."""
        self._day2._lines = [
            "1-3 a: hestloaa",
            "2-4 b: by the way what is up babeby",
            "2-2 c: hello chris",
            "1-3 a: abaaaa",
            "2-4 b: obabbbbbbb",
            "2-2 c: ace",
        ]
        self.assertEqual(self._day2.check_passwords(self._day2.validate_line_a), 2)

    def test_password_checker_day2b(self):
        """Test the password checker function gets the correct number of valid passwords for day 2b."""
        self._day2._lines = [
            "1-3 a: hestloaa",
            "2-4 b: by the way what is up babeby",
            "2-2 c: hello chris",
            "1-3 a: abcaaa",
            "2-4 b: owabbbbbbb",
            "2-3 c: ace",
            "1-3 a: aba",
        ]
        self.assertEqual(self._day2.check_passwords(self._day2.validate_line_b), 3)
