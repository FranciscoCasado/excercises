import unittest

from data_structures.graph import Graph, Node

from cracking.ex_0401.route_between_nodes import find_route_between_nodes

class TestFindRouteBetweenNodes(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()
        self.assertIsNone(find_route_between_nodes("p", "q"))


if __name__ == "__main__":
    unittest.main()
