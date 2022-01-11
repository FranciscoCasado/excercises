import unittest

from mastermind import hits


class TestHitCount(unittest.TestCase):
    def test_hits(self):
        solution = "RGBY"
        guess = "GGRR"
        h = hits(solution, guess)
        self.assertEqual(h, {'hits': 1, 'pseudo': 1})

if __name__ == "__main__":
    unittest.main()