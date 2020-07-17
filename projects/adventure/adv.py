from room import Room
from player import Player
from world import World



import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()



# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

move_backwards = {
  'n': 's', 
  's': 'n',
  'e': 'w',
  'w': 'e'
}


directions = Stack()

visited = {}



# loop until total visited is equal to total rooms in world
while len(visited) < len(world.rooms):

    # get the neighbors *** returns complete list 
    # will need to get rid of already visited directions later
    exits = player.current_room.get_exits()


    # will hold the possible exits that can be chosen from below
    # for the that will be pushed on the stack
    # this will reset it everytime
    
    path = []

    # shuffles the exits so that when it is chosen below it isn't the same

    random.shuffle(exits)
    # print(player.current_room.id)
    # print(exits)

    # print('starting path')
    # print(path)

    # loop through the exits
    for exit in exits:

        # grab next room that is in the exit direction
        next_room = player.current_room.get_room_in_direction(exit)
        # print(exit)
        # print(next_room.id)

        # this is to ensure to develop the nested dictionaries correctly
        # initializes if empty
        if visited.get(player.current_room.id) == None:
            visited[player.current_room.id]= {}
            # for loop to add ? to 
            for empty_exit in exits:
                visited[player.current_room.id][empty_exit] = '?'

        # id's the rooms so we can check if next room id is in visited
        # could probably use a set instead
        # originally was going a differnt direction
  

        # need to make sure that we filter the exits list to not include
        # any place we have been
        if next_room.id not in visited:
            # print(exit)
            path.append(exit)
            # print('visited')
            
            
        if exit =='n':
            visited[player.current_room.id][exit] = next_room.id
        if exit =='s':
            visited[player.current_room.id][exit] = next_room.id
        if exit =='e':
            visited[player.current_room.id][exit] = next_room.id
        if exit =='w':
            visited[player.current_room.id][exit] = next_room.id

        # print(visited)
            
    # this gives the choice of the available directions
    if len(path) > 0:

        # print('this is the path to choose from')
        # print(path)
        
        # print('path')
        # print(path)
        
        step = len(path) -1
        # print(step)
        # selects location in the path list to grab  the value and add to push
        directions.push(path[step])
        
        player.travel(path[step])
        # print(path[step])
        traversal_path.append(path[step])
        # print('traversal path')
        # print(traversal_path)
    
    else:
        dead_end = directions.pop()
        # print('dead end')
        # print(dead_end)
        player.travel(move_backwards[dead_end])
        if len(visited) != len(world.rooms):
            traversal_path.append(move_backwards[dead_end])
        # print(move_backwards[dead_end])
        # print(traversal_path)


result = any('?' in d.values() for d in visited.values())
print(result)


# def traversal_recursive(room = player.current_room, traversal_path = [], visited = {}):
#     print("traversal_path")
#     print(traversal_path)
#     if len(visited) == len(world.rooms):
#         return traversal_path

#     exits = player.current_room.get_exits()
#     path = []
#     random.shuffle(exits)

#     for exit in exits:
#         next_room = player.current_room.get_room_in_direction(exit)

#         if visited.get(player.current_room.id) == None:
#             visited[player.current_room.id]= {}
          
#             for empty_exit in exits:
#                 visited[player.current_room.id][empty_exit] = '?'
#         if next_room.id not in visited:
         
#             path.append(exit)
         
            
            
#         if exit =='n':
#             visited[player.current_room.id][exit] = next_room.id
#         if exit =='s':
#             visited[player.current_room.id][exit] = next_room.id
#         if exit =='e':
#             visited[player.current_room.id][exit] = next_room.id
#         if exit =='w':
#             visited[player.current_room.id][exit] = next_room.id

#     if len(path) > 0:
        
#         step = len(path) -1
#         directions.push(path[step])
        

#         traversal_path.append(path[step])
#         traversal_recursive( player.travel(path[step]), traversal_path, visited)
    
#     else:
#         dead_end = directions.pop()

#         player.travel(move_backwards[dead_end])

#         if len(visited) != len(world.rooms):
#             traversal_path.append(move_backwards[dead_end])
#         traversal_recursive(player.travel(move_backwards[dead_end]), traversal_path, visited)
    
    

# traversal_path = traversal_recursive()



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
