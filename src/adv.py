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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room["outside"], "Hannah")

items = {
    'toy' : Item("Toy", "A small playful thing for a child"),
    'weapon' : Item("Weapon", "A large item that can cause some harm"),
    'shield' : Item("Shield", "A large item that can protect player")
}

#initial set up to add items to rooms
room['foyer'].addItem('toy')
room['overlook'].addItem('weapon')
room['overlook'].addItem('shield')
room['narrow'].addItem('toy')
room['narrow'].addItem('weapon')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


def displayPlayer(player):
   
        print(f"My current location: {player.room.roomName}")
        print(player.room.desc)
        for i in player.room.items:
            print(f"Item in this room: {i}")
        print("### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###")

        #verb would be go, take and drop
        intent = input("What would you like to do? #take #drop #n #w #s #e #q ").split(' ')
        print(intent)
        if len(intent) == 1:
            if intent[0].lower() == "i":
                for i in player.items:
                    print(f"Inventory: {i}")
                displayPlayer(player)
            elif intent[0].lower() != "q":
                playerMove(player, intent[0])
        elif len(intent) == 2:
            itemCollection(player, intent[0], intent[1])


def itemCollection(player, action, item):
    if item in player.room.items and action == "take":
        player.addItem(item)
        player.room.dropItem(item)
        print(f"You just picked up a {item}")
        print("### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###")

        displayPlayer(player)
    
    elif item in player.items and action == "drop":
        player.dropItem(item)
        player.room.addItem(item)
        print(f"You just dropped a {item}")
        print("### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###")

        displayPlayer(player)
    else:
        print(f"You cannot {action} {item}")
        displayPlayer(player)


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

def playerMove(player, dir):
        try:
            if dir.upper() == "N" and hasattr(player.room, 'n_to'):
                player.room = player.room.n_to
            elif dir.upper() =="S" and hasattr(player.room, 's_to'):
                player.room = player.room.s_to
            elif dir.upper() == "W" and hasattr(player.room, 'w_to'):
                player.room = player.room.w_to
            elif dir.upper() == "E" and hasattr(player.room, 'e_to'):
                player.room = player.room.e_to
            else:
                print('Wrong Move! You hit a wall! Remember to use "N", "S", "W", or "E" for direction.')
            
            displayPlayer(player)

        except:
            print('Wrong Move!!! Do you know where you want to go? Type in the direction using "N", "S", "W", or "E" or else you will hit a wall or fall off a cliff!')
            displayPlayer(player)

displayPlayer(player1)

# If the user enters "q", quit the game.
