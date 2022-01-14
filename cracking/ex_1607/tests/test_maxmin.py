import unittest

from cracking.ex_1607.maxmin import max, min


class TestMaxMin(unittest.TestCase):
    def test_max(self):
        a = 10
        b = -5
        self.assertEqual(max(a,b), a)

    def test_min(self):
        a = 10
        b = -5
        self.assertEqual(min(a,b), b)

if __name__ == "__main__":
    unittest.main()