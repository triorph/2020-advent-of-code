import unittest
from .day17a import Conway3DSimulatorDay17a
from .day17b import Conway3DSimulatorDay17b


class TestDay17(unittest.TestCase):
    def setUp(self):
        self._d17a = Conway3DSimulatorDay17a("test_data.txt")
        self._d17b = Conway3DSimulatorDay17b("test_data.txt")

    def test_example_a(self):
        self.assertEqual(self._d17a.day_a(), 112)

    def test_example_b(self):
        self.assertEqual(self._d17b.day_b(), 848)
