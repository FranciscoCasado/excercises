import unittest

from graph import Node, Graph


class TestNode(unittest.TestCase):
    def test_empty_node(self):
        n = Node("a")
        self.assertEqual(n.name, "a")
        self.assertFalse(n.children)

    def test_node_with_two_children(self):
        n = Node("a", [Node("b"), Node("c")])
        self.assertEqual(n.name, "a")
        self.assertEqual(repr(n), "a->[b,c]")

    def test_add_duplicated_child(self):
        n = Node("a", node_list=[Node("b"), Node("b")])
        self.assertEqual(n.name, "a")
        self.assertEqual(repr(n), "a->[b]")


if __name__ == "__main__":
    unittest.main()
