# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, desc):
        self.roomName = roomName
        self.desc = desc 
        self.items = []

    def __str__(self):
        return "Room Name: {self.roomName}, Description: {self.desc}".format(self=self)

    def addItem(self, item):
        self.items.append(item)
    
    def dropItem(self, item):
        self.items.remove(item)