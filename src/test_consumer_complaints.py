import unittest
from .consumer_complaints import normal_round


class TestNormalRound(unittest.TestCase):
    def test_round(self):
        self.assertEqual(normal_round(0.499), 0)
        self.assertEqual(normal_round(0.50), 1)
        self.assertEqual(normal_round(1.5), 2)
        self.assertEqual(normal_round(-123.499999999999999999999999999999999999999999), -123)