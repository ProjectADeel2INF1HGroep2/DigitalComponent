import pygame
import os
from pygame.locals import*
import time

pygame.init()

display_height = 750
display_width = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turf Wars')
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path


DEFAULT_FONT = "freesansbold.ttf"
SMALL_FONT = pygame.font.Font(os.path.join("resources", "fonts", "COMIC.ttf"),40)
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
backgroundImg = pygame.image.load(os.path.join(image_path, 'logo.jpg'))

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
    TextSurf, TextRectangle = text_objects(text, LARGE_FONT)
    TextRectangle.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRectangle)


def button(msg, x,y,w,h,ic,ac,action=None):
# This function has the parameters of:
# msg: What do you want the button to say on it.
# x: The x location of the top left coordinate of the button box.
# y: The y location of the top left coordinate of the button box.
# w: Button width.
# h: Button height.
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

    textSurf, textRectangle = text_objects(msg, SMALL_FONT)
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
        TextSurf, TextRectangle = text_objects("Digital Component", LARGE_FONT)
        TextRectangle.center = ((display_width/2),(display_height/2))
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

        gameDisplay.fill(white)
        #Enter Code on this line
        gameDisplay.blit(backgroundImg, (0, 0))


        pygame.display.update()
        clock.tick(15)


game_intro()
gameloop()
pygame.quit()
quit()