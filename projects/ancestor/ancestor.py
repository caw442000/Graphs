from util import Queue, Stack



def earliest_ancestor(ancestors, starting_node):
    # queue of current nodes
    s = Stack()
    # add first node to path set
    path = [starting_node]
    s.push(path)

    visited = set()
    

    while s.size() > 0:
        # pop off the first path
        current_path = s.pop()
        path_copy = []
        print(current_path)
        last_vertex = current_path[-1]
        

        # grab the last item in the current path 
        # this is equivalent of last visited vertix that would have been in a set
        # if len(current_path) != 0:
        #     furthest_ancestor = current_path[-1]
        # # print(furthest_ancestor)

        # if furthest_ancestor not in visited:

        #     visited.add(furthest_ancestor)
        #     print(furthest_ancestor)

        parent_added = False
        # look into each ancestors connection
        parents = []

        for node in current_path: 
                for family in ancestors:
                    # if the child (family[1]) is the child we are looking for
                    # add the parent to the list
                    
                    if family[1] == node:
                        parent_added = True
                        if family not in visited:
                            parents.append(family[0])
                            print(family[0])
                            visited.add(family)
                
                    
                    

        # fixes issue with outputting lowest number if 2 parents are at same letter
        # sorts the parents numbers in descending order so that 
        # lower number is appended to the copy list last so it is pushed on last as well
        if parent_added:
            parents.sort(reverse=True)       
            # add parents in for loop
            for parent in parents:
                # if parent not in visited:
                path_copy.append(parent)
                
            s.push(path_copy)

                
                
                
        # when we get this far we are as far as we can go 
        # no parents added 
        if parent_added is False:
            # makes sure if there is no ancestors it returns -1
            if current_path[0] == starting_node:
                return -1
            else:
                
                return last_vertex


test_ancestors = [(19, 22), (15, 22), (22, 2), (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (11, 8), (8, 9), (4, 8), (10, 1)]


print(earliest_ancestor(test_ancestors, 9))


