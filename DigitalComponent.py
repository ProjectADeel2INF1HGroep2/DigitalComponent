import pygame
import damian
from pygame.locals import *
import sys, os, time, random
from itertools import cycle


pygame.init()

#GameDisplay
display_height = 750
display_width = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turf Wars')
clock = pygame.time.Clock()

#paths
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path
font_path = os.path.join(resource_path, 'fonts')

#fonts
DEFAULT_FONT = "freesansbold.ttf"
SMALL_FONT = pygame.font.Font(os.path.join(font_path, "COMIC.ttf"),40)
TINY_FONT = pygame.font.Font(os.path.join(font_path, "COMIC.ttf"),20)
LARGE_FONT  = pygame.font.Font(os.path.join(font_path, "COMIC.ttf"),80)

#colors
purple = (128, 0, 128)
blue = (0,0,200)
red = (200,0,0)
green = (0,200,0)
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
bright_blue = (0,0,255)
bright_green = (0,255,0)

#images
backgroundImg = pygame.image.load(os.path.join(image_path, 'logo.jpg'))
logoImg = pygame.image.load(os.path.join(image_path, 'logo.jpg'))

#imagesize
logoImg = pygame.transform.scale(logoImg, (250,250))











def enter_text(max_length, lower = False, upper = False, title = False):
    """
    returns user name input of max length "max length and with optional
    string operation performed
    """
    pressed = ""
    finished = False
    # create list of allowed characters using ascii values
    # numbers 1-9, letters a-z
    all_chars = [i for i in range(97, 123)] +\
                     [i for i in range(48,58)]

    # create blinking underscore
    BLINKING_UNDERSCORE = pygame.USEREVENT + 0
    pygame.time.set_timer(BLINKING_UNDERSCORE, 800)
    blinky = cycle(["_", " "])
    next_blink = next(blinky)

    while not finished:
        pygame.draw.rect(gameDisplay, red, (125,175,200,40))
        print_text(TINY_FONT, 125, 150, "Enter Name:")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == BLINKING_UNDERSCORE:
                next_blink = next(blinky)
            # if input is in list of allowed characters, add to variable
            elif event.type == pygame.KEYUP and event.key in all_chars \
                 and len(pressed) < max_length:
                # caps entry?
                if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods()\
                   & pygame.KMOD_CAPS:
                    pressed += chr(event.key).upper()
                # lowercase entry
                else:
                    pressed += chr(event.key)
            # otherwise, only the following are valid inputs
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    pressed = pressed[:-1]
                elif event.key == pygame.K_SPACE:
                    pressed += " "
                elif event.key == pygame.K_RETURN:
                    finished = True
        # only draw underscore if input is not at max character length
        if len(pressed) < max_length:
            print_text(TINY_FONT, 130, 180, pressed + next_blink)
        else:
            print_text(TINY_FONT, 130, 180, pressed)
        pygame.display.update()

    # perform any selected string operations
    if lower: pressed = pressed.lower()
    if upper: pressed = pressed.upper()
    if title: pressed = pressed.title()

    return pressed



def print_text(TINY_FONT, x, y, text, color = white):
    """Draws a text image to display surface"""
    text_image = TINY_FONT.render(text, True, color)
    gameDisplay.blit(text_image, (x,y))



def logo(x,y):
    gameDisplay.blit(logoImg, (x,y))

x = (display_width * 0.10)
y = (display_height * 0.10)
    
def exit():
    pygame.quit()
    quit()

def textblock(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def textdisplay(text):
    TextSurf, TextRectangle = textblock(text, LARGE_FONT)
    TextRectangle.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRectangle)

def button(msg, x,y,w,h,ic,ac,action=None):
# This function has the parameters of:
# msg: Message you want to display
# x: The x location of the top left of the button box.
# y: The y location of the top left of the button box.
# w: horizontal width.
# h: vertical height.
# ic: Inactive color (when a mouse is not hovering).
# ac: Active color (when a mouse is hovering).
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
                action()      
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    textSurf, textRectangle = textblock(msg, SMALL_FONT)
    textRectangle.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRectangle)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                exit()
        
        #background
        gamemap = pygame.image.load(os.path.join(image_path, 'map.jpg'))
        gamemap = pygame.transform.scale(gamemap,(1000,750))
        gameDisplay.blit(gamemap, (0,0))

        # logo
        logo(x, y)

        # title
        TextSurf, TextRectangle = textblock("Digital Component", LARGE_FONT)
        TextRectangle.center = ((display_width / 2),((display_height *0.5)))
        gameDisplay.blit(TextSurf, TextRectangle)

        #buttons
        button('START!',150,550,300,150,bright_blue,blue,gameloop)
        button('EXIT!', 550,550,300,150,red,bright_red,exit)

        pygame.display.update()
        clock.tick(15)

def gameloop():
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



        #background
        gamemap = pygame.image.load(os.path.join(image_path, 'map.jpg'))
        gamemap = pygame.transform.scale(gamemap,(1000,750))
        gameDisplay.blit(gamemap, (0,0))


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

        gamemap = pygame.image.load(os.path.join(image_path, 'map.jpg'))
        gamemap = pygame.transform.scale(gamemap,(1000,750))
        gameDisplay.blit(gamemap, (0,0))


        pygame.draw.rect(gameDisplay, black, (690,500,150,40))
        print_text(TINY_FONT, 700, 500, BlackPlayer)
        
        pygame.draw.rect(gameDisplay, red, (290,500,150,40))
        print_text(TINY_FONT, 300, 500, RedPlayer)

        pygame.draw.rect(gameDisplay, purple, (90,500,150,40))
        print_text(TINY_FONT, 100, 500, PurplePlayer)


        pygame.draw.rect(gameDisplay, green, (490,500,150,40))
        print_text(TINY_FONT, 500, 500, GreenPlayer)

        button('PROCEED!',300,300,300,150,bright_green,black,game_start)
        pygame.display.update()
        clock.tick(15)

def game_start():


    start = True
    gameDisplay.fill(white)

    while start:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                exit()


        gameDisplay.fill(white)


        pygame.display.update()
        clock.tick(15)


game_intro()




exit()