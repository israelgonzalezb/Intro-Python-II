# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room

    def talk(self):
        print(f"Hello! I'm in {self.room}")