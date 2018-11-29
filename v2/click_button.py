import pygame

from local_variables import *
pygame.init()

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