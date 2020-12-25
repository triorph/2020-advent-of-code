from .day25 import CryptoHackerDay25
import unittest


class TestDay25(unittest.TestCase):
    def test_find_private_key(self):
        d25 = CryptoHackerDay25("example_data.txt")
        self.assertEqual(d25.find_private_key(7, d25._public_keys[0]), 8)
        self.assertEqual(d25.find_private_key(7, d25._public_keys[1]), 11)

    def test_day_a(self):
        d25 = CryptoHackerDay25("example_data.txt")
        self.assertEqual(d25.day_a(), 14897079)