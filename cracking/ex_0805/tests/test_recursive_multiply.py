import unittest

from cracking.ex_0805.recursive_multiply import multiply


class TestRecursiveMultiply(unittest.TestCase):
    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5,0), 0)
        self.assertEqual(multiply(0,10), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply(5,1), 5)
        self.assertEqual(multiply(1,3), 3)


    def test_multiply_by_two_numbers(self):
        self.assertEqual(multiply(5,2), 10)
        self.assertEqual(multiply(2,3), 6)
        

if __name__ == "__main__":
    unittest.main()
