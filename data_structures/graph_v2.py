from data_structures.stack import Stack
from data_structures.queue import Queue

class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = []
        if children:
            self.append(children)
            
    def append(self, children):
        if type(children) == self.__class__:
            # print(f"appending {children.data} to {self.data} ")
            self.children.append(children)
            return
        
        for child in children:
            self.children.append(child)
            
    def __repr__(self):
        return self.data

class Graph:
    
    def __init__(self, vertices: list, edges: list):
        self.vertices = dict()
        for vertex in vertices:
            self.vertices[vertex] = Node(vertex)
            
        self.edges = []
        for edge in edges:
            if (edge[0] not in vertices) or (edge[1] not in vertices):
                raise ValueError("Invalid Edge: vertex is not in the provided vertices list")
            
            start_vertex = self.vertices[edge[0]]
            end_vertex = self.vertices[edge[1]]
            start_vertex.append(end_vertex)
            self.edges.append(edge)
        
    def __contains__(self, vertex) -> bool:
        print(self.vertices)
        return vertex in self.vertices
        
    def breadth_first_search(self, start_vertex):
        visited = []
        distance_to = dict()
        frontier = Queue()
        frontier.add(self.vertices[start_vertex])
        visited.append(self.vertices[start_vertex].data)
        distance_to[self.vertices[start_vertex].data] = 0
        while not frontier.is_empty:
            current = frontier.remove()
            for child in current.children:
                if not child.data in visited:
                    frontier.add(child)
                    distance_to[child.data] = float('inf')
                    visited.append(child.data)
                distance_to[child.data] = min(distance_to[child.data], distance_to[current.data] + 1)
        
        return visited, distance_to

    def depth_first_search(self, start_vertex):
        visited = []
        distance_to = dict()
        frontier = Stack()
        frontier.push(self.vertices[start_vertex])
        visited.append(self.vertices[start_vertex].data)
        distance_to[self.vertices[start_vertex].data] = 0
        while not frontier.is_empty:
            current = frontier.pop()
            for child in current.children:
                if not child.data in visited:
                    frontier.push(child)
                    distance_to[child.data] = float('inf')
                    visited.append(child.data)
                distance_to[child.data] = min(distance_to[child.data], distance_to[current.data] + 1)
        
        return visited, distance_to
