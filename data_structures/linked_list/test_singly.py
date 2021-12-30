import unittest

from singly import Node, SinglyLinkedList


class TestNode(unittest.TestCase):
    def test_empty_node(self):
        n = Node()
        self.assertIsNone(n.data)
        self.assertIsNone(n.next)

    def test_node(self):
        n = Node(data=0, next=Node())
        self.assertEqual(n.data, 0)
        self.assertIsNotNone(n.next)


class TestSinglyLinkedList(unittest.TestCase):
    def test_empty_list(self):
        l = SinglyLinkedList()
        self.assertIsNotNone(l._root)
        self.assertIsNone(l.first_node)
        self.assertEqual(repr(l), "[]")

    def test_list_with_one_node(self):
        l = SinglyLinkedList()

        l.append(33)
        self.assertEqual(l.first, 33)
        self.assertEqual(l.last, 33)

    def test_list_with_two_nodes(self):
        l = SinglyLinkedList()
        l.append(33)
        l.append(44)
        self.assertEqual(l.first_node.data, 33)
        self.assertEqual(l.last_node.data, 44)

    def test_insert_node(self):
        l = SinglyLinkedList()
        l.append(33)
        l.append(44)
        l.append(66)
        l.insert(44, 55)
        self.assertEqual(l.first_node.next.next.data, 55)
        self.assertEqual(l.find_node(55).next, l.last_node)
        self.assertIsNotNone(l.find_node(55).next)

    def test_linked_list_repr(self):
        l = SinglyLinkedList()
        l.append(67)
        l.append(34)
        l.insert_at_begining(17)
        l.insert(67, 81)
        self.assertEqual(repr(l), "[17,67,81,34]")

        l.insert(34, 1)
        self.assertEqual(repr(l), "[17,67,81,34,1]")

    def test_remove_node(self):
        l = SinglyLinkedList()
        l.append(22)
        l.append(44)
        l.append(55)
        l.append(66)
        
        self.assertFalse(l.remove_node(33))

        self.assertTrue(l.remove_node(44))
        self.assertEqual(repr(l), "[22,55,66]")

        self.assertTrue(l.remove_node(22))
        self.assertEqual(repr(l), "[55,66]")

        self.assertTrue(l.remove_node(66))
        self.assertEqual(repr(l), "[55]")

        self.assertTrue(l.remove_node(55))
        self.assertEqual(repr(l), "[]")

if __name__ == "__main__":
    unittest.main()
