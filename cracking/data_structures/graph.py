from enum import Enum
from stack import Stack


class Node:
    def __init__(self, name, node_list=[]):
        self.name = name
        self._children = dict()  # dict implementation ensures node uniqueness :)
        self.add_children(node_list)

    @property
    def children(self):
        return list(self._children.values())

    def add_children(self, node_list):
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
        self._nodes = dict()  # dict implementation ensures node uniqueness :)
        self.add_nodes(node_list)

    @property
    def nodes(self):
        return list(self._nodes.values())

    def add_nodes(self, node_list, parent_node=None):
        if parent_node:
            self._nodes[parent_node].add_children(node_list)

        for node in node_list:
            if node.name not in self._nodes:
                self._nodes[node.name] = node
                self.add_nodes(node.children)

    def find_node(self, name):
        if name in self._nodes:
            return self._nodes[name]

        return False

    def find_route_between_two_nodes(self, origin, destination):
        if origin not in self._nodes or destination not in self._nodes:
            return None
        s = Stack()
        s.push(self.find_node(origin))
        routes = dict()
        routes[origin] = [origin]  # the route to first node is itself

        while not s.is_empty:
            current_node = s.pop()

            for child in current_node.children:
                if child.name not in routes:
                    route = routes[current_node.name].copy()
                    route.append(child.name)
                    routes[child.name] = route
                    s.push(child)

                if child.name == destination:
                    return routes[child.name]

        return None
