import unittest

from triple_step import count_ways, count_ways_dynamic


class TestTripleStep(unittest.TestCase):
    def test_base_case_recursive(self):
        self.assertEqual(count_ways(0), 0)
        self.assertEqual(count_ways(1), 1)
        self.assertEqual(count_ways(2), 2)

    def test_base_case_dynamic(self):
        self.assertEqual(count_ways_dynamic(0), 0)
        self.assertEqual(count_ways_dynamic(1), 1)
        self.assertEqual(count_ways_dynamic(2), 2)

    def test_sample_case(self):
        self.assertEqual(count_ways(4), 6)
        self.assertEqual(count_ways_dynamic(4), 6)
        self.assertEqual(count_ways(10), count_ways_dynamic(10))
        self.assertEqual(count_ways(25), count_ways_dynamic(25))


if __name__ == "__main__":
    unittest.main()
