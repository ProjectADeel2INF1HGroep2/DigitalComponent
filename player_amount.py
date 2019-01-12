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

def draw_square(sqr_x, sqr_y, sqr_w, sqr_h, sqr_color, sqr_border, sqr_str=None):
    sqr_rect = pygame.Rect(sqr_x, sqr_y, sqr_w, sqr_h)

    pygame.draw.rect(gameDisplay, shadow, pygame.Rect(sqr_x + 3, sqr_y + 3, sqr_w, sqr_h))
    pygame.draw.rect(gameDisplay, sqr_border, pygame.Rect(sqr_x - 1, sqr_y - 1, sqr_w + 2, sqr_h + 2))
    pygame.draw.rect(gameDisplay, sqr_color, sqr_rect)

    sqr_text = PA_fontSmall.render(sqr_str, True, white)
    sqr_text_shadow = PA_fontSmall.render(sqr_str, True, shadow)
    text_rect = sqr_text.get_rect(center=(sqr_x + (sqr_w / 2), sqr_y + (sqr_h / 2)))
    text_shadow_rect = sqr_text_shadow.get_rect(center=(sqr_x + (sqr_w / 2) + 1, sqr_y + (sqr_h / 2) + 1))
    gameDisplay.blit(sqr_text_shadow, text_shadow_rect)
    gameDisplay.blit(sqr_text, text_rect)

    return sqr_rect
