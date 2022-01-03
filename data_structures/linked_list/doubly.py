"""
Implementation of doubly-linked list data structure
"""


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self._root = Node()
        self._tail = Node()
        self._root.next = self._tail
        self._tail.prev = self._root

    @property
    def is_empty(self):
        return self._root.next == self._tail

    @property
    def first(self):
        if self.is_empty:
            return None
        return self._root.next

    @property
    def last(self):
        if self.is_empty:
            return None
        return self._tail.prev

    def insert_at_begining(self, new_node):
        self.insert_node_next(self._root, new_node)

    def insert_at_end(self, new_node):
        self.insert_node_prev(self._tail, new_node)

    def insert_node_next(self, ref_node, new_node):
        if type(new_node) != Node:
            new_node = Node(new_node)
        new_node.next = ref_node.next
        new_node.prev = ref_node
        ref_node.next.prev = new_node
        ref_node.next = new_node

    def insert_node_prev(self, ref_node, new_node):
        if type(new_node) != Node:
            new_node = Node(new_node)
        new_node.prev = ref_node.prev
        new_node.next = ref_node
        ref_node.prev.next = new_node
        ref_node.prev = new_node

    def find_node(self, content):
        n = self.first
        while n.next:
            if n.data == content:
                return n
            n = n.next

        return None

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def __repr__(self):
        if self.is_empty:
            return "[]"

        n = self.first
        rep = ""
        while n.next:
            rep += str(n.data) + ","
            n = n.next

        return "[" + rep[:-1] + "]"
