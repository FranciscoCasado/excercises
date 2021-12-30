import unittest

from triple_step import dynamic_triple_step

class TestDynamicTripleStep(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(dynamic_triple_step(0) , 0)
        self.assertEqual(dynamic_triple_step(1) , 1)
        self.assertEqual(dynamic_triple_step(2) , 2)

    def test_sample_cas(self):
        self.assertEqual(dynamic_triple_step(4) , 6)


if __name__ == "__main__":
    unittest.main()