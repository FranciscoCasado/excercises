from enum import Enum


class Node:
    def __init__(self, name, node_list=[]):
        self.name = name
        self._children = dict()
        self.add_nodes(node_list)

    @property
    def children(self):
        return list(self._children.values())

    def add_nodes(self, node_list):
        for node in node_list:
            if node.name not in self._children:
                self._children[node.name] = node

    def __repr__(self):
        children_list = ""
        for child in self._children.values():
            children_list += str(child.name) + ","

        return str(self.name) + "->[" + children_list[:-1] + "]"


class SearchType(Enum):
    DFS = 1
    BFS = 2


class Graph:
    def __init__(self, node_list=[]):
        self._nodes = node_list

    def find_node(search_type, data):
        if search_type == SearchType.DFS:
            return self.search_depth_first(data)
        if search_type == SearchType.BFS:
            return self.search_breadth_first(data)

    def add_node(parent_node, new_node):
        self._nodes.append(new_node)
        parent_node.add_node(new_node)

    def search_depth_first(self, data) -> Node:
        return Node()

    def search_breadth_first(self, data) -> Node:
        return Node()
