import unittest
from length_number import length_num


class TestLengthNum(unittest.TestCase):
    def test_length_num(self):
        self.assertEqual(length_num(10), 2)
