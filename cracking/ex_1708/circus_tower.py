class Node:
    def __init__(self, data=(0, 0), height=1, parent=None, children=None):
        self.data = data
        self.parent = parent
        self.children = []
        self.height = height

    def append_child(self, new_child):
        new_child.height += self.height
        new_child.parent = self
        self.children.append(new_child)

    def __le__(self, other):
        return (self.data[0] <= other.data[0]) and (self.data[1] <= other.data[1])

    def __ge__(self, other):
        return (self.data[0] >= other.data[0]) and (self.data[1] >= other.data[1])

    def __repr__(self):
        return str(self.data)


class Tree:
    def __init__(self, root):
        self.root = root
        self.leaves = []

    def add_child(self, new_child):
        if not self.leaves:
            self.root.append_child(new_child)
            self.leaves.append(new_child)
            return
        spot = self._find_best_spot_for_new_child(new_child)
        self._append_new_child(spot, new_child)

    def _find_best_spot_for_new_child(self, new_child):
        best = self.root
        for child in self.leaves:
            current = child
            while current.parent:
                if current <= new_child:
                    break
                current = current.parent
            best = current if current.height >= best.height else best

        return best

    def _append_new_child(self, spot, new_child):
        spot.append_child(new_child)
        self.leaves.append(new_child)
        if spot in self.leaves:
            self.leaves.remove(spot)

    def largest_branch(self):
        largest = self.root
        for leaf in self.leaves:
            largest = leaf if leaf.height >= self.root.height else largest
        return largest


def largest_tower(people: list) -> list:
    tower_height = 0
    people.sort()
    nodes = [Node(person) for person in people]
    tree = Tree(Node(height=0))

    for node in nodes:
        tree.add_child(node)

    return tree.largest_branch()
