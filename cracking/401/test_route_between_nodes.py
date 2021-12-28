import unittest

from cracking.data_structures.graph import Graph, Node
from route_between_nodes import find_route_between_nodes

class TestFindRouteBetweenNodes(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()
        self.assertIsNone(find_route_between_nodes("p", "q"))


if __name__ == "__main__":
    unittest.main()
