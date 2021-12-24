from linked_list import LinkedList, Node

class Stack:
    def __init__(self):
        self.list = LinkedList()

    @property
    def isEmpty(self):
        return self.list.is_empty

    def push(self, data):
        self.list.insert_at_end(data)
    
    def pop(self):
        if self.isEmpty:
            raise EmptyStackException()
        return self.list.remove_node(self.list.last)

    def peek(self):
        if self.isEmpty:
            raise EmptyStackException()
        return self.list.last.data

class EmptyStackException(Exception):
    pass
