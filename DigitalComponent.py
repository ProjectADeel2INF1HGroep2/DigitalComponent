import random
from click_button import *
from input import *
from local_variables import *
from player_amount import *

pygame.init()
# Total resources for each player
total_resource_list = [0, 0, 0, 0]
player_list = ["Purple", "Red", "Green", "Black"]
current_player = 1

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

    input_active = True
    while not gameExit and input_active:
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

            button('Proceed',350,250,300,150,bright_green,green,gamescreen_3)

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

        '''
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
        '''

    # Resets the loop
    turns = turns + 1
    print(turns)
    print_text(SMALL_FONT, 825, 675, "Turns: " + str(turns), white)


def next_player():
    global current_player
    global player_amount_num
    global turns

    if current_player == player_amount_num:
        current_player = 1
        pygame.display.update()

        pGet = ((pY_resources * 1) + (pO_resources * 2) + (pB_resources * 3) + (pR_resources * 4))
        rGet = ((rY_resources * 1) + (rO_resources * 2) + (rB_resources * 3) + (rR_resources * 4))
        gGet = ((gY_resources * 1) + (gO_resources * 2) + (gB_resources * 3) + (gR_resources * 4))
        bGet = ((bY_resources * 1) + (bO_resources * 2) + (bB_resources * 3) + (bR_resources * 4))

        total_resource_list[0] += pGet
        total_resource_list[1] += rGet
        total_resource_list[2] += gGet
        total_resource_list[3] += bGet

        turns = turns + 1

    else:
        current_player = current_player + 1

    background()

