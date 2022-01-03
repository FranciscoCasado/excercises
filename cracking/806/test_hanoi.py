import unittest

from hanoi import Tower, HanoiTowers, HanoiDiscError

class TestTower(unittest.TestCase):
    def test_empty_tower(self):
        t = Tower()
        self.assertFalse(t._list)
        self.assertIsNone(t.pop())
        
    def test_push_element_into_empty_tower(self):
        t = Tower()
        t.push(16)
        self.assertIsNotNone(t._list)
        self.assertEqual(t._list[-1], 16)

    def test_non_empty_tower(self):
        t = Tower(5)
        self.assertIsNotNone(t._list)
        self.assertEqual(list(t._list), [5, 4, 3, 2, 1])
        self.assertEqual(t.pop(), 1)
        
    
    def test_push_bigger_disc_and_raise_error(self):
        t = Tower(5)
        self.assertRaises(HanoiDiscError, t.push, 45)

    def test_tower_repr(self):
        t = Tower()
        self.assertEqual(repr(t),"[]")
        t = Tower(5)
        self.assertEqual(repr(t),"[5, 4, 3, 2, 1]")

    



if __name__ == "__main__":
    unittest.main()
