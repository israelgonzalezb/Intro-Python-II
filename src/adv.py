from room import Room
from player import Player
from item import Item

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

# Declare all the items

items = {
    "coins": Item("coins", "A pile of dirty gold coins.")
}

# Links items to rooms
room['narrow'].items = [items['coins']]

# For stretch, maybe a distinct map can be added as a property of each room, for example room['treasure'].map
map = """
               N
      overlook ____________
    |          | treasure |
  W |          |          | E
    |  foyer      narrow  |
    |          ------------
    | outside  |
               S
"""

#
# Main
#

# ✓ Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# ✓ Prints the current room name
# ✓ Prints the current description (the textwrap module might be useful here).
# ✓ Waits for user input and decides what to do.
#
# ✓ If the user enters a cardinal direction, attempt to move to the room there.
# ✓ Print an error message if the movement isn't allowed.
#
# ✓ If the user enters "q", quit the game.

# Stretch:
# ✓ If the user enters "m", show the map.
# If the user enters "m", show the map and the user's place on the map.
#

# print(f"!!! {room['outside'].n_to}") # !!! Foyer
# print(f"??? {room['outside'].__dict__}")
# print(f"User's room is {player.room}") # User's room is foyer
# print(f"North room adjacent key name is {room[player.room].__dict__.items()}") # North room adjacent key name is dict_items([('room', 'Foyer'), ('description', 'Dim light filters in from the south. Dusty\npassages run north and east.'), ('s_to', <room.Room object at 0x10ab220d0>), ('n_to', <room.Room object at 0x10ab22550>), ('e_to', <room.Room object at 0x10ab22390>)])
# print(f"North room adjacent key name is {list(room[player.room].__dict__.items())}") # North room adjacent key name is [('room', 'Foyer'), ('description', 'Dim light filters in from the south. Dusty\npassages run north and east.'), ('s_to', <room.Room object at 0x10b255110>), ('n_to', <room.Room object at 0x10b255590>), ('e_to', <room.Room object at 0x10b2553d0>)]
# player.room = "narrow"
# print(f"room[player.room].n_to.room is {room[player.room].n_to.room}") # room[player.room].n_to.room is Grand Overlook
# print(f"room[player.room].n_to.__dict__.keys() is {room[player.room].n_to.__dict__.keys()}") # room[player.room].n_to.keys() is dict_keys(['room', 'description', 's_to'])

print("\n")
print('{:s}'.format('\u0332'.join('IZZY\'S LAMBDA ADVENTURE')))
print("\nPress h for help\n")
user_name = input("Hello adventurer. What is your name?\n>> ")
player = Player(room["outside"], user_name)
print(f"Welcome {user_name}. Safe travels.\n")
while True:
    print(f'\nYou are at the {player.room}')
    try:
        print("You see:\n")
        [print(f"   {i}: {val}") for i, val in enumerate(player.room.items)]
    except AttributeError:
        pass
    user_input = input("\nChoose a direction to continue...\n>> ")
    if user_input == "q":
        print("\nA tunnel of sparkling light erupts from beneath your feet and whisks you away...\n")
        break
    if user_input == "n":
        try:
            player.room = player.room.n_to
        except AttributeError:
            if player.room.room_name == "Grand Overlook":
                print("\nYou stare into the abyss, and the abyss stares back. You decide not to attempt to cross the chasm.")
            elif player.room.room_name == "Treasure Chamber":
                print("\nYou look at the wall in front of you. The rat in the corner hisses and scurries away.")
    if user_input == "s":
        try:
            player.room = player.room.s_to
        except AttributeError:
            if player.room.room_name == "Outside Cave Entrance":
                print("\nYou're already outside. You can't be anymore outside!")
            elif player.room.room_name == "Narrow Passage":
                print("\nYou look at the southernmost wall of the passage. You notice etchings in a strange language. It reads ⟟⋔⌿⍜⍀⏁ ⏃⋏⏁⟟☌⍀⏃⎐⟟⏁⊬")
    if user_input == "w":
        try:
            player.room = player.room.w_to
        except AttributeError:
            if player.room.room_name == "Grand Overlook":
                print("\nIn the distance to the west, the sky is covered in glowing ash.")
            elif player.room.room_name == "Treasure Chamber":
                print("\nThe wall to the west is stained with liquid oozing from the ceiling.")
            elif player.room.room_name == "Outside Cave Entrance":
                print("\nA large boulder blocks your path.")
            elif player.room.room_name == "Foyer":
                print("\nStalactites hang from the ceiling.")
    if user_input == "e":
        try:
            player.room = player.room.e_to
        except AttributeError:
            if player.room.room_name == "Narrow Passage":
                print("\nYou look through a crevice in the wall. You see a far away village burning.")
            elif player.room.room_name == "Outside Cave Entrance":
                print("\nA pile of rotting, burnt felled trees lies to the east.")
            elif player.room.room_name == "Treasure Chamber":
                print("\nThe eastern wall is hot to the touch.")
            if player.room.room_name == "Grand Overlook":
                print("\nTo the east smoke billows from a distant village.")
    if user_input == "m":
        print("\n"+map+"\n")
            