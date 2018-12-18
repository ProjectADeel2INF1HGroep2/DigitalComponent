import random
from click_button import *
from input import *
from local_variables import *
from player_amount import *

pygame.init()
# Total resources for each player
total_resource_list = [0, 0, 0, 0]
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

def hardcoremode_toggle():
    global hardcore_setting
    hardcore_setting = True

def playerinput_screen():
    gameDisplay.fill(white)
    gameExit = False
    fpsclock = pygame.time.Clock()
    fps = 30
    global PurplePlayer
    global RedPlayer
    global GreenPlayer
    global BlackPlayer
    global hardcore_setting

    while not gameExit:
        fpsclock.tick(fps)
        pressed = None
        background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # Player Amount
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                global player_amount_num
                global player_amount_done
                # Check if Player Amount Boxes are clicked
                if startPlayer2.collidepoint(event.pos):  # If click event matches position of button 2
                    if not player_amount_num == 2:  # If player amount is not equal to 2
                        startPlayer2.y += 2  # Raise y by 2
                    if player_amount_num == 3:
                        startPlayer3.y -= 2
                    elif player_amount_num == 4:
                        startPlayer4.y -= 2
                    player_amount_num = 2
                elif startPlayer3.collidepoint(event.pos):
                    if not player_amount_num == 3:
                        startPlayer3.y += 2
                    if player_amount_num == 2:
                        startPlayer2.y -= 2
                    elif player_amount_num == 4:
                        startPlayer4.y -= 2
                    player_amount_num = 3
                elif startPlayer4.collidepoint(event.pos):
                    if not player_amount_num == 4:
                        startPlayer4.y += 2
                    if player_amount_num == 2:
                        startPlayer2.y -= 2
                    elif player_amount_num == 3:
                        startPlayer3.y -= 2
                    player_amount_num = 4
                elif startPlayerContinue.collidepoint(event.pos):
                    player_amount_done = True
                    background()

        if not player_amount_done:
            # Starting Player Selection ==============================================
            pygame.draw.rect(gameDisplay, (30, 30, 30), startPlayerBgBorder)      # Player Amount Background Border
            pygame.draw.rect(gameDisplay, (220, 200, 80), startPlayerBackground)  # Player Amount Background Rect

            text_write("Select Player Amount", PA_font_mid, player_amount_x, player_amount_y - 25)  # Player Amount Text
            # Draw Selection Rects ===================================================
            pygame.draw.rect(gameDisplay, player_amount_shadow, startPlayerShadow)          # Shadow behind buttons

            pygame.draw.rect(gameDisplay, player_amount_color, startPlayer2)        # 2 Players Button Rect
            text_write("2", 30, startPlayer2.x + 5, startPlayer2.y + 9)             # 2 Players Text
            pygame.draw.rect(gameDisplay, player_amount_color, startPlayer3)        # 3 Players Button Rect
            text_write("3", 30, startPlayer3.x + 4, startPlayer3.y + 9)             # 3 Players Text
            pygame.draw.rect(gameDisplay, player_amount_color, startPlayer4)        # 4 Players Button Rect
            text_write("4", 30, startPlayer4.x + 3, startPlayer4.y + 9)             # 4 Players Text

            pygame.draw.rect(gameDisplay, player_amount_shadow, startPlayerContinueShadow)  # Continue Button Shadow
            pygame.draw.rect(gameDisplay, (50, 200, 50), startPlayerContinue)               # Continue Button
            text_write("Continue", PA_font_mid, startPlayerContinue.x + 4, startPlayerContinue.y + 8)  # Continue Text

            button('Hardcore Mode Toggle', 550,300,400,100,red,bright_red,hardcoremode_toggle)

        if player_amount_done:
            if not PurplePlayer:
                PurplePlayer = enter_text(15)

                pygame.draw.rect(gameDisplay, purple, (120,500,150,40))
                print_text(TINY_FONT, 130, 505, PurplePlayer, white)

            if not RedPlayer:
                RedPlayer = enter_text(15)
                pygame.draw.rect(gameDisplay, red, (320,500,150,40))
                print_text(TINY_FONT, 330, 505, RedPlayer, white)

            if not GreenPlayer and player_amount_num >= 3:
                GreenPlayer = enter_text(15)
                pygame.draw.rect(gameDisplay, green, (520,500,150,40))
                print_text(TINY_FONT, 530, 505, GreenPlayer, white)

            if not BlackPlayer and player_amount_num == 4:
                BlackPlayer = enter_text(15)

            background()

            playerText = "Player 1:"

            print_text(TINY_FONT, 125, 470, "Player 1:", black)
            pygame.draw.rect(gameDisplay, purple, (120,500,150,40))
            print_text(TINY_FONT, 130, 505, PurplePlayer, white)

            print_text(TINY_FONT, 325, 470, "Player 2:", black)
            pygame.draw.rect(gameDisplay, red, (320,500,150,40))
            print_text(TINY_FONT, 330, 505, RedPlayer, white)

            if player_amount_num >= 3:
                print_text(TINY_FONT, 525, 470, "Player 3:", black)
                pygame.draw.rect(gameDisplay, green, (520,500,150,40))
                print_text(TINY_FONT, 530, 505, GreenPlayer, white)

                if player_amount_num == 4:
                    print_text(TINY_FONT, 725, 470, "Player 4:", black)
                    pygame.draw.rect(gameDisplay, black, (720,500,150,40))
                    print_text(TINY_FONT, 730, 505, BlackPlayer, white)

            button('Proceed', 550, 250,300,150, bright_green,green,resource_counter)

                # Resource Menu
            text_write("Purple Player Resources: " + str(total_resource_list[0]), PA_font_mid, player_amount_x, player_amount_y - 20)
            text_write("Red Player Resources: " + str(total_resource_list[1]), PA_font_mid, player_amount_x, player_amount_y + 10)
            if player_amount_num >= 3:
                text_write("Green Player Resources: " + str(total_resource_list[2]), PA_font_mid, player_amount_x, player_amount_y + 40)
                if player_amount_num == 4:
                    text_write("Black Player Resources: " + str(total_resource_list[3]), PA_font_mid, player_amount_x, player_amount_y + 70)


            yellowRect = pygame.Rect(320, 20, 80, 120)
            orangeRect = pygame.Rect(yellowRect.x + yellowRect.width*1.1, yellowRect.y, yellowRect.width, yellowRect.height)
            blueRect = pygame.Rect(yellowRect.x + yellowRect.width*2.2, yellowRect.y, yellowRect.width, yellowRect.height)
            redRect = pygame.Rect(yellowRect.x + yellowRect.width*3.3, yellowRect.y, yellowRect.width, yellowRect.height)

            pygame.draw.rect(gameDisplay, (255, 255, 0), yellowRect)
            pygame.draw.rect(gameDisplay, (255, 128, 0), orangeRect)
            pygame.draw.rect(gameDisplay, (0, 0, 255), blueRect)
            pygame.draw.rect(gameDisplay, (255, 0, 0), redRect)

        pygame.display.update()
        clock.tick(15)


