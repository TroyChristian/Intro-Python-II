#CLASSES
class Room():
    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None 
        self.e_to = None
        self.w_to = None

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f'{direction}_to')
        return None 


class Player:
    def __init__(self, name:str, current_room:Room):
        self.name = name
        self.current_room = current_room 


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player = Player("Yelda", room['outside'])

running = True

while running:
    print(player.current_room.name)
    print(player.current_room.description)

    user_input = input("Where do you want to go? Enter a directional letter or q to quit: ")
    if user_input == "q":
        print("Thanks for playing, return soon!")
        running = False 

    
    else:
        next_room = player.current_room.get_room_in_direction(user_input)
        if next_room is None:
            print("There is no place to go in that direction")
        
        else:
            player.current_room = next_room 

    
    
