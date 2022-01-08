import unittest

from recursive_multiply import multiply


class TestRecursiveMultiply(unittest.TestCase):
    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5,0), 0)
        self.assertEqual(multiply(0,10), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply(5,1), 5)
        self.assertEqual(multiply(1,3), 3)
        

if __name__ == "__main__":
    unittest.main()
