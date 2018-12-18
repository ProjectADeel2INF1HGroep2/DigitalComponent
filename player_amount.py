from local_variables import *

player_amount_num = 4  # Change later
player_amount_done = False

# Text Function
def text_write(write_text, write_size, write_x, write_y):

    write_color = (255, 255, 255)
    write_color_shadow = (30, 30, 30)
    font_name = "arial"
    font_object = pygame.font.SysFont(font_name, write_size)
    text_surface = font_object.render(write_text, True, write_color)
    text_rectangle = text_surface.get_rect()
    text_rectangle.topleft = write_x, write_y
    text_surface_shadow = font_object.render(write_text, True, write_color_shadow)
    text_rectangle_shadow = text_surface_shadow.get_rect()
    text_rectangle_shadow.topleft = write_x+1, write_y+1

    gameDisplay.blit(text_surface_shadow, text_rectangle_shadow)
    gameDisplay.blit(text_surface, text_rectangle)