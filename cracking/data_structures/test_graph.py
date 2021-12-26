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
        self.assertEqual(len(n.children), 2)

    def test_add_duplicated_child(self):
        n = Node("a", node_list=[Node("b"), Node("b")])
        self.assertEqual(n.name, "a")
        self.assertEqual(repr(n), "a->[b]")
        self.assertEqual(len(n.children), 1)


class TestGraph(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()
        self.assertFalse(g.nodes)

    def test_add_five_nodes(self):
        nodes = {char: Node(char) for char in "abcde"}
        g = Graph()
        g.add_nodes(nodes.values())
        self.assertEqual(len(g.nodes), 5)
        self.assertEqual(repr(g.nodes), "[a->[], b->[], c->[], d->[], e->[]]")

    def test_add_cycle_with_three_nodes(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.add_children([b])
        b.add_children([c])
        c.add_children([a])
        g = Graph([a])
        g.add_nodes([a])
        self.assertEqual(g.nodes, [a, b, c])

    def test_find_route_between_two_nodes(self):
        nodes = {char: Node(char) for char in "abcde"}
        nodes["a"].add_children([nodes["b"], nodes["c"]])
        nodes["b"].add_children([nodes["d"]])
        g = Graph()
        g.add_nodes(nodes.values())
        self.assertEqual(["a","b"], g.find_route_between_two_nodes("a", "b"))
        self.assertEqual(["a","c"], g.find_route_between_two_nodes("a", "c"))
        self.assertEqual(["a","b","d"], g.find_route_between_two_nodes("a", "d"))
        self.assertIsNone(g.find_route_between_two_nodes("a", "e"))
        self.assertIsNone(g.find_route_between_two_nodes("a", "g"))



if __name__ == "__main__":
    unittest.main()
