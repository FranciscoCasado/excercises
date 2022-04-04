
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def find(self, data):
        for child in self.children:
            if child.data == data:
                return child
        
        return None
        
    def __repr__(self):
        representation = str(self.data)
        
        if self.children:
            for child in self.children:
                representation = representation + repr(child)
        
        return representation
        
                
    def append(self, node):
        self.children.append(node)

class IndexTrie:
    def __init__(self):
        self.root = Node("> ")
    
    def insert(self, word):
        current = self.root
        for char in word:
            child = current.find(char)
            if not child:
                child = Node(char)
                current.append(child)
            current = child
            
    def __repr__(self):
        return repr(self.root)
        
        
                
            
            
        
        
        


def multisearch(long_string, smaller_strings):
    
    return True