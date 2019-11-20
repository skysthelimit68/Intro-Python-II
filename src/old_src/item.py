
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return "Name of the item: {self.name}, Description of the item: {self.description}".format(self=self)