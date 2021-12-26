import unittest

from stack import Stack, EmptyStackException


class TestStack(unittest.TestCase):
    def test_empty_stack(self):
        s = Stack()
        self.assertTrue(s.is_empty)

    def test_push_one_item(self):
        s = Stack()
        s.push(1)
        self.assertFalse(s.is_empty)
        self.assertEqual(s.list.first.data, 1)

    def test_push_two_items(self):
        s = Stack()
        s.push(23)
        s.push(42)
        self.assertEqual(s.list.first.data, 23)
        self.assertEqual(s.list.last.data, 42)

    def test_push_one_item_then_pop_one(self):
        s = Stack()
        s.push(15)
        p = s.pop()
        self.assertTrue(s.is_empty)
        self.assertEqual(p.data, 15)

    def test_pop_from_empty_stack(self):
        s = Stack()
        self.assertRaises(EmptyStackException, s.pop)

    def test_peek_from_emty_stack(self):
        s = Stack()
        self.assertRaises(EmptyStackException, s.peek)

    def test_peek_from_non_emty_stack(self):
        s = Stack()
        s.push(15)
        self.assertEqual(s.peek(), 15)

    def test_add_three_items_then_remove_one(self):
        s = Stack()
        s.push(47)
        s.push(35)
        s.push(57)
        self.assertEqual(repr(s), "[47,35,57]")
        s.pop()
        self.assertEqual(repr(s), "[47,35]")


if __name__ == "__main__":
    unittest.main()
