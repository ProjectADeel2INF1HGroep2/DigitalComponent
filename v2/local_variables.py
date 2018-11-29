import pygame
import os
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