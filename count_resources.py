from local_variables import *


def resource_counter():

    # TODO: Build a while loop which keeps going if the game is active.
    # TODO: Add a turn counter in the game loop.
    # TODO: Store the values per player so they can be remembered and used again.
    # TODO: Make the amount of players variable.
    # TODO: Use the names that were filled in at the beginning.

    # Defining the variables
    global current_player
    current_player = 1
    global player_resources
    player_resources = 0
    global current_player_name
    current_player_name = 0

    if current_player == 1:
        current_player_name = BlackPlayer
    elif current_player == 2:
        current_player_name = RedPlayer
    elif current_player == 3:
        current_player_name = PurplePlayer
    elif current_player == 4:
        current_player_name = GreenPlayer

    while current_player <= 4:

        # Let the user input the amount of land they own
        print('The amount of yellow land ' + str(current_player_name) + ' owns:')
        global yellow_amount
        yellow_amount = input()
        print('The amount of orange land ' + str(current_player_name) + ' owns:')
        global orange_amount
        orange_amount = input()
        print('The amount of blue land ' + str(current_player_name) + ' owns:')
        global blue_amount
        blue_amount = input()
        print('The amount of red land ' + str(current_player_name) + ' owns:')
        global red_amount
        red_amount = input()

        # Calculates the amount of land and multiplies it with the value of the land
        yellow = int(yellow_amount) * 1
        orange = int(orange_amount) * 2
        blue = int(blue_amount) * 3
        red = int(red_amount) * 4

        # Counts up the four given values
        player_resources = player_resources + yellow + orange + blue + red
        print(str(current_player_name) + ' gets ' + str(player_resources) + ' resources')

        # Continues to the next player and puts the playerResources on zero
        current_player = current_player + 1

        player_resources = 0

    # Resets the loop
    current_player = 1