def gamescreen_3():

    global input_active
    input_active = False
    start = True
    background()

    #'''
    # 'Hardcore Mode'
    hardcore_setting = False
    hardcore_color = red
    event_list = ['You gain 1 resource', 'You gain 3 resources', 'You gain 5 resources',
                  'You lose 1 resource', 'You lose 3 resources', 'You lose 5 resources',
                  'You gain 1 troop', 'You gain 3 troops', 'You gain 5 troops',
                  'You lose 1 troop', 'You lose 3 troops', 'You lose 5 troops']
    event_msg = random.choice(event_list)
    event_active = False
    #'''

    global pY_resources
    global pO_resources
    global pB_resources
    global pR_resources
    pY_resources = 0
    pO_resources = 0
    pB_resources = 0
    pR_resources = 0

    global rY_resources
    global rO_resources
    global rB_resources
    global rR_resources
    rY_resources = 0
    rO_resources = 0
    rB_resources = 0
    rR_resources = 0

    global gY_resources
    global gO_resources
    global gB_resources
    global gR_resources
    gY_resources = 0
    gO_resources = 0
    gB_resources = 0
    gR_resources = 0

    global bY_resources
    global bO_resources
    global bB_resources
    global bR_resources
    bY_resources = 0
    bO_resources = 0
    bB_resources = 0
    bR_resources = 0


    while start:
        #global turns
        pygame.draw.rect(gameDisplay, green, next_p_rect)

        text_write("Current Player: " + str(player_list[current_player-1]), PA_font_mid, 760, 150)
        text_write("Next Player", PA_font_mid, 792, 190)
        text_write("Round: " + str(turns), PA_font_big, 20, 700)


        if current_player == 1 and turns > 0:
            text_write(str(PurplePlayer)+" gets " + str(pGet) + " resources", PA_font_mid, 400, 200)
            text_write(str(RedPlayer)+ " gets " + str(rGet) + " resources", PA_font_mid, 400, 250)
            if player_amount_num >= 3:
                text_write(str(GreenPlayer)+ " gets " + str(gGet) + " resources", PA_font_mid, 400, 300)
                if player_amount_num == 4:
                    text_write(str(BlackPlayer)+" gets " + str(bGet) + " resources", PA_font_mid, 400, 350)

        # resource_counter()  <- commented while working on resource + and - buttons

        # Resource Menu
        yellow_X = 320   # Most of the stuff in the resource menu scales off of these
        yellow_Y = 20    #
        yellow_W = 80    #
        yellow_H = 140   #
        yellow_Gap = 24  #

        text_write(str(PurplePlayer)+"'s Resources: " + str(total_resource_list[0]), PA_font_mid, player_amount_x, yellow_H/4)           # Player resource text, left side
        text_write(str(RedPlayer)+"'s Resources: " + str(total_resource_list[1]), PA_font_mid, player_amount_x, yellow_H/2)              #
        if player_amount_num >= 3:                                                                                                #
            text_write(str(GreenPlayer)+"'s Resources: " + str(total_resource_list[2]), PA_font_mid, player_amount_x, yellow_H*0.75)     #
            if player_amount_num == 4:                                                                                            #
                text_write(str(BlackPlayer)+"'s Resources: " + str(total_resource_list[3]), PA_font_mid, player_amount_x, yellow_H)      #

        yellowRect = pygame.Rect(yellow_X, yellow_Y, yellow_W, yellow_H/2 + ((yellow_H/4)*(player_amount_num-2)))                         # Colored rects for + and - buttons
        orangeRect = pygame.Rect(yellow_X+yellow_W+yellow_Gap, yellow_Y, yellow_W, yellow_H/2 + ((yellow_H/4)*(player_amount_num-2)))     #
        blueRect = pygame.Rect(orangeRect.x+yellow_W+yellow_Gap, yellow_Y, yellow_W, yellow_H/2 + ((yellow_H/4)*(player_amount_num-2)))   #
        redRect = pygame.Rect(blueRect.x+yellow_W+yellow_Gap, yellow_Y, yellow_W, yellow_H/2 + ((yellow_H/4)*(player_amount_num-2)))      #

        alpha_bgSurf = pygame.Surface((yellow_W*8.5+20, yellow_H/2 + (player_amount_num-2)*(yellow_H/4)), pygame.SRCALPHA, 32)    # Creates surface with alpha channel / transparency
        alpha_bgSurf.fill((100, 100, 100, 1))                                                                                     # Fill the surface
        gameDisplay.blit(alpha_bgSurf, (yellow_Y/2, yellow_Y))                                                                    # Blit the surface

        pygame.draw.rect(gameDisplay, (255, 255, 0), yellowRect)    # Draw colored rects for + and - buttons
        pygame.draw.rect(gameDisplay, (255, 128, 0), orangeRect)    #
        pygame.draw.rect(gameDisplay, (0, 0, 255), blueRect)        #
        pygame.draw.rect(gameDisplay, (255, 0, 0), redRect)         #

        pygame.draw.line(gameDisplay, black, (10, yellow_Y), (yellow_W*8.5+31, yellow_Y), 2)                                       # Draw horizontal lines
        pygame.draw.line(gameDisplay, black, (10, yellow_Y+(yellow_H/4)), (yellow_W*8.5+31, yellow_Y+(yellow_H/4)), 2)             #
        pygame.draw.line(gameDisplay, black, (10, yellow_Y+(yellow_H/2)), (yellow_W*8.5+31, yellow_Y+(yellow_H/2)), 2)             #
        if player_amount_num >= 3:                                                                                                 #
            pygame.draw.line(gameDisplay, black, (10, yellow_Y+(yellow_H*0.75)), (yellow_W*8.5+31, yellow_Y+(yellow_H*0.75)), 2)   #
            if player_amount_num == 4:                                                                                             #
                pygame.draw.line(gameDisplay, black, (10, yellow_Y+yellow_H), (yellow_W*8.5+32, yellow_Y+yellow_H), 2)             #

        pygame.draw.line(gameDisplay, black, (yellow_X, yellow_Y), (yellow_X, yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))                              # Yellow vertical lines
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2, yellow_Y), (yellow_X+yellow_W/2, yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))        #
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*2, yellow_Y), (yellow_X+yellow_W/2*2, yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    #

        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*2 + yellow_Gap, yellow_Y), (yellow_X+yellow_W/2*2 + yellow_Gap, yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    # Orange vertical lines
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*3 + yellow_Gap, yellow_Y), (yellow_X+yellow_W/2*3 + yellow_Gap, yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    #
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*4 + yellow_Gap, yellow_Y), (yellow_X+yellow_W/2*4 + yellow_Gap, yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    #

        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*4 + (yellow_Gap*2), yellow_Y), (yellow_X+yellow_W/2*4 + (yellow_Gap*2), yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    # Blue vertical lines
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*5 + (yellow_Gap*2), yellow_Y), (yellow_X+yellow_W/2*5 + (yellow_Gap*2), yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    #
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*6 + (yellow_Gap*2), yellow_Y), (yellow_X+yellow_W/2*6 + (yellow_Gap*2), yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    #

        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*6 + (yellow_Gap*3), yellow_Y), (yellow_X+yellow_W/2*6 + (yellow_Gap*3), yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    # Black vertical lines
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*7 + (yellow_Gap*3), yellow_Y), (yellow_X+yellow_W/2*7 + (yellow_Gap*3), yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    #
        pygame.draw.line(gameDisplay, black, (yellow_X+yellow_W/2*8 + (yellow_Gap*3), yellow_Y), (yellow_X+yellow_W/2*8 + (yellow_Gap*3), yellow_Y+(yellow_H/2)+((yellow_H/4)*(player_amount_num-2))))    #

        # Draw pluses
        for plusRepeat in range(4):
            for plus in range(player_amount_num):
                pygame.draw.line(gameDisplay, green,
                                 (yellow_X+yellow_W/8+(yellow_W*plusRepeat)+(yellow_Gap*plusRepeat), yellow_Y+yellow_H/8+(yellow_H/8*(plus*2))),
                                 (yellow_X+yellow_W/8+yellow_W*0.25+(yellow_W*plusRepeat)+(yellow_Gap*plusRepeat), yellow_Y+yellow_H/8+(yellow_H/8*(plus*2))), 2)
                pygame.draw.line(gameDisplay, green,
                                 (yellow_X+yellow_W/4+(yellow_W*plusRepeat)+(yellow_Gap*plusRepeat), yellow_Y+(yellow_H/16+((yellow_H/8)*(plus*2)))),
                                 (yellow_X+yellow_W/4+(yellow_W*plusRepeat)+(yellow_Gap*plusRepeat), yellow_Y+(yellow_H/16*3+((yellow_H/8)*(plus*2)))), 2)

        # Draw minuses
        for minRepeat in range(4):
            for minus in range(player_amount_num):
                pygame.draw.line(gameDisplay, red,
                                 (yellow_X+yellow_W/2+(yellow_W/8)+(yellow_W*minRepeat)+(yellow_Gap*minRepeat), yellow_Y+yellow_H/8+(yellow_H/8*(minus*2))),
                                 (yellow_X+yellow_W/2+(yellow_W/8*3)+(yellow_W*minRepeat)+(yellow_Gap*minRepeat), yellow_Y+yellow_H/8+(yellow_H/8*(minus*2))), 2)

        # Plus / Minus List
        plus_minus_list = [[[], [], [], [], [], [], [], []],
                           [[], [], [], [], [], [], [], []],
                           [[], [], [], [], [], [], [], []],
                           [[], [], [], [], [], [], [], []]]

        # Fill in the plus_minus_list in a real inefficient way but meh it's late
        for PMRow in range(4):
            for PMColumn in range(8):
                if PMColumn < 2 and PMRow == 0:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn), (yellow_Y)+((yellow_W/2)*PMRow)+2])
                elif 2 <= PMColumn < 4 and PMRow == 0:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap + 2), yellow_Y+((yellow_W/2)*PMRow)+2])
                elif 4 <= PMColumn < 6 and PMRow == 0:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*2 + 2), yellow_Y+((yellow_W/2)*PMRow)+2])
                elif PMColumn > 5 and PMRow == 0:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*3 + 2), yellow_Y+((yellow_W/2)*PMRow)+2])

                elif PMColumn < 2 and PMRow == 1:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn), (yellow_Y)+((yellow_W/2)*PMRow)-2])
                elif 2 <= PMColumn < 4 and PMRow == 1:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap + 2), yellow_Y+((yellow_W/2)*PMRow)-2])
                elif 4 <= PMColumn < 6 and PMRow == 1:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*2 + 2), yellow_Y+((yellow_W/2)*PMRow)-2])
                elif PMColumn > 5 and PMRow == 1:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*3 + 2), yellow_Y+((yellow_W/2)*PMRow)-2])

                elif PMColumn < 2 and PMRow == 2:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn), (yellow_Y)+((yellow_W/2)*PMRow)-8])
                elif 2 <= PMColumn < 4 and PMRow == 2:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap + 2), yellow_Y+((yellow_W/2)*PMRow)-8])
                elif 4 <= PMColumn < 6 and PMRow == 2:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*2 + 2), yellow_Y+((yellow_W/2)*PMRow)-8])
                elif PMColumn > 5 and PMRow == 2:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*3 + 2), yellow_Y+((yellow_W/2)*PMRow)-8])

                elif PMColumn < 2 and PMRow == 3:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn), (yellow_Y)+((yellow_W/2)*PMRow)-12])
                elif 2 <= PMColumn < 4 and PMRow == 3:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap + 2), yellow_Y+((yellow_W/2)*PMRow)-12])
                elif 4 <= PMColumn < 6 and PMRow == 3:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*2 + 2), yellow_Y+((yellow_W/2)*PMRow)-12])
                elif PMColumn > 5 and PMRow == 3:
                    plus_minus_list[PMRow][PMColumn].append([yellow_X+((yellow_W/2)*PMColumn)+(yellow_Gap*3 + 2), yellow_Y+((yellow_W/2)*PMRow)-12])


                #'''

        # Resource counters for each color
        text_write(str(pY_resources), PA_font_mid, yellow_X - 22, yellow_H/4)
        text_write(str(pO_resources), PA_font_mid, yellow_X + (yellow_W*1) + yellow_Gap - 22, yellow_H/4)
        text_write(str(pB_resources), PA_font_mid, yellow_X + (yellow_W*2) + (yellow_Gap*2) - 22, yellow_H/4)
        text_write(str(pR_resources), PA_font_mid, yellow_X + (yellow_W*3) + (yellow_Gap*3) - 22, yellow_H/4)

        text_write(str(rY_resources), PA_font_mid, yellow_X - 22, yellow_H/2)
        text_write(str(rO_resources), PA_font_mid, yellow_X + (yellow_W*1) + yellow_Gap - 22, yellow_H/2)
        text_write(str(rR_resources), PA_font_mid, yellow_X + (yellow_W*3) + (yellow_Gap*3) - 22, yellow_H/2)
        text_write(str(rB_resources), PA_font_mid, yellow_X + (yellow_W*2) + (yellow_Gap*2) - 22, yellow_H/2)


        if player_amount_num >= 3:
            text_write(str(gY_resources), PA_font_mid, yellow_X - 22, yellow_H*0.75)
            text_write(str(gO_resources), PA_font_mid, yellow_X + (yellow_W*1) + yellow_Gap - 22, yellow_H*0.75)
            text_write(str(gB_resources), PA_font_mid, yellow_X + (yellow_W*2) + (yellow_Gap*2) - 22, yellow_H*0.75)
            text_write(str(gR_resources), PA_font_mid, yellow_X + (yellow_W*3) + (yellow_Gap*3) - 22, yellow_H*0.75)

            if player_amount_num == 4:
                text_write(str(bY_resources), PA_font_mid, yellow_X - 22, yellow_H)
                text_write(str(bO_resources), PA_font_mid, yellow_X + (yellow_W*1) + yellow_Gap - 22, yellow_H)
                text_write(str(bB_resources), PA_font_mid, yellow_X + (yellow_W*2) + (yellow_Gap*2) - 22, yellow_H)
                text_write(str(bR_resources), PA_font_mid, yellow_X + (yellow_W*3) + (yellow_Gap*3) - 22, yellow_H)


        # 'Hardcore Mode'
        hardcore_state = TINY_FONT.render(str(hardcore_setting), True, white)   # True / False Text
        hardcore_txt = TINY_FONT.render('Hardcore mode:', True, white)          # Hardcore mode Text
        event_txt = TINY_FONT.render(event_msg, True, black)                    # Random Events Text
        event_button_txt = TINY_FONT.render("Random Event", True, white)        # Event Button Text

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 'Hardcore Mode'

                pGet = ((pY_resources * 1) + (pO_resources * 2) + (pB_resources * 3) + (pR_resources * 4))
                rGet = ((rY_resources * 1) + (rO_resources * 2) + (rB_resources * 3) + (rR_resources * 4))
                gGet = ((gY_resources * 1) + (gO_resources * 2) + (gB_resources * 3) + (gR_resources * 4))
                bGet = ((bY_resources * 1) + (bO_resources * 2) + (bB_resources * 3) + (bR_resources * 4))

                if hardcore_button.collidepoint(event.pos):     # If hardcore button is clicked
                    background()                    # Refill background to white before redrawing
                    hardcore_setting = not hardcore_setting     # Toggle hardcore_setting between True / False
                    if hardcore_setting:                        # if True
                        hardcore_color = (0, 255, 0)            # Green
                    else:                                       # Else
                        hardcore_color = red                    # Red
            
                elif event_button.collidepoint(event.pos) and not event_active and hardcore_setting:                 # If event button is clicked and an event is not already open
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
                    background()
                    # Reset

                elif next_p_rect.collidepoint(event.pos) and not event_active:
                    next_player()

                # Plus / Minus buttons

                # First Row
                elif plus_minus_list[0][0][0][1] <= event.pos[1] < plus_minus_list[1][0][0][1]:
                    # Yellow
                    if plus_minus_list[0][0][0][0] <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)):
                        pY_resources += 1
                        background()
                    elif plus_minus_list[0][0][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)*2):
                        if pY_resources > 0:
                            pY_resources -= 1
                            background()
                    # Orange
                    elif plus_minus_list[0][2][0][0] <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)):
                        pO_resources += 1
                        background()
                    elif plus_minus_list[0][2][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)*2):
                        if pO_resources > 0:
                            pO_resources -= 1
                            background()
                    # Blue
                    elif plus_minus_list[0][4][0][0] <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)):
                        pB_resources += 1
                        background()
                    elif plus_minus_list[0][4][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)*2):
                        if pB_resources > 0:
                            pB_resources -= 1
                            background()
                    # Red
                    elif plus_minus_list[0][6][0][0] <= event.pos[0] < (plus_minus_list[0][6][0][0] + (yellow_W / 2)):
                        pR_resources += 1
                        background()
                    elif plus_minus_list[0][6][0][0] + (yellow_W / 2) <= event.pos[0] < (
                            plus_minus_list[0][6][0][0] + (yellow_W / 2) * 2):
                        if pR_resources > 0:
                            pR_resources -= 1
                            background()

                # Second Row
                elif plus_minus_list[1][0][0][1] <= event.pos[1] < plus_minus_list[2][0][0][1]:
                    # Yellow
                    if plus_minus_list[0][0][0][0] <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)):
                        rY_resources += 1
                        background()
                    elif plus_minus_list[0][0][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)*2):
                        if rY_resources > 0:
                            rY_resources -= 1
                            background()
                    # Orange
                    elif plus_minus_list[0][2][0][0] <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)):
                        rO_resources += 1
                        background()
                    elif plus_minus_list[0][2][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)*2):
                        if rO_resources > 0:
                            rO_resources -= 1
                            background()
                    # Blue
                    elif plus_minus_list[0][4][0][0] <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)):
                        rB_resources += 1
                        background()
                    elif plus_minus_list[0][4][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)*2):
                        if rB_resources > 0:
                            rB_resources -= 1
                            background()
                    # Red
                    elif plus_minus_list[0][6][0][0] <= event.pos[0] < (plus_minus_list[0][6][0][0] + (yellow_W / 2)):
                        rR_resources += 1
                        background()
                    elif plus_minus_list[0][6][0][0] + (yellow_W / 2) <= event.pos[0] < (
                            plus_minus_list[0][6][0][0] + (yellow_W / 2) * 2):
                        if rR_resources > 0:
                            rR_resources -= 1
                            background()

                # Third Row
                elif plus_minus_list[2][0][0][1] <= event.pos[1] < plus_minus_list[3][0][0][1]:
                    # Yellow
                    if plus_minus_list[0][0][0][0] <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)):
                        gY_resources += 1
                        background()
                    elif plus_minus_list[0][0][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)*2):
                        if gY_resources > 0:
                            gY_resources -= 1
                            background()
                    # Orange
                    elif plus_minus_list[0][2][0][0] <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)):
                        gO_resources += 1
                        background()
                    elif plus_minus_list[0][2][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)*2):
                        if gO_resources > 0:
                            gO_resources -= 1
                            background()
                    # Blue
                    elif plus_minus_list[0][4][0][0] <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)):
                        gB_resources += 1
                        background()
                    elif plus_minus_list[0][4][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)*2):
                        if gB_resources > 0:
                            gB_resources -= 1
                            background()
                    # Red
                    elif plus_minus_list[0][6][0][0] <= event.pos[0] < (plus_minus_list[0][6][0][0] + (yellow_W / 2)):
                        gR_resources += 1
                        background()
                    elif plus_minus_list[0][6][0][0] + (yellow_W / 2) <= event.pos[0] < (
                            plus_minus_list[0][6][0][0] + (yellow_W / 2) * 2):
                        if gR_resources > 0:
                            gR_resources -= 1
                            background()

                # Fourth Row
                elif plus_minus_list[3][0][0][1] <= event.pos[1] < plus_minus_list[3][0][0][1]+(yellow_W/2):
                    # Yellow
                    if plus_minus_list[0][0][0][0] <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)):
                        bY_resources += 1
                        background()
                    elif plus_minus_list[0][0][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][0][0][0] + (yellow_W/2)*2):
                        if bY_resources > 0:
                            bY_resources -= 1
                            background()
                    # Orange
                    elif plus_minus_list[0][2][0][0] <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)):
                        bO_resources += 1
                        background()
                    elif plus_minus_list[0][2][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][2][0][0] + (yellow_W/2)*2):
                        if bO_resources > 0:
                            bO_resources -= 1
                            background()
                    # Blue
                    elif plus_minus_list[0][4][0][0] <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)):
                        bB_resources += 1
                        background()
                    elif plus_minus_list[0][4][0][0]+(yellow_W/2) <= event.pos[0] < (plus_minus_list[0][4][0][0] + (yellow_W/2)*2):
                        if bB_resources > 0:
                            bB_resources -= 1
                            background()
                    # Red
                    elif plus_minus_list[0][6][0][0] <= event.pos[0] < (plus_minus_list[0][6][0][0] + (yellow_W / 2)):
                        bR_resources += 1
                        background()
                    elif plus_minus_list[0][6][0][0] + (yellow_W / 2) <= event.pos[0] < (plus_minus_list[0][6][0][0] + (yellow_W / 2) * 2):
                        if bR_resources > 0:
                            bR_resources -= 1
                            background()


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
        #'''

        pygame.display.update()
        clock.tick(60)


start_screen()


exit()
