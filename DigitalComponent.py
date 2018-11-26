import pygame
import os
from pygame.locals import*

pygame.init()

display_height = 800
display_width = 1100
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turf Wars')
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path


DEFAULT_FONT = "freesansbold.ttf"
LARGE_FONT  = pygame.font.Font(os.path.join("resources", "fonts", "COMIC.ttf"),80)


blue = (0,0,200)
red = (200,0,0)
green = (0,200,0)
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
bright_blue = (0,0,255)
bright_green = (255,0,0)


logoImg = pygame.image.load(os.path.join(image_path, 'logo.png'))

def logo(x,y):
    gameDisplay.blit(logoImg, (x,y))

x = (display_width * 0.10)
y = (display_height * 0.10)
    
def exit():
    pygame.quit()
    quit()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    TextSurf, TextRect = text_objects(text, LARGE_FONT)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

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
        TextSurf, TextRect = text_objects("Digital Component", LARGE_FONT)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        if 100+300 > mouse[0] > 100 and 550+150 > mouse[1] > 550:
            pygame.draw.rect(gameDisplay, bright_blue,(100,550,300,150))
        else:
            pygame.draw.rect(gameDisplay, blue,(100,550,300,150))

        if 400+300 > mouse[0] > 400 and 550+150 > mouse[1] > 550:
            pygame.draw.rect(gameDisplay, bright_red,(500,550,300,150))
        else:
            pygame.draw.rect(gameDisplay, red,(500,550,300,150))

        pygame.display.update()
        clock.tick(15)
        
game_intro()
pygame.quit()
quit()