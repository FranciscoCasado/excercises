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

    def test_equality(self):
        a = Tower(5)
        self.assertTrue(a.__eq__(Tower(5)))
        self.assertFalse(a.__eq__(Tower(4)))

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

    def test_move_tower(self):
        h = HanoiTowers(1)

        [a, b, c] = h._towers

        h.move_tower(a, b, c, 1)

        self.assertEqual(a, Tower())
        self.assertEqual(b, Tower(1))
        self.assertEqual(c, Tower())


if __name__ == "__main__":
    unittest.main()
