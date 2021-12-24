import unittest

from is_unique import is_unique

class TestIsUnique(unittest.TestCase):

    def test_unique_string(self):
        self.assertTrue(is_unique('hola'))

    
    def test_non_unique_string(self):
        self.assertFalse(is_unique('noesunica'))

if __name__ == '__main__':
    unittest.main()