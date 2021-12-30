"""
Implementation of singly-linked list data structure
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 

class SinglyLinkedList:
    def __init__(self):
        self._root = Node()

    @property
    def is_empty(self):
        return not self._root.next

    @property
    def first_node(self):
        return self._root.next

    @property
    def first(self):
        return self.last_node.data

    @property
    def last_node(self):
        node = self.first_node
        while node:
            if not node.next:
                return node
            node = node.next
        
        return None
        
    @property
    def last(self):
        return self.last_node.data
        

    def find_node(self, data):
        node = self.first_node
        while node:
            if node.data == data:
                return node
            node = node.next
        
        return None

    def _find_previous_to_last_node(self):
        node = self._root
        while node and node.next:
            if not node.next.next:
                return node
            node = node.next
        
        return None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty:
            self._root.next = new_node
            return

        self.last_node.next = new_node

    def insert(self, ref_data, new_data):
        ref_node = self.find_node(ref_data)
        new_node = Node(new_data)
        new_node.next = ref_node.next
        ref_node.next = new_node

    def insert_at_begining(self, new_data):
        new_node = Node(new_data)
        new_node.next = self._root.next
        self._root.next = new_node

    def remove_node(self, data):
        node = self.find_node(data)
        if not node:
            return False
        if not node.next:
            self.remove_last_node()
            return True
        
        node.data = node.next.data
        node.next = node.next.next
        return True

    def remove_last_node(self):
        prev_to_last = self._find_previous_to_last_node()
        prev_to_last.next = None

    def __repr__(self):
        if self.is_empty:
            return "[]"

        node = self.first_node
        rep = ""
        while node:
            rep += str(node.data) + ","
            node = node.next

        return "[" + rep[:-1] + "]"
