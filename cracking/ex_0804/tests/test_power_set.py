import unittest

from cracking.ex_0804.power_set import power_set


class TestPowerSet(unittest.TestCase):
    def test_empty_set(self):
        s = []
        self.assertEqual(power_set(s), [[]])


    def test_singleton(self):
        s = ['a']
        self.assertEqual(power_set(s), [[], ['a']])


    def test_two_items(self):
        s = ['a', 'b']
        self.assertEqual(power_set(s), [[], ['a'], ['b'], ['a','b']])



if __name__ == "__main__":
    unittest.main()