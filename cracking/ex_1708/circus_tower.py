class Node:
    def __init__(self, data=(0,0), height=1,parent=None, children=None):
        self.data = data
        self.parent = parent
        self.children = []
        self.tower_height = height

    def append_child(self, new_child):
        new_child.tower_height += self.tower_height
        new_child.parent = self
        self.children.append(new_child)

    def __le__(self, other):
        return (self.data[0] <= other.data[0]) and (self.data[1] <= other.data[1]) 
    
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

        candidates = []
        for child in self.leaves:
            current = child
            print(f"{current}:{new_child}")
            while current.parent:
                if current <= new_child:
                    break
                current = current.parent
            candidates.append(current)

        best = candidates[0]
        for candidate in candidates:
            best = candidate if candidate.tower_height >= best.tower_height else best
        
        best.append_child(new_child)
        self.leaves.append(new_child)
        if best in self.leaves:
            self.leaves.remove(best)


def largest_tower(people: list):
    tower_height = 0
    people.sort()
    nodes = [Node(person) for person in people]
    tree = Tree(Node(height=0))
    
    for node in nodes:
        tree.add_child(node)
        tower_height = max(node.tower_height, tower_height)
    
    return tower_height