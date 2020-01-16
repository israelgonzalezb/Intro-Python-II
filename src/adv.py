from room import Room
from player import Player

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


"""
        overlook | treasure
          |           |
        foyer   -  narrow
          |
        outside
"""

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# ✓ Prints the current room name
# ✓ Prints the current description (the textwrap module might be useful here).
# ✓ Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# ✓ If the user enters "q", quit the game.


player = Player(room["outside"])

# print(f"!!! {room['outside'].n_to}") # !!! Foyer
# print(f"??? {room['outside'].__dict__}")
# print(f"User's room is {player.room}") # User's room is foyer
# print(f"North room adjacent key name is {room[player.room].__dict__.items()}") # North room adjacent key name is dict_items([('room', 'Foyer'), ('description', 'Dim light filters in from the south. Dusty\npassages run north and east.'), ('s_to', <room.Room object at 0x10ab220d0>), ('n_to', <room.Room object at 0x10ab22550>), ('e_to', <room.Room object at 0x10ab22390>)])
# print(f"North room adjacent key name is {list(room[player.room].__dict__.items())}") # North room adjacent key name is [('room', 'Foyer'), ('description', 'Dim light filters in from the south. Dusty\npassages run north and east.'), ('s_to', <room.Room object at 0x10b255110>), ('n_to', <room.Room object at 0x10b255590>), ('e_to', <room.Room object at 0x10b2553d0>)]
# player.room = "narrow"
# print(f"room[player.room].n_to.room is {room[player.room].n_to.room}") # room[player.room].n_to.room is Grand Overlook
# print(f"room[player.room].n_to.__dict__.keys() is {room[player.room].n_to.__dict__.keys()}") # room[player.room].n_to.keys() is dict_keys(['room', 'description', 's_to'])

print(f"Player.room: {player.room.room_name}")
while True:
    print(f'You are at the {player.room}')
    user_input = input("Choose a direction to continue\n")
    if user_input == "q":
        break
    if user_input == "n":
        try:
            player.room = player.room.n_to
        except AttributeError:
            if player.room.room_name == "Grand Overlook":
                print("You stare into the abyss, and the abyss stares back. You decide not to attempt to cross the chasm.")
            elif player.room.room_name == "treasure":
                print("You look at the wall in front of you. The rat in the corner hisses and scurries away.")
    if user_input == "s":
        try:
            player.room = player.room.s_to
        except AttributeError:
            if player.room.room_name == "Outside Cave Entrance":
                print("You're already outside. You can't be anymore outside!")
    if user_input == "w":
        break
    if user_input == "e":
        break
