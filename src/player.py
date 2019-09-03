# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, name):
        self.room = room
        self.name = name
    def __str__(self):
        return "Where am I: {self.room.roomName}, Name: {self.name}".format(self=self)

    