import unittest

from linked_list import Node, LinkedList

class TestNode(unittest.TestCase):

    def test_empty_node(self):
        n = Node()
        self.assertIsNone(n.data)
        self.assertIsNone(n.prev)
        self.assertIsNone(n.next)
    
    def test_node(self):
        n = Node(data=0, next=Node(), prev=Node())
        self.assertEqual(n.data, 0)
        self.assertIsNotNone(n.prev)
        self.assertIsNotNone(n.next)

class TestLinkedList(unittest.TestCase):
    
    def test_empty_list(self):
        l = LinkedList()
        self.assertIsNotNone(l._root)
        self.assertIsNotNone(l._tail)
        self.assertEqual(l._root.next, l._tail)
        self.assertEqual(l._tail.prev, l._root)
        self.assertIsNone(l.first)
        self.assertIsNone(l.last)
        self.assertEqual(repr(l), '[]')

    def test_list_with_one_node(self):
        l = LinkedList()
        l.insert_at_begining(Node(56))
        self.assertEqual(l.first.data, 56)
        self.assertEqual(l.first, l.last)

    def test_insert_node_next(self):
        l = LinkedList()
        l.insert_at_begining(Node(33))
        l.insert_node_next(l.first, Node(56))
        self.assertEqual(l.first.data, 33)
        self.assertEqual(l.last.data, 56)
        self.assertEqual(l.first.next.data, 56)
        self.assertEqual(l.last.prev.data, 33)

    def test_insert_node_prev(self):
        l = LinkedList()
        l.insert_at_begining(Node(33))
        l.insert_node_prev(l.first, Node(56))
        self.assertEqual(l.first.data, 56)
        self.assertEqual(l.last.data, 33)
        self.assertEqual(l.first.next.data, 33)
        self.assertEqual(l.last.prev.data, 56)

    def test_linked_list_repr(self):
        l = LinkedList()
        l.insert_at_begining(Node(34))
        l.insert_at_begining(Node(67))
        l.insert_at_begining(Node(17))
        l.insert_at_end(Node(81))
        self.assertEqual(repr(l), '[17,67,34,81]')



if __name__ == '__main__':
    unittest.main()