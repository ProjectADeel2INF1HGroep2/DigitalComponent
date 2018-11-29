import pygame
from pygame.locals import *
import sys, time

from local_variables import *
from click_button import *
from name_input import *

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

def game_intro():

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

        button('PROCEED!',300,300,300,150,bright_green,green,game_start)

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

        background()

        pygame.display.update()
        clock.tick(15)

game_intro()


exit()