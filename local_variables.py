import pygame
import os
pygame.init()


# GameDisplay
display_height = 750
display_width = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turf Wars')


# Paths
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path
font_path = os.path.join(resource_path, 'fonts')


# Fonts
DEFAULT_FONT = "freesansbold.ttf"
SMALL_FONT = pygame.font.Font(os.path.join(font_path, "SourceSansPro-SemiBold.otf"),40)
TINY_FONT = pygame.font.Font(os.path.join(font_path, "SourceSansPro-SemiBold.otf"),20)
LARGE_FONT  = pygame.font.Font(os.path.join(font_path, "SourceSansPro-SemiBold.otf"),80)


# Colors
purple = (128, 0, 128)
light_purple = (255, 50, 255)
blue = (0, 0, 200)
bright_blue = (0, 0, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
light_green = (50, 255, 50)
bright_green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
shadow = (30, 30, 30)

player_amount_color = (130, 130, 130)


# Turns Counter
turns = 0


# Player Amount Font
PA_font = pygame.font.SysFont("arial", 36)                                                            # Default font
PA_font_big = 36
PA_fontSmall = pygame.font.SysFont("arial", 18)                                                       # Small Font
PA_font_mid = 18
PA_fontInput = pygame.font.SysFont("arial", 20)                                                       # Setup Screen Font
PA_font_small = 8
PA_textShadow = (30, 30, 30)


# Player Amount Buttons
player_amount_x = 20
player_amount_y = 40
player_amount_size = 26

player_amount_num = 4  # Number of Players selected

startPlayerBackground = pygame.Rect(player_amount_x-4, player_amount_y - 25, player_amount_size * 7, player_amount_size * 4)
startPlayerBgBorder = pygame.Rect(startPlayerBackground.x-2, startPlayerBackground.y-2, startPlayerBackground.width+4, startPlayerBackground.height + 4)
startPlayerShadow = pygame.Rect(player_amount_x+2, player_amount_y+4, player_amount_size * 3 + 2, player_amount_size*2)
startPlayer2 = pygame.Rect(player_amount_x, player_amount_y, player_amount_size, player_amount_size*2)
startPlayer3 = pygame.Rect(player_amount_x + player_amount_size+1, player_amount_y, player_amount_size, player_amount_size*2)
startPlayer4 = pygame.Rect(player_amount_x + player_amount_size*2 + 2, player_amount_y+2, player_amount_size, player_amount_size*2)
startPlayerContinue = pygame.Rect(player_amount_x*5.5, player_amount_y+10, player_amount_size*3 + 2, player_amount_size*1.5)
startPlayerContinueShadow = pygame.Rect(startPlayerContinue.x+2, startPlayerContinue.y+2, player_amount_size*3 + 2, player_amount_size*1.5)


# Current Screen Name Variable
current_screen = None


# Player Name List
player_list = [None, None, None, None]


# Hardcore Mode
event_list = ['You gain 1 resource', 'You gain 3 resources', 'You gain 5 resources',
              'You lose 1 resource', 'You lose 3 resources', 'You lose 5 resources',
              'You gain 1 troop', 'You gain 3 troops', 'You gain 5 troops',
              'You lose 1 troop', 'You lose 3 troops', 'You lose 5 troops']


# Game Screen Resource Counter Lists
purple_resources = [0, 0, 0, 0]
red_resources = [0, 0, 0, 0]
green_resources = [0, 0, 0, 0]
black_resources = [0, 0, 0, 0]


# Resource Menu Variables
yellow_X = 220              # Most of the stuff in the resource menu scales off of these
yellow_Y = 20               #
yellow_W = 80               #
yellow_H = 140              #
yellow_Gap = 24             #
yellow_x_margin = 10        #
yellow_line_thickness = 2   #


# Plus / Minus List
plus_minus_list = [[[], [], [], [], [], [], [], []],
                   [[], [], [], [], [], [], [], []],
                   [[], [], [], [], [], [], [], []],
                   [[], [], [], [], [], [], [], []]]
