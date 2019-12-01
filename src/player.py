# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.score = 0
        self.status = True

    def __str__(self):
        return f"Current Room: {self.current_room.name}, Name: {self.name}, Items on hand: {self.items}"

    def addItem(self, item):
        self.items.append(item)


    def dropItem(self, item):
        if item in self.items: self.items.remove(item)
