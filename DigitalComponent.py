import pygame
import os
import time
from pygame.locals import *
import random

pygame.init()

#Screen
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
bright_green = (255,0,0)

#images
backgroundImg = pygame.image.load(os.path.join(image_path, 'logo.jpg'))
logoImg = pygame.image.load(os.path.join(image_path, 'logo.jpg'))

#imagesize
logoImg = pygame.transform.scale(logoImg, (250,250))

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
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        logo(x, y)
        TextSurf, TextRectangle = textblock("Digital Component", LARGE_FONT)
        TextRectangle.center = ((display_width / 2),((display_height *0.5)))
        gameDisplay.blit(TextSurf, TextRectangle)


        button('START!',150,550,300,150,bright_blue,blue,gameloop)
        button('EXIT!', 550,550,300,150,red,bright_red,exit)

        pygame.display.update()
        clock.tick(15)

def gameloop():

    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        gamemap = pygame.image.load(os.path.join(image_path, 'map.jpg'))
        gamemap = pygame.transform.scale(gamemap,(1000,750))

        gameDisplay.blit(gamemap, (0,0))
        #Enter Code on this line
        pygame.display.update()
        clock.tick(15)


game_intro()




exit()