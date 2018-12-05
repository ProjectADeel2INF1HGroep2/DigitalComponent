import pygame
from local_variables import *
from click_button import *
from name_input import *
from count_resources import *

import random   # For random events

pygame.init()

def background():
    gamemap = pygame.image.load(os.path.join(image_path, 'map.jpg'))
    gamemap = pygame.transform.scale(gamemap,(display_width,display_height))
    gameDisplay.blit(gamemap, (0,0))

def logo(x,y):
    logoImg = pygame.image.load(os.path.join(image_path, 'logo.jpg'))
    logoImg = pygame.transform.scale(logoImg, (int(display_height/3),int(display_width/4)))
    gameDisplay.blit(logoImg, (x,y))
    
def exit():
    pygame.quit()
    quit()

def start_screen():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                exit()

        background()
        logo(display_width * 0.10, display_height * 0.10)

        # title
        TextSurf, TextRectangle = textblock("Digital Component", LARGE_FONT)
        TextRectangle.center = ((display_width / 2),((display_height *0.5)))
        gameDisplay.blit(TextSurf, TextRectangle)

        #buttons
        button('START!',150,550,300,150,bright_blue,blue,playerinput_screen)
        button('EXIT!', 550,550,300,150,red,bright_red,exit)

        pygame.display.update()
        clock.tick(15)

def player_amount_screen():
    background()



    
def playerinput_screen():
    gameDisplay.fill(white)
    gameExit = False
    fpsclock = pygame.time.Clock()
    fps = 30
    PurplePlayer = False
    RedPlayer = False
    GreenPlayer = False
    BlackPlayer = False

    while not gameExit:
        fpsclock.tick(fps)
        pressed = None
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYUP:
                print(pygame.key.name(event.key))
                print(ord(pygame.key.name(event.key)))
            if event.type == pygame.QUIT:
                exit()

        background()

        if not PurplePlayer:
            PurplePlayer = enter_text(15)

        pygame.draw.rect(gameDisplay, purple, (90,500,150,40))
        print_text(TINY_FONT, 100, 500, PurplePlayer)

        if not RedPlayer:
            RedPlayer = enter_text(15)
        pygame.draw.rect(gameDisplay, red, (290,500,150,40))
        print_text(TINY_FONT, 300, 500, RedPlayer)

        if not GreenPlayer:
            GreenPlayer = enter_text(15)
        pygame.draw.rect(gameDisplay, green, (490,500,150,40))
        print_text(TINY_FONT, 500, 500, GreenPlayer)

        if not BlackPlayer:
            BlackPlayer = enter_text(15)

        background()

        pygame.draw.rect(gameDisplay, black, (690,500,150,40))
        print_text(TINY_FONT, 700, 500, BlackPlayer)
        
        pygame.draw.rect(gameDisplay, red, (290,500,150,40))
        print_text(TINY_FONT, 300, 500, RedPlayer)

        pygame.draw.rect(gameDisplay, purple, (90,500,150,40))
        print_text(TINY_FONT, 100, 500, PurplePlayer)

        pygame.draw.rect(gameDisplay, green, (490,500,150,40))
        print_text(TINY_FONT, 500, 500, GreenPlayer)

        button('PROCEED!',300,300,300,150,bright_green,green,gamescreen_3)

        count_resources()

        pygame.display.update()
        clock.tick(15)

def gamescreen_3():
    start = True
    gameDisplay.fill(white)

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
                    gameDisplay.fill(white)                     # Refill background to white before redrawing
                    hardcore_setting = not hardcore_setting     # Toggle hardcore_setting between True / False
                    if hardcore_setting:                        # if True
                        hardcore_color = (0, 255, 0)            # Green
                    else:                                       # Else
                        hardcore_color = red                    # Red

                elif event_button.collidepoint(event.pos) and not event_active:                 # If event button is clicked and an event is not already open
                    event_active = True                                                         # Set event active to true
                    gameDisplay.fill(white)                                                     # Refill background to white before redrawing
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
                    gameDisplay.fill(white)                                                     # Reset board to white

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