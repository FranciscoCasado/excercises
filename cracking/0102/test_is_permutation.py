import unittest
from is_permutation import is_permutation


class TestIsPermutation(unittest.TestCase):
    def test_different_lengths(self):
        self.assertFalse(is_permutation("a", "aa"))

    def test_permuted(self):
        self.assertTrue(is_permutation("ola", "alo"))

    def test_non_permuted(self):
        self.assertFalse(is_permutation("ola", "abc"))


if __name__ == "__main__":
    unittest.main()
