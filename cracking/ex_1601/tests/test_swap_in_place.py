import unittest

from cracking.ex_1601.swap_in_place import swap

class TestSwapInPlace(unittest.TestCase):
    def test_swap_numbers(self):
        a = 5
        b = 15
        self.assertEqual(swap(a,b), (15,5))

if __name__ == "__main__":
    unittest.main()
