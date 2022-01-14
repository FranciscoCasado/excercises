import unittest

from hanoi import Tower, HanoiTowers, HanoiDiscError, MoveTowerError


class TestTower(unittest.TestCase):
    def test_empty_tower(self):
        t = Tower()
        self.assertTrue(t.is_empty)
        self.assertIsNone(t.pop())

    def test_push_element_into_empty_tower(self):
        t = Tower()
        t.push(16)
        self.assertFalse(t.is_empty)
        self.assertEqual(t._list[-1], 16)
        self.assertRaises(HanoiDiscError, t.push, None)

    def test_non_empty_tower(self):
        t = Tower(5)
        self.assertIsNotNone(t._list)
        self.assertEqual(list(t._list), [5, 4, 3, 2, 1])
        self.assertEqual(t.pop(), 1)

    def test_equality(self):
        a = Tower(5)
        self.assertTrue(a.__eq__(Tower(5)))
        self.assertFalse(a.__eq__(Tower(4)))
        self.assertFalse(a.__eq__(0))

    def test_push_bigger_disc_and_raise_error(self):
        t = Tower(5)
        self.assertRaises(HanoiDiscError, t.push, 45)

    def test_tower_repr(self):
        t = Tower()
        self.assertEqual(repr(t), "[]")
        t = Tower(5)
        self.assertEqual(repr(t), "[5, 4, 3, 2, 1]")


class TestHanoiTowers(unittest.TestCase):
    def test_create_hanoi_towers(self):
        h = HanoiTowers(5)
        self.assertEqual(len(h._towers), 3)
        self.assertEqual(repr(h._towers[0]), repr(Tower(5)))

        h_repr = "A:[5, 4, 3, 2, 1]\nB:[]\nC:[]"
        self.assertEqual(repr(h), h_repr)

    def test_move_single_disc_tower(self):
        h = HanoiTowers(1)

        [a, b, c] = h._towers

        h._move_tower(a, b, c, 1)

        self.assertEqual(a, Tower())
        self.assertEqual(b, Tower(1))
        self.assertEqual(c, Tower())
        
    def test_shitft_hanoi_towers(self):
        h = HanoiTowers(10)
        h.shift_towers()
        
        [a, b, c] = h._towers
        self.assertEqual(a, Tower())
        self.assertEqual(b, Tower(10))
        self.assertEqual(c, Tower())
    
    def test_move_empty_tower(self):
        h = HanoiTowers(5)
        
        [a, b, c] = h._towers
        self.assertRaises(MoveTowerError, h._move_tower, b, a, c, 5)
    
    def test_move_zero_discs(self):
        h = HanoiTowers(5)
        
        [a, b, c] = h._towers
        self.assertRaises(MoveTowerError, h._move_tower, a, b, c, 0)




if __name__ == "__main__":
    unittest.main()
