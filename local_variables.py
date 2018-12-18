import pygame
import os
pygame.init()

# GameDisplay
display_height = 750
display_width = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turf Wars')
clock = pygame.time.Clock()

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
blue = (0,0,200)
red = (200,0,0)
green = (0,200,0)
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
bright_blue = (0,0,255)
bright_green = (0,255,0)

# Players
PurplePlayer = 0
RedPlayer = 0
GreenPlayer = 0
BlackPlayer = 0

# Turns
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

startPlayerBackground = pygame.Rect(player_amount_x-4, player_amount_y - 25, player_amount_size * 7, player_amount_size * 4)
startPlayerBgBorder = pygame.Rect(startPlayerBackground.x-2, startPlayerBackground.y-2, startPlayerBackground.width+4, startPlayerBackground.height + 4)
startPlayerShadow = pygame.Rect(player_amount_x+2, player_amount_y+4, player_amount_size * 3 + 2, player_amount_size*2)
startPlayer2 = pygame.Rect(player_amount_x, player_amount_y, player_amount_size, player_amount_size*2)
startPlayer3 = pygame.Rect(player_amount_x + player_amount_size+1, player_amount_y, player_amount_size, player_amount_size*2)
startPlayer4 = pygame.Rect(player_amount_x + player_amount_size*2 + 2, player_amount_y+2, player_amount_size, player_amount_size*2)
startPlayerContinue = pygame.Rect(player_amount_x*5.5, player_amount_y+10, player_amount_size*3 + 2, player_amount_size*1.5)
startPlayerContinueShadow = pygame.Rect(startPlayerContinue.x+2, startPlayerContinue.y+2, player_amount_size*3 + 2, player_amount_size*1.5)

player_amount_color = (130, 130, 130)
player_amount_shadow = (30, 30, 30)

hardcore_setting = False
