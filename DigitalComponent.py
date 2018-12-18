import random
from click_button import *
from input import *
from local_variables import *

pygame.init()

def background():
    gamemap = pygame.image.load(os.path.join(image_path, 'map-blur.jpg'))
    gamemap = pygame.transform.scale(gamemap,(display_width,display_height))
    gameDisplay.blit(gamemap, (0,0))


def logo(x,y):
    logoImg = pygame.image.load(os.path.join(image_path, 'logo.png'))
    logoImg = pygame.transform.scale(logoImg, (int(display_height/2),int(display_width/2.66)))
    gameDisplay.blit(logoImg, (x,y))


def exit():
    pygame.quit()
    quit()


def start_screen():

    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exit()

        background()
        logo(display_width * 0.31, display_height * 0.1)

        # # title
        # TextSurf, TextRectangle = textblock("Turf Wars", LARGE_FONT)
        # TextRectangle.center = ((display_width / 2),((display_height *0.5)))
        # gameDisplay.blit(TextSurf, TextRectangle)

        #buttons
        button('Start',150,550,300,150,bright_blue,blue,playerinput_screen)
        button('Exit', 550,550,300,150,red,bright_red,exit)

        pygame.display.update()
        clock.tick(15)

def player_amount_screen():
    background()


def playerinput_screen():
    gameDisplay.fill(white)
    gameExit = False
    fpsclock = pygame.time.Clock()
    fps = 30
    global PurplePlayer
    global RedPlayer
    global GreenPlayer
    global BlackPlayer

    while not gameExit:
        fpsclock.tick(fps)
        pressed = None
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                print(pygame.key.name(event.key))
                print(ord(pygame.key.name(event.key)))
            if event.type == pygame.QUIT:
                exit()

        background()

        if not PurplePlayer:
            PurplePlayer = enter_text(15)

        pygame.draw.rect(gameDisplay, purple, (120,500,150,40))
        print_text(TINY_FONT, 130, 505, PurplePlayer, white)

        if not RedPlayer:
            RedPlayer = enter_text(15)
        pygame.draw.rect(gameDisplay, red, (320,500,150,40))
        print_text(TINY_FONT, 330, 505, RedPlayer, white)

        if not GreenPlayer:
            GreenPlayer = enter_text(15)
        pygame.draw.rect(gameDisplay, green, (520,500,150,40))
        print_text(TINY_FONT, 530, 505, GreenPlayer, white)

        if not BlackPlayer:
            BlackPlayer = enter_text(15)

        background()

        playerText = "Player 1:"

        print_text(TINY_FONT, 725, 470, "Player 4:", black)
        pygame.draw.rect(gameDisplay, black, (720,500,150,40))
        print_text(TINY_FONT, 730, 505, BlackPlayer, white)

        print_text(TINY_FONT, 325, 470, "Player 2:", black)
        pygame.draw.rect(gameDisplay, red, (320,500,150,40))
        print_text(TINY_FONT, 330, 505, RedPlayer, white)

        print_text(TINY_FONT, 125, 470, "Player 1:", black)
        pygame.draw.rect(gameDisplay, purple, (120,500,150,40))
        print_text(TINY_FONT, 130, 505, PurplePlayer, white)

        print_text(TINY_FONT, 525, 470, "Player 3:", black)
        pygame.draw.rect(gameDisplay, green, (520,500,150,40))
        print_text(TINY_FONT, 530, 505, GreenPlayer, white)

        button('Proceed',350,250,300,150,bright_green,green,gamescreen_3)

        pygame.display.update()
        clock.tick(15)


def resource_counter():

    # TODO: Store the values per player so they can be remembered and used again.
    # TODO: Add + & - buttons for adding and subtracting resources (instead of typing).

    # Defining the variables
    global turns
    global current_player
    current_player = 1
    global player_resources
    player_resources = 0
    global current_player_name
    current_player_name = 0
    global yellow_amount
    global orange_amount
    global blue_amount
    global red_amount

    while current_player <= 4:

        if current_player == 1:
            current_player_name = PurplePlayer
        elif current_player == 2:
            current_player_name = RedPlayer
        elif current_player == 3:
            current_player_name = GreenPlayer
        elif current_player == 4:
            current_player_name = BlackPlayer

        # Let the user input the amount of land they own
        yellow_amount = enter_resources(2, "yellow", str(current_player_name))
        background()
        orange_amount = enter_resources(2, "orange", str(current_player_name))
        background()
        blue_amount = enter_resources(2, "blue", str(current_player_name))
        background()
        red_amount = enter_resources(2, "red", str(current_player_name))
        background()

        # Calculates the amount of land and multiplies it with the value of the land
        yellow = int(yellow_amount) * 1
        orange = int(orange_amount) * 2
        blue = int(blue_amount) * 3
        red = int(red_amount) * 4

        # Counts up the four given values
        player_resources = player_resources + yellow + orange + blue + red
        background()
        print_text(SMALL_FONT, 250, 470, "Player " + str(current_player_name) + " gets " + str(player_resources) + " resources.", white)

        # Continues to the next player and puts the playerResources on zero
        current_player = current_player + 1

        player_resources = 0

    # Resets the loop
    current_player = 1
    turns = turns + 1
    print_text(SMALL_FONT, 825, 675, "Turns: " + str(turns), white)


