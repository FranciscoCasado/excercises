import unittest

from cracking.ex_1701.add_without_plus import add, bit_sum, carry, bit, set_bit

class TestHelperFunctions(unittest.TestCase):
    def test_get_bit(self):
        self.assertEqual(bit(15, 0), 1)
        self.assertEqual(bit(15, 1), 1)
        self.assertEqual(bit(15, 2), 1)
        self.assertEqual(bit(15, 3), 1)
        self.assertEqual(bit(15, 4), 0)
        self.assertEqual(bit(8, 0), 0)
        self.assertEqual(bit(8, 1), 0)
        self.assertEqual(bit(8, 2), 0)
        self.assertEqual(bit(8, 3), 1)
    
    def test_set_bit(self):
        c = 0
        c = set_bit(c, 1, 3)
        self.assertEqual(c, 8)
        c = set_bit(c, 1, 2)
        self.assertEqual(c, 12)

    def test_bit_sum(self):
        self.assertEqual(bit_sum(0, 0, 0), 0)
        self.assertEqual(bit_sum(0, 0, 1), 1)
        self.assertEqual(bit_sum(0, 1, 0), 1)
        self.assertEqual(bit_sum(0, 1, 1), 0)
        self.assertEqual(bit_sum(1, 0, 0), 1)
        self.assertEqual(bit_sum(1, 0, 1), 0)
        self.assertEqual(bit_sum(1, 1, 0), 0)
        self.assertEqual(bit_sum(1, 1, 1), 1)

    def test_carry_out(self):
        self.assertEqual(carry(0, 0, 0), 0)
        self.assertEqual(carry(0, 0, 1), 0)
        self.assertEqual(carry(0, 1, 0), 0)
        self.assertEqual(carry(0, 1, 1), 1)
        self.assertEqual(carry(1, 0, 0), 0)
        self.assertEqual(carry(1, 0, 1), 1)
        self.assertEqual(carry(1, 1, 0), 1)
        self.assertEqual(carry(1, 1, 1), 1)


class TestAddWithoutPlus(unittest.TestCase):
    def test_zero_plus_zero(self):
        self.assertEqual(add(0,0), 0)

    def test_zero_plus_one(self):
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(1, 0), 1)

    def test_three_plus_two(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(3, 2), 5) 

if __name__ == "__main__":
    unittest.main()
