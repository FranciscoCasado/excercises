from linked_list import LinkedList, Node


class Stack:
    def __init__(self):
        self.list = LinkedList()

    @property
    def is_empty(self):
        return self.list.is_empty

    def push(self, data):
        self.list.insert_at_end(data)

    def pop(self):
        if self.is_empty:
            raise EmptyStackException()
        return self.list.remove_node(self.list.last).data

    def peek(self):
        if self.is_empty:
            raise EmptyStackException()
        return self.list.last.data

    def __repr__(self):
        return repr(self.list)


class EmptyStackException(Exception):
    pass
