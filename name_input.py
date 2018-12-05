import pygame
from local_variables import *
from itertools import cycle
pygame.init()


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