def resource_counter():

    # TODO: Build a while loop which keeps going if the game is active.
    # TODO: Add a turn counter in the game loop.
    # TODO: Store the values per player so they can be remembered and used again.
    # TODO: Make the amount of players variable.

    # Defining the variables
    global turns
    global current_player
    current_player = 1
    global player_resources
    player_resources = 0
    global current_player_name
    current_player_name = 0
    background()
    global hardcore_setting
    while current_player <= player_amount_num:

        if current_player == 1:
            current_player_name = PurplePlayer
        elif current_player == 2:
            current_player_name = RedPlayer
        if player_amount_num >= 3:
            if current_player == 3:
                current_player_name = GreenPlayer
            if player_amount_num == 4:
                if current_player == 4:
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
        total_resource_list[current_player-1] += player_resources  # add player resources to the corresponding player in total_resource_list
        background()
        print_text(SMALL_FONT, 125, 470, "Player " + str(current_player_name) + " gets " + str(player_resources) + " resources.", white)

        # Continues to the next player and puts the playerResources on zero
        current_player = current_player + 1

        player_resources = 0

    # Resets the loop
    current_player = 1
    turns = turns + 1
    print(turns)
    print_text(SMALL_FONT, 825, 675, "Turns: " + str(turns), white)
    if hardcore_setting:
        gamescreen_3()





def gamescreen_3():
    start = True
    background()
    global hardcore_setting
    # 'Hardcore Mode'
    hardcore_color = red
    event_list = ['You gain 1 resource', 'You gain 3 resources', 'You gain 5 resources',
                  'You lose 1 resource', 'You lose 3 resources', 'You lose 5 resources',
                  'You gain 1 troop', 'You gain 3 troops', 'You gain 5 troops',
                  'You lose 1 troop', 'You lose 3 troops', 'You lose 5 troops']
    event_msg = random.choice(event_list)
    event_active = False

    while start:

        # Resource Menu
        text_write("Purple Player Resources: " + str(total_resource_list[0]), PA_font_mid, player_amount_x, player_amount_y - 20)
        text_write("Red Player Resources: " + str(total_resource_list[1]), PA_font_mid, player_amount_x, player_amount_y + 10)
        if player_amount_num >= 3:
            text_write("Green Player Resources: " + str(total_resource_list[2]), PA_font_mid, player_amount_x, player_amount_y + 40)
            if player_amount_num == 4:
                text_write("Black Player Resources: " + str(total_resource_list[3]), PA_font_mid, player_amount_x, player_amount_y + 70)


        yellowRect = pygame.Rect(320, 20, 80, 120)
        orangeRect = pygame.Rect(yellowRect.x + yellowRect.width*1.1, yellowRect.y, yellowRect.width, yellowRect.height)
        blueRect = pygame.Rect(yellowRect.x + yellowRect.width*2.2, yellowRect.y, yellowRect.width, yellowRect.height)
        redRect = pygame.Rect(yellowRect.x + yellowRect.width*3.3, yellowRect.y, yellowRect.width, yellowRect.height)

        pygame.draw.rect(gameDisplay, (255, 255, 0), yellowRect)
        pygame.draw.rect(gameDisplay, (255, 128, 0), orangeRect)
        pygame.draw.rect(gameDisplay, (0, 0, 255), blueRect)
        pygame.draw.rect(gameDisplay, (255, 0, 0), redRect)


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

                # if hardcore_button.collidepoint(event.pos):     # If hardcore button is clicked
                #     background()                    # Refill background to white before redrawing
                #     hardcore_setting = not hardcore_setting     # Toggle hardcore_setting between True / False
                #     if hardcore_setting:                        # if True
                #         hardcore_color = (0, 255, 0)            # Green
                #     else:                                       # Else
                #         hardcore_color = red                    # Red
            
                if event_button.collidepoint(event.pos) and not event_active:                 # If event button is clicked and an event is not already open
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
                    playerinput_screen()
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
