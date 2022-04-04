import unittest

from data_structures.graph_v2 import Graph


class TestGraph(unittest.TestCase):
    def test_empty_graph(self):
        V = []
        E = []
        g = Graph(V, E)

        self.assertEqual(len(g.vertices), 0)

    def test_non_empty_graph(self):
        V = ["a", "b", "c"]
        E = []
        g = Graph(V, E)

        self.assertIn("a", g)
        self.assertIn("b", g)
        self.assertIn("c", g)
        self.assertNotIn("d", g)

    def test_edge_validation(self):
        V = ["a", "b"]
        E = [("a", "b")]
        g = Graph(V, E)

        self.assertIn(("a", "b"), g.edges)

        V = ["a", "b"]
        E = [("a", "b"), ("a", "c")]
        self.assertRaises(ValueError, Graph, V, E)
        

    def test_BFS(self):
        V = ["a", "b", "c", "d", "e"]
        E = [
            ("a", "b"),
            ("a", "d"),
            ("a", "e"),
            ("b", "c"),
            ("b", "d"),
            ("d", "c"),
            ("d", "e"),
        ]
        g = Graph(V, E)
        
        visited, distance_to = g.breadth_first_search("a")
        self.assertEqual(visited, ["a", "b", "d", "e", "c"])
        self.assertEqual(distance_to, {"a": 0, "b": 1, "d": 1, "e": 1, "c": 2})

        visited, distance_to = g.breadth_first_search("d")
        self.assertEqual(visited, ["d", "c", "e"])
        self.assertEqual(distance_to, {"d": 0, "c": 1, "e": 1})

        visited, distance_to = g.breadth_first_search("e")
        self.assertEqual(visited, ["e"])
        self.assertEqual(distance_to, {"e": 0})

    def test_DFS(self):
        V = ["a", "b", "c", "d", "e"]
        E = [
            ("a", "b"),
            ("a", "d"),
            ("a", "e"),
            ("b", "c"),
            ("b", "d"),
            ("d", "c"),
            ("d", "e"),
        ]
        g = Graph(V, E)
        
        visited, distance_to = g.depth_first_search("a")
        self.assertEqual(visited, ["a", "b", "d", "e", "c"])
        self.assertEqual(distance_to, {"a": 0, "b": 1, "d": 1, "e": 1, "c": 2})

        visited, distance_to = g.depth_first_search("d")
        self.assertEqual(visited, ["d", "c", "e"])
        self.assertEqual(distance_to, {"d": 0, "c": 1, "e": 1})

        visited, distance_to = g.depth_first_search("e")
        self.assertEqual(visited, ["e"])
        self.assertEqual(distance_to, {"e": 0})
