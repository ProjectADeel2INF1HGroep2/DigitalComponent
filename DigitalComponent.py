import pygame
import os
from pygame.locals import*

pygame.init()

display_height = 800
display_width = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turf Wars')
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path




blue = (63,72,204)
red = (200,0,0)
black = (0,0,0)
green = (0,200,0)
white = (255,255,255)


logoImg = pygame.image.load(os.path.join(image_path, 'logo.png'))

def logo(x,y):
    gameDisplay.blit(logoImg, (x,y))

x = (display_width * 0.10)
y = (display_height * 0.10)


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
        # largeText = pygame.font.Font('freesansbold.ttf',115)
        # TextSurf, TextRect = text_objects("Turf Wars", largeText)
        # TextRect.center = ((display_width/2),(display_height/2))
        # gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
        

game_intro()
pygame.quit()
quit()