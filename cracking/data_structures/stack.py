from linked_list import LinkedList, Node

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    @property
    def isEmpty(self):
        return self.stack.is_empty

    def push(self, data):
        self.stack.insert_at_end(Node(data))
    
    def pop(self):
        return self.stack.remove_node(self.stack.last)

    def peek(self):
        return self.stack.last.data

    
