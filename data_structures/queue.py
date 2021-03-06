from data_structures.linked_list.doubly import DoublyLinkedList


class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()

    @property
    def is_empty(self):
        return self.list.is_empty

    def add(self, data):
        self.list.insert_at_begining(data)

    def remove(self):
        if self.is_empty:
            raise EmptyQueueException()
        return self.list.remove_node(self.list.last).data

    def __repr__(self):
        return repr(self.list)


class EmptyQueueException(Exception):
    pass
