# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, light):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.is_light = light

    def __str__(self):
        return f"Room Name: {self.name}, Description: {self.description}, Items: {self.items}"

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        if item in self.items: self.items.remove(item)
