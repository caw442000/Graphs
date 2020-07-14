"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        pass  # TODO
        if vertex_id in self.vertices:
            return
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our queue isn't empty
        while q.size() > 0:
        ## dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
        ## if we haven't visited this node yet,
            if current_node not in visited:
        ### mark as visited
                visited.add(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors,
                for neighbor in neighbors:
        #### add to queue
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
        # make a stack
        s= Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our stack isn't empty
        while s.size() > 0:
        ## pop off whatever's on top, this is current_node
            current_node = s.pop()
            ## if we haven't visited this vertex before
            if current_node not in visited:
            ### run function / print
                print(current_node)
                ### mark as visited
                visited.add(current_node)
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors
                for neighbor in neighbors:
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # recursion does the stack stuff for us
        # if visited is None initialize it
        # print starting vertex
        print(starting_vertex)

        # grab neighbors
        neighbors = self.get_neighbors(starting_vertex)
        # if visited tracking set not passed and = None 

        # add current to visited set
        visited.add(starting_vertex)

        # for each neighbor
        # if it is not visited 
        # recure on the neighbors
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue
        q = Queue()
        # enqueue path to the starting vertex
        q.enqueue([starting_vertex])
        # create a set to track vertices we have visited
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            current_path = q.dequeue()
            # get last vertex from the path
            last_vertex = current_path[-1]
            # if vertex has not been visited:
            if last_vertex not in visited:
                # check the destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark is as visited
                visited.add(last_vertex)
                # add a path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:
                    # clone path
                    path_copy = list(current_path)
                # add neighbor to the back of the queue
                    path_copy.append(v)
                    q.enqueue(path_copy)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack
        stack = Stack()
        # push the starting_vertex onto the stack
        stack.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty
        while stack.size() > 0:
            # dequeue the first path
            current_path = stack.pop()
            # get the last vertex from the path
            last_vertex = current_path[-1]
            # it has not been visited:
            if last_vertex not in visited:
                # check destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark it as visited
                visited.add(last_vertex)
                # add path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:

                    # clone path
                    path_copy = list(current_path)

                # add neighbor to the back of the queue
                    path_copy.append(v)
                    stack.push(path_copy)

    def dfs_recursive(self, vertex, destination_vertex, path =[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # mark our node as visited
        visited.add(vertex)
        
        # check if it is our target node, if so return
        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)


        # iterate over neighbors
        neighbors = self.get_neighbors(vertex)

        # check if visited
        for neighbor in neighbors:
            if neighbor not in visited:


        # if not recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        # if this recursion returns a path
                if result is not None:
        # return from here
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
