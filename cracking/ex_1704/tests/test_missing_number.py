import unittest
from random import shuffle

from cracking.ex_1704.missing_number import missing_number, discard_numbers_with_bit


class TestMissingNumber(unittest.TestCase):
    def test_two_numbers_miss_0(self):
        l = [1]
        self.assertEqual(missing_number(l), 0)
    
    def test_two_numbers_miss_1(self):
        l = [0]
        self.assertEqual(missing_number(l), 1)
    
    def test_five_numbers_miss_0(self):
        l = [1, 2, 3, 4]
        self.assertEqual(missing_number(l), 0)
    
    def test_five_numbers_miss_2(self):
        l = [0, 1, 3, 4]
        self.assertEqual(missing_number(l), 2)

    def test_ten_numbers_miss_5(self):
        l = [0, 1, 2, 3, 4, 6, 7, 8, 9]
        self.assertEqual(missing_number(l), 5)

    def test_ten_numbers_miss_6(self):
        l = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
        self.assertEqual(missing_number(l), 6)
    
    def test_ten_numbers_miss_6_unsorted(self):
        l = [7, 3, 2, 9, 4, 8, 5, 0, 10, 1]
        self.assertEqual(missing_number(l), 6)

class TestDiscardNumbers(unittest.TestCase):
    def test_discard_lsb_1(self):
        l = list(range(10))
        discard_numbers_with_bit(l, 0, 1)
        self.assertEqual(l, [0, 2, 4, 6, 8])

    def test_discard_lsb_0(self):
        l = list(range(10))
        discard_numbers_with_bit(l, 0, 0)
        self.assertEqual(l, [1, 3, 5, 7, 9])
    
    def test_discard_b1_1(self):
        l = list(range(10))
        discard_numbers_with_bit(l, 1, 1)
        self.assertEqual(l, [0, 1, 4, 5, 8, 9])
    
    def test_discard_b1_1(self):
        l = list(range(10))
        discard_numbers_with_bit(l, 1, 0)
        self.assertEqual(l, [2, 3, 6, 7])

if __name__ == "__main__":
    unittest.main()