def count_resources():

    # TODO: Build a while loop which keeps going if the game is active
    # TODO: Add a turn counter in the game loop
    # TODO: Store the values per player so they can be remembered and used again.
    # TODO: Make the amount of players variable
    # TODO: Show the names filled in at the beginning

    # Defining the variables
    global current_player
    current_player = 1
    player_resources = 0

    while current_player <= 4:

        # Let the user input the amount of land they own
        print('The amount of yellow land player ' + str(current_player) + ' owns:')
        yellow_amount = input()
        print('The amount of orange land player ' + str(current_player) + ' owns:')
        orange_amount = input()
        print('The amount of blue land player ' + str(current_player) + ' owns:')
        blue_amount = input()
        print('The amount of red land player ' + str(current_player) + ' owns:')
        red_amount = input()

        # Calculates the amount of land and multiplies it with the value of the land
        yellow = int(yellow_amount) * 1
        orange = int(orange_amount) * 2
        blue = int(blue_amount) * 3
        red = int(red_amount) * 4

        # Counts up the four given values
        player_resources = player_resources + yellow + orange + blue + red
        print('Player ' + str(current_player) + ' gets ' + str(player_resources) + ' resources')

        # Continues to the next player and puts the playerResources on zero
        current_player = current_player + 1

        player_resources = 0

    # Resets the loop
    current_player = 1