import unittest

from queue import Queue, EmptyQueueException

class TestQueue(unittest.TestCase):
    def test_empty_queue(self):
        q = Queue()
        self.assertTrue(q.is_empty)
    
    def test_add_one_item(self):
        q = Queue()
        q.add(13)
        self.assertFalse(q.is_empty)
        self.assertEqual(q.list.first.data, 13)
        self.assertEqual(q.list.last.data, 13)
    
    def test_add_one_item_then_remove(self):
        q = Queue()
        q.add(13)
        r = q.remove()
        self.assertTrue(q.is_empty)
        self.assertEqual(r.data, 13)

    def test_add_three_items_then_remove_one(self):
        q = Queue()
        q.add(47)
        q.add(35)
        q.add(57)
        self.assertEqual(repr(q), '[57,35,47]')
        q.remove()
        self.assertEqual(repr(q), '[57,35]')


    
    def test_remove_from_empty_queue(self):
        q = Queue()
        self.assertRaises(EmptyQueueException, q.remove)
        


if __name__ == "__main__":
    unittest.main()
