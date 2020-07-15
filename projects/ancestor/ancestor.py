from util import Queue, Stack
# Understood

# Plan
## Graphs Problem Solving
### Translate the problem
#### Nodes: people
#### Edges: when a child has a parent

### build our graph, or just define get_neighors
#### 

### Choose algorithm
#### Either BFS or DFS
#### DFS
##### How would we know if DFS happened to be faster?

# import deque from collections


# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighors(self, vertex):
        return self.vertices[vertex]

## Build a path like we did in search
## But we don't know when to stop until we've seen everyone
def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph

def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()

    visited = set()

    s.push([starting_node])

    longest_path = [starting_node]
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        # if path is longer, or path is equal but the id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)

    return aged_one


# def earliest_ancestor(ancestors, starting_node):
#     # queue of current nodes
#     s = Stack()
#     # add first node to path set
#     path = [starting_node]
#     s.push(path)

#     visited = set()
    

#     while s.size() > 0:
#         # pop off the first path
#         current_path = s.pop()
#         path_copy = []
#         print(current_path)
#         last_vertex = current_path[-1]


#         parent_added = False
#         # look into each ancestors connection
#         parents = []

#         for node in current_path: 
#                 for family in ancestors:
#                     # if the child (family[1]) is the child we are looking for
#                     # add the parent to the list
                    
#                     if family[1] == node:
#                         parent_added = True
#                         if family not in visited:
#                             parents.append(family[0])
#                             print(family[0])
#                             visited.add(family)

#         # fixes issue with outputting lowest number if 2 parents are at same letter
#         # sorts the parents numbers in descending order so that 
#         # lower number is appended to the copy list last so it is pushed on last as well
#         if parent_added:
#             parents.sort(reverse=True)       
#             # add parents in for loop
#             for parent in parents:
#                 # if parent not in visited:
#                 path_copy.append(parent)
                
#             s.push(path_copy)
        
#         # when we get this far we are as far as we can go 
#         # no parents added 
#         else:
#             # makes sure if there is no ancestors it returns -1
#             if current_path[0] == starting_node:
#                 return -1
#             else:
                
#                 return last_vertex


test_ancestors = [(19, 22), (15, 22), (22, 2), (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (11, 8), (8, 9), (4, 8), (10, 1)]


print(earliest_ancestor(test_ancestors, 6))


