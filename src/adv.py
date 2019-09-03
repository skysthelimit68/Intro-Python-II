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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(room["outside"], "Hannah")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.



def displayPlayer(player):
    print(f"Your current location: {player.room.roomName}")
    print(player.room.desc)
    print("### ### ### ### ### ###")
    dir = input("Where would you like to go? ")

    playerMove(player, dir)


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
            dir = input("Where would you like to go? ")
            playerMove(player, dir)


displayPlayer(player1)

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
