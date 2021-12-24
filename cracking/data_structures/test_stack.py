import unittest

from stack import Stack, EmptyStackException

class TestStack(unittest.TestCase):
    def test_empty_stack(self):
        s = Stack()
        self.assertTrue(s.isEmpty)

    def test_push_one_item(self):
        s = Stack()
        s.push(1)
        self.assertFalse(s.isEmpty)
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
        self.assertTrue(s.isEmpty)
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
        
if __name__ == '__main__':
    unittest.main()