from room import Room
from player import Player
from item import Item, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
False),
}

# Declare all items

items = {
    "shield": Item("Shield", "Protecting players from attack"),
    "gold": Item("Gold", "Provide a mean of trade for player"),
    "spear": Item("Spear", "Allowing player to attack opponent"),
    "puppy": Item("Puppy", "Totally useless"),
    "lamp": LightSource("Lamp", "Providing light source for player"),
    "redbull": Item("RedBull", "Energy drink")
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

# scatter items to rooms
room['foyer'].addItem(items['puppy'])
room['overlook'].addItem(items['lamp'])
room['narrow'].addItem(items['spear'])
room['treasure'].addItem(items['gold'])
room['overlook'].addItem(items['shield'])
room['narrow'].addItem(items['redbull'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def move_player(player, direction):
    if direction == "e" and player.current_room.e_to:
        player.current_room = player.current_room.e_to
        player.score += 1
        return True
    elif direction == "w" and player.current_room.w_to:
        player.current_room = player.current_room.w_to
        player.score += 1
        return True
    elif direction == "n" and player.current_room.n_to:
        player.current_room = player.current_room.n_to
        player.score += 1
        return True
    elif direction == "s" and player.current_room.s_to:
        player.current_room = player.current_room.s_to
        player.score += 1
        return True
    player.score -= 1
    return False


def move_item(player, input):
    input_arr = input.split(' ')
    if input == "i" or input == "inventory":
        print(f"---\n{len(player.items)} item(s) on hand")
        for item in player.items:
            print(f"{item.name}")
        print("---")
    elif input == "score":
        print(f"---\nYour score is {player.score}\n---")
    elif input_arr[1]: 
        if input_arr[0] == "take":
            if input_arr[1].lower() in items and items[input_arr[1].lower()] in player.current_room.items:
                player.addItem(items[input_arr[1].lower()])
                player.current_room.removeItem(items[input_arr[1].lower()])
                items[input_arr[1].lower()].on_take()
            else: 
                print(f"{input_arr[1]} is not in this room\n\n---")
        if input_arr[0] == "drop":
            if input_arr[1].lower() in items and items[input_arr[1].lower()] in player.items:
                player.dropItem(items[input_arr[1].lower()])
                player.current_room.addItem(items[input_arr[1].lower()])
                items[input_arr[1].lower()].on_drop()
            else:
                print(f"You do not have {input_arr[1]}\n\n---")
    else:
        print("Invalid input.")            


def start_game(name, room_name):
    _player = Player(name, room[room_name])
    dir_input = ['s', 'e', 'n', 'w']
    item_input = ['take', 'drop', 'i', 'inventory', 'score']
    print(f"---\n\n{name}, you have successfully entered '{_player.current_room.name}'\n{_player.current_room.description}\n\n")
    
    if _player.current_room.is_light or items['lamp'] in _player.items or items['lamp'] in _player.current_room.items:
        print(f"There are {len(_player.current_room.items)} item(s) in this room\n")
        for i in range(0, len(_player.current_room.items)) :
            print(f"Item {i+1}: {_player.current_room.items[i].name}\n")    
        print("---")
    else:
        print("This room is pitch black\n---")
    
       
    print("\nValid Commands: n, e, w, s, i, inventory, score, take, drop, and name of the item\n")

    while _player.status:
        user_input = input("\nWhat would you like to do? ")
        input_arr = user_input.split(" ")
        if user_input == "q": _player.status = False

        elif user_input in dir_input and move_player(_player, user_input): 
            print(f"---\nYou've entered {_player.current_room.name}\n{_player.current_room.description}")
            if _player.current_room.is_light or items['lamp'] in _player.items or items['lamp'] in _player.current_room.items:
                print(f"There are {len(_player.current_room.items)} item(s) in this room\n")
                for i in range(0, len(_player.current_room.items)) :
                    print(f"Item {i+1}: {_player.current_room.items[i].name}\n")    
                print("---")
            else:
                print(f"It is pitch black in here!\n---")
        elif input_arr[0] in item_input:
            move_item(_player, user_input)
        else:
            print(f"THAT'S NOT A VALID MOVE! \n---")


player_name = input("Enter the player's name: ")
start_game(player_name, 'outside')