def gamescreen_3():
    start = True
    background()

    # 'Hardcore Mode'
    hardcore_setting = False
    hardcore_color = red
    event_list = ['You gain 1 resource', 'You gain 3 resources', 'You gain 5 resources',
                  'You lose 1 resource', 'You lose 3 resources', 'You lose 5 resources',
                  'You gain 1 troop', 'You gain 3 troops', 'You gain 5 troops',
                  'You lose 1 troop', 'You lose 3 troops', 'You lose 5 troops']
    event_msg = random.choice(event_list)
    event_active = False

    while start:

        resource_counter()

        # 'Hardcore Mode'
        hardcore_state = TINY_FONT.render(str(hardcore_setting), True, white)   # True / False Text
        hardcore_txt = TINY_FONT.render('Hardcore mode:', True, white)          # Hardcore mode Text
        event_txt = TINY_FONT.render(event_msg, True, black)                    # Random Events Text
        event_button_txt = TINY_FONT.render("Random Event", True, white)        # Event Button Text

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 'Hardcore Mode'
                if hardcore_button.collidepoint(event.pos):     # If hardcore button is clicked
                    background()                    # Refill background to white before redrawing
                    hardcore_setting = not hardcore_setting     # Toggle hardcore_setting between True / False
                    if hardcore_setting:                        # if True
                        hardcore_color = (0, 255, 0)            # Green
                    else:                                       # Else
                        hardcore_color = red                    # Red

                elif event_button.collidepoint(event.pos) and not event_active:                 # If event button is clicked and an event is not already open
                    event_active = True                                                         # Set event active to true
                    background()                                                  			   # Refill background before redrawing
                    event_msg = random.choice(event_list)                                       # Get a random event from event list
                    pygame.draw.rect(gameDisplay, (50, 100, 100), event_background)             # Draw event background
                    pygame.draw.rect(gameDisplay, (30, 30, 30), event_close)                    # Draw event closing button
                    pygame.draw.line(gameDisplay, red, (event_close.x, event_close.y),          # Draw event closing button cross
                                     (event_close.x + 28, event_close.y + 28), 2)
                    pygame.draw.line(gameDisplay, red, (event_close.x, event_close.y+28),
                                     (event_close.x + 28, event_close.y), 2)
                    gameDisplay.blit(event_txt, (event_background.x+10, event_background.y+5))  # Blit random event text

                elif event_close.collidepoint(event.pos):                                       # If event closing button is clicked
                    event_active = False                                                        # Set event active to false
                    background()                    			                                # Reset board

        # 'Hardcore Mode'
        hardcore_button = pygame.Rect(890, 30, 60, 30)                                         # The "button" rect
        hardcore_bg = pygame.Rect(hardcore_button.x - 160, hardcore_button.y - 5,              # Background rect, scaled to button rect
                                  hardcore_button.width + 170, hardcore_button.height + 10)
        pygame.draw.rect(gameDisplay, black, hardcore_bg)                                      # Draw background
        pygame.draw.rect(gameDisplay, hardcore_color, hardcore_button)                         # Draw button
        gameDisplay.blit(hardcore_state, (hardcore_button.x + 5, hardcore_button.y))           # Blit button state, position relative to button rect
        gameDisplay.blit(hardcore_txt, (hardcore_button.x - 150, hardcore_button.y))           # Blit hardcore mode text, left of button rect


        # Events
        event_button = pygame.Rect(hardcore_button.x - 160, hardcore_button.y + 50,            # Event button
                                   hardcore_button.width + 170, hardcore_button.height + 10)
        event_background = pygame.Rect(display_width/4, display_height/4,                      # Event background
                                   hardcore_button.width + 270, hardcore_button.height + 100)
        event_close = pygame.Rect(event_background.x + event_background.width - 30,            # Event closing button
                                  event_background.y, 30, 30)

        if hardcore_setting:                                                                   # If hardcore is set to True
            pygame.draw.rect(gameDisplay, (50, 130, 130), event_button)                        # Draw event button
            gameDisplay.blit(event_button_txt, (event_button.x + 10, event_button.y + 5))      # Blit event button text

        pygame.display.update()
        clock.tick(15)


start_screen()


exit()
