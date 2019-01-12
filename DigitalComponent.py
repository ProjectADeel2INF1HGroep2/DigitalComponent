import random
from click_button import *
from input import *
from draw import *

pygame.init()


# Draw Background
def background():
    gamemap = pygame.image.load(os.path.join(image_path, 'map-blur.jpg'))
    gamemap = pygame.transform.scale(gamemap, (display_width, display_height))
    gameDisplay.blit(gamemap, (0, 0))


# Display Logo
def logo(x, y):
    logo_img = pygame.image.load(os.path.join(image_path, 'logo.png'))
    logo_img = pygame.transform.scale(logo_img, (int(display_height/2), int(display_width/2.66)))
    gameDisplay.blit(logo_img, (x, y))


# Exit the game (For Exit Button)
def game_exit():
    pygame.quit()
    quit()


# Update round counter
def next_round():
    global turns

    turns = turns + 1
    background()


# Initial Screen
def start_screen():

    global current_screen                                                               # Get variable from local_variables
    current_screen = "Start Screen"                                                     # Set screen to "Start Screen"

    while current_screen == "Start Screen":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                               # Exit game
                game_exit()

        background()                                                                    # Draw Background
        logo(display_width * 0.31, display_height * 0.1)                                # Draw Logo in Start Screen

        # Start Screen Buttons
        button('Start', 150, 550, 300, 150, bright_blue, blue, player_amount_screen)    # Start Button
        button('Exit', 550, 550, 300, 150, red, bright_red, game_exit)                  # Exit Button

        pygame.display.update()


# Player Amount Selection Screen
def player_amount_screen():
    global current_screen                                                           # Get variable from local_variables
    global player_amount_num                                                        # Declare player amount global variable used in game_screen

    current_screen = "Player Amount Screen"                                         # Set screen to "Player Amount Screen"
    background()                                                                    # Reset Background

    while current_screen == "Player Amount Screen":
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:          # If left clicked

                # Check if Player Amount Boxes are clicked
                if startPlayer2.collidepoint(event.pos):                            # If click event matches position of button 2
                    if not player_amount_num == 2:                                  # If player amount is not equal to 2 (2 is not already active)
                        startPlayer2.y += 2                                         # Increase 2's y position (Draw button in "Pressed" position)
                    if player_amount_num == 3:                                      # If player amount is 3
                        startPlayer3.y -= 2                                         # Decrease 3's y position (Draw as "Unpressed")
                    elif player_amount_num == 4:                                    # If player amount is 4
                        startPlayer4.y -= 2                                         # Decrease 4's y position (Draw as "Unpressed")
                    player_amount_num = 2
                elif startPlayer3.collidepoint(event.pos):
                    if not player_amount_num == 3:
                        startPlayer3.y += 2
                    if player_amount_num == 2:
                        startPlayer2.y -= 2
                    elif player_amount_num == 4:
                        startPlayer4.y -= 2
                    player_amount_num = 3
                elif startPlayer4.collidepoint(event.pos):
                    if not player_amount_num == 4:
                        startPlayer4.y += 2
                    if player_amount_num == 2:
                        startPlayer2.y -= 2
                    elif player_amount_num == 3:
                        startPlayer3.y -= 2
                    player_amount_num = 4
                elif startPlayerContinue.collidepoint(event.pos):                   # Continue to Player Input Screen
                    player_input_screen()

        # Draw the Player Amount Selection Elements =================================================================================

        # Draw Background
        pygame.draw.rect(gameDisplay, shadow, startPlayerBgBorder)                            # Player Amount Background Border
        pygame.draw.rect(gameDisplay, (220, 200, 80), startPlayerBackground)                        # Player Amount Background Rect

        text_write("Select Player Amount", PA_font_mid, player_amount_x, player_amount_y - 25)      # Player Amount Text

        # Draw Selection Rects
        pygame.draw.rect(gameDisplay, shadow, startPlayerShadow)                      # Shadow behind buttons

        pygame.draw.rect(gameDisplay, player_amount_color, startPlayer2)                            # 2 Players Button Rect
        text_write("2", 30, startPlayer2.x + 5, startPlayer2.y + 9)                                 # 2 Players Text
        pygame.draw.rect(gameDisplay, player_amount_color, startPlayer3)                            # 3 Players Button Rect
        text_write("3", 30, startPlayer3.x + 4, startPlayer3.y + 9)                                 # 3 Players Text
        pygame.draw.rect(gameDisplay, player_amount_color, startPlayer4)                            # 4 Players Button Rect
        text_write("4", 30, startPlayer4.x + 3, startPlayer4.y + 9)                                 # 4 Players Text

        # Draw Continue Button
        pygame.draw.rect(gameDisplay, shadow, startPlayerContinueShadow)              # Continue Button Shadow
        pygame.draw.rect(gameDisplay, (50, 200, 50), startPlayerContinue)                           # Continue Button
        text_write("Continue", PA_font_mid, startPlayerContinue.x + 4, startPlayerContinue.y + 8)   # Continue Text

        # ===========================================================================================================================

        pygame.display.update()


# Player name input screen
def player_input_screen():

    global current_screen                         # Get current screen variable
    current_screen = "Player Input Screen"        # Set current_screen to "Player Input Screen"

    background()

    while current_screen == "Player Input Screen":
        for event in pygame.event.get():
            # Exit Game
            if event.type == pygame.QUIT:
                game_exit()

        # Enter first player name, add to player_list
        if not player_list[0]:
            player_list[0] = enter_text(15)

            pygame.draw.rect(gameDisplay, purple, (120, 500, 150, 40))
            print_text(TINY_FONT, 130, 505, player_list[0], white)

        # Enter second player name, add to player_list
        if not player_list[1]:
            player_list[1] = enter_text(15)
            pygame.draw.rect(gameDisplay, red, (320, 500, 150, 40))
            print_text(TINY_FONT, 330, 505, player_list[1], white)

        # (If at least 3 players) Enter third player name, add to player_list
        if not player_list[2] and player_amount_num >= 3:
            player_list[2] = enter_text(15)
            pygame.draw.rect(gameDisplay, green, (520, 500, 150, 40))
            print_text(TINY_FONT, 530, 505, player_list[2], white)

        # (If 4 players) Enter fourth player name, add to player_list
        if not player_list[3] and player_amount_num == 4:
            player_list[3] = enter_text(15)

        background()  # Reset Background

        # Display player 1
        print_text(TINY_FONT, 125, 470, "Player 1:", black)
        pygame.draw.rect(gameDisplay, purple, (120, 500, 150, 40))
        print_text(TINY_FONT, 130, 505, player_list[0], white)

        # Display player 2
        print_text(TINY_FONT, 325, 470, "Player 2:", black)
        pygame.draw.rect(gameDisplay, red, (320, 500, 150, 40))
        print_text(TINY_FONT, 330, 505, player_list[1], white)

        # If at least 3 players:
        if player_amount_num >= 3:

            # Display player 3
            print_text(TINY_FONT, 525, 470, "Player 3:", black)
            pygame.draw.rect(gameDisplay, green, (520, 500, 150, 40))
            print_text(TINY_FONT, 530, 505, player_list[2], white)

            # If 4 players:
            if player_amount_num == 4:

                # Display player 4
                print_text(TINY_FONT, 725, 470, "Player 4:", black)
                pygame.draw.rect(gameDisplay, black, (720, 500, 150, 40))
                print_text(TINY_FONT, 730, 505, player_list[3], white)

        # Button to game_screen
        button('Proceed', 350, 250, 300, 150, bright_green, green, game_screen)

        pygame.display.update()


# Game screen
def game_screen():
    global current_screen
    current_screen = "Game Screen"

    background()

    # 'Hardcore Mode' variables
    hardcore_setting = False
    hardcore_color = red
    event_active = False
    show_resource_gain = False

    # Placeholder button, prevent local variables from being referenced before assignment
    placeholder_button = draw_square(display_width + 200, 10, 10, 10, white, white, "Placeholder")
    event_close = event_button = resource_close = end_yes = end_no = placeholder_button

    while current_screen == "Game Screen":
        text_write("Round: " + str(turns), PA_font_big, 20, 700)  # Turn Counter Text

        # Draw Buttons
        round_rect = draw_square(790, 115, 110, 40, green, light_green, "Next Round:")                              # Next Round Button
        end_rect = draw_square(display_width-110, display_height-50, 100, 40, purple, light_purple, "End Game")     # End Button

        hardcore_bg = draw_square(730, 15, 230, 40, bright_red, white)                                              # Background rect, scaled to button rect
        text_write("Hardcore Mode:", PA_font_mid, hardcore_bg.x+10, hardcore_bg.y+10)                               # Hardcore mode Text
        hardcore_button = draw_square(hardcore_bg.x+160, hardcore_bg.y + 5, hardcore_bg.width - 170,
                                      hardcore_bg.height - 10, hardcore_color, white, str(hardcore_setting))        # Hardcore Button

        # If hardcore is set to True, draw event button, then blit event button text
        if hardcore_setting:
            event_button = draw_square(round_rect.x-10, round_rect.y-round_rect.h-10, 130, 40, blue, (50, 50, 255), "Random Event")

        # Make resources available for leaderboard()
        global purple_gets, red_gets, green_gets, black_gets

        # Formulas to calculate how many resources each player gets at the end of each round
        purple_gets = ((purple_resources[0] * 1) + (purple_resources[1] * 2) + (purple_resources[2] * 3) + (purple_resources[3] * 4))
        red_gets = ((red_resources[0] * 1) + (red_resources[1] * 2) + (red_resources[2] * 3) + (red_resources[3] * 4))
        green_gets = ((green_resources[0] * 1) + (green_resources[1] * 2) + (green_resources[2] * 3) + (green_resources[3] * 4))
        black_gets = ((black_resources[0] * 1) + (black_resources[1] * 2) + (black_resources[2] * 3) + (black_resources[3] * 4))

        # Player Names in the Resource Menu
        text_write(str(player_list[0]), PA_font_mid, player_amount_x, yellow_H / 4)
        text_write(str(player_list[1]), PA_font_mid, player_amount_x, yellow_H / 2)
        if player_amount_num >= 3:
            text_write(str(player_list[2]), PA_font_mid, player_amount_x, yellow_H * 0.75)
            if player_amount_num == 4:
                text_write(str(player_list[3]), PA_font_mid, player_amount_x, yellow_H)

        # Define rects for Resource menu + and - buttons (Colored Background)
        yellow_rect = pygame.Rect(yellow_X, yellow_Y, yellow_W, yellow_H / 2 + ((yellow_H / 4) * (player_amount_num - 2)))
        orange_rect = pygame.Rect(yellow_X + yellow_W + yellow_Gap, yellow_Y, yellow_W, yellow_H / 2 + ((yellow_H / 4) * (player_amount_num - 2)))
        blue_rect = pygame.Rect(orange_rect.x + yellow_W + yellow_Gap, yellow_Y, yellow_W, yellow_H / 2 + ((yellow_H / 4) * (player_amount_num - 2)))
        red_rect = pygame.Rect(blue_rect.x + yellow_W + yellow_Gap, yellow_Y, yellow_W, yellow_H / 2 + ((yellow_H / 4) * (player_amount_num - 2)))

        # Draw colored rects for + and - buttons (Colored Background)
        pygame.draw.rect(gameDisplay, (255, 255, 0), yellow_rect)
        pygame.draw.rect(gameDisplay, (255, 128, 0), orange_rect)
        pygame.draw.rect(gameDisplay, (0, 0, 255), blue_rect)
        pygame.draw.rect(gameDisplay, (255, 0, 0), red_rect)

        # Creates surface with alpha channel / transparency, fill the surface, then blit the surface
        alpha_bg_surf = pygame.Surface((yellow_X + (yellow_W*5) + (yellow_Gap*3) + (yellow_line_thickness-1) - yellow_x_margin, yellow_H / 2 + (player_amount_num - 2) * (yellow_H / 4)), pygame.SRCALPHA, 32)
        alpha_bg_surf.fill((100, 100, 100, 1))
        gameDisplay.blit(alpha_bg_surf, (yellow_X - 210, yellow_rect.y))

        # Draw horizontal lines for the Resource Counter Frame, scaled to the amount of players
        for hor_line in range(player_amount_num + 1):
            pygame.draw.line(gameDisplay, black, (yellow_x_margin, yellow_Y + ((yellow_H/4)*hor_line)), (yellow_X + (yellow_W*5) + (yellow_Gap*3), yellow_Y + ((yellow_H/4)*hor_line)), yellow_line_thickness)

        # Draw vertical lines for the Resource Counter Frame
        for vert_line in range(12):
            pygame.draw.line(gameDisplay, black, (yellow_X + yellow_W / 2 * vert_line + (yellow_Gap*(vert_line//3)) - ((yellow_W/2)*(vert_line//3)), yellow_Y),
                             (yellow_X + yellow_W / 2 * vert_line + (yellow_Gap*(vert_line//3)) - ((yellow_W/2)*(vert_line//3)), yellow_Y + (yellow_H / 2) + ((yellow_H / 4) * (player_amount_num - 2))))

        # Draw pluses
        for plusRepeat in range(4):
            for plus in range(player_amount_num):

                # Horizontal Lines
                pygame.draw.line(gameDisplay, green,
                                 (yellow_X + yellow_W / 8 + (yellow_W * plusRepeat) + (yellow_Gap * plusRepeat), yellow_Y + yellow_H / 8 + (yellow_H / 8 * (plus * 2))),
                                 (yellow_X + yellow_W / 8 + (yellow_W * plusRepeat) + (yellow_Gap * plusRepeat) + yellow_W * 0.25, yellow_Y + yellow_H / 8 + (yellow_H / 8 * (plus * 2))), 2)

                # Vertical Lines
                pygame.draw.line(gameDisplay, green,
                                 (yellow_X + yellow_W / 4 + (yellow_W * plusRepeat) + (yellow_Gap * plusRepeat), yellow_Y + (yellow_H / 16 + ((yellow_H / 8) * (plus * 2)))),
                                 (yellow_X + yellow_W / 4 + (yellow_W * plusRepeat) + (yellow_Gap * plusRepeat), yellow_Y + (yellow_H / 16 * 3 + ((yellow_H / 8) * (plus * 2)))), 2)

        # Draw minuses
        for minRepeat in range(4):
            for minus in range(player_amount_num):
                pygame.draw.line(gameDisplay, red,
                                 (yellow_X + yellow_W / 2 + (yellow_W / 8) + (yellow_W * minRepeat) + (yellow_Gap * minRepeat), yellow_Y + yellow_H / 8 + (yellow_H / 8 * (minus * 2))),
                                 (yellow_X + yellow_W / 2 + (yellow_W / 8 * 3) + (yellow_W * minRepeat) + (yellow_Gap * minRepeat), yellow_Y + yellow_H / 8 + (yellow_H / 8 * (minus * 2))), 2)

        # Fill in the plus_minus_list with the x,y coordinates of each individual + and - button
        for PMRow in range(4):
            for PMColumn in range(8):

                button_coords = [yellow_X + ((yellow_W / 2) * PMColumn) + (yellow_Gap * PMColumn//1.8 - (2*(PMColumn//1.8))),
                                 yellow_Y + ((yellow_W / 2) * PMRow) + 2 - (PMRow // 1.5 * 4 + (PMRow * 2) + (min(PMRow, 1) * 2))]

                plus_minus_list[PMRow][PMColumn].append(button_coords)

        # Resource counters for each color

        # Yellow counters
        for y_count in range(4):
                text_write(str(purple_resources[y_count]), PA_font_mid, yellow_X - 22 + (yellow_W * y_count) + (yellow_Gap * y_count), yellow_H / 4)

        # Red Counters
        for r_count in range(4):
            text_write(str(red_resources[r_count]), PA_font_mid, yellow_X - 22 + (yellow_W * r_count) + (yellow_Gap * r_count), yellow_H / 2)

        # If at least 3 Players
        if player_amount_num >= 3:
            # Green Counters
            for g_count in range(4):
                text_write(str(green_resources[g_count]), PA_font_mid, yellow_X - 22 + (yellow_W * g_count) + (yellow_Gap * g_count), yellow_H * 0.75)

            # If 4 Players
            if player_amount_num == 4:
                # Black Counters
                for b_count in range(4):
                    text_write(str(black_resources[b_count]), PA_font_mid, yellow_X - 22 + (yellow_W * b_count) + (yellow_Gap * b_count), yellow_H)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    # Left click

                if hardcore_button.collidepoint(event.pos) and not event_active and not show_resource_gain:     # If hardcore button is clicked
                    background()                                # Redraw background before redrawing
                    hardcore_setting = not hardcore_setting     # Toggle hardcore_setting between True / False
                    if hardcore_setting:                        # if True
                        hardcore_color = (0, 255, 0)            # Green
                    else:                                       # Else
                        hardcore_color = red                    # Red

                if event_button.collidepoint(event.pos) and not event_active and not show_resource_gain and hardcore_setting:    # If event button is clicked and an event is not already open
                    event_active = True                                                                 # Set event active to true
                    background()                                                                        # Refill background before redrawing
                    event_msg = random.choice(event_list)                                               # Get a random event from event list
                    event_background = draw_square(display_width-280, display_height/4,
                                                   250, 100,
                                                   (60, 100, 100), white, event_msg)                    # Event background)
                    event_close = draw_square(event_background.x + event_background.width - 30,
                                              event_background.y, 30, 30, red, white)                   # Event closing button

                    pygame.draw.line(gameDisplay, shadow, (event_close.x+1, event_close.y+1), (event_close.x + 29, event_close.y + 29), 2)
                    pygame.draw.line(gameDisplay, shadow, (event_close.x+1, event_close.y + 29), (event_close.x + 29, event_close.y+1), 2)  # Draw event closing button cross shadow
                    pygame.draw.line(gameDisplay, white, (event_close.x, event_close.y), (event_close.x + 28, event_close.y + 28), 2)
                    pygame.draw.line(gameDisplay, white, (event_close.x, event_close.y + 28), (event_close.x + 28, event_close.y), 2)  # Draw event closing button cross

                if event_close.collidepoint(event.pos) and event_active:   # If event closing button is clicked
                    event_active = False                    # Set event active to false
                    background()                            # Redraw background

                # If next round rect is clicked, increment turn counter, show each player's resources gained
                elif round_rect.collidepoint(event.pos) and not event_active and not show_resource_gain:
                    next_round()
                    show_resource_gain = True

                    resource_background = draw_square(display_width/2-200, display_height/4, 400, 200,  (20, 150, 250), white)                            # Resource background)
                    resource_close = draw_square(resource_background.x + resource_background.width - 30, resource_background.y, 30, 30, red, white)     # Resource closing button

                    pygame.draw.line(gameDisplay, shadow, (resource_close.x+1, resource_close.y+1), (resource_close.x + 29, resource_close.y + 29), 2)
                    pygame.draw.line(gameDisplay, shadow, (resource_close.x+1, resource_close.y + 29), (resource_close.x + 29, resource_close.y+1), 2)  # Draw resource closing button cross shadow
                    pygame.draw.line(gameDisplay, white, (resource_close.x, resource_close.y), (resource_close.x + 28, resource_close.y + 28), 2)
                    pygame.draw.line(gameDisplay, white, (resource_close.x, resource_close.y + 28), (resource_close.x + 28, resource_close.y), 2)       # Draw resource closing button cross

                # Popup message showing the resources each player gets at the end of a round
                if show_resource_gain:
                    text_write_centered_x(str(player_list[0]) + " gets " + str(purple_gets) + " resources", PA_font_mid, 210)
                    text_write_centered_x(str(player_list[1]) + " gets " + str(red_gets) + " resources", PA_font_mid, 260)
                    if player_amount_num >= 3:
                        text_write_centered_x(str(player_list[2]) + " gets " + str(green_gets) + " resources", PA_font_mid, 310)
                        if player_amount_num == 4:
                            text_write_centered_x(str(player_list[3]) + " gets " + str(black_gets) + " resources", PA_font_mid, 360)

                if resource_close.collidepoint(event.pos) and not event_active:
                    show_resource_gain = False
                    background()

                # If End round button is clicked
                elif end_rect.collidepoint(event.pos) and not event_active and not show_resource_gain:
                    text_write("Are you sure?", PA_font_mid, end_rect.x-5, end_rect.y-80)
                    end_yes = draw_square(end_rect.x, end_rect.y-50, 50, 40, green, white, "Yes")
                    end_no = draw_square(end_yes.x+end_yes.width+5, end_rect.y-50, 50, 40, red, white, "No")

                if end_yes.collidepoint(event.pos):
                    leaderboard()

                elif end_no.collidepoint(event.pos):
                    end_yes = placeholder_button
                    end_no = placeholder_button
                    background()

                # Make Plus / Minus buttons interactive
                pm_names = [purple_resources, red_resources, green_resources, black_resources]

                if not event_active and not show_resource_gain:
                    for p_m_row in range(4):
                        if plus_minus_list[p_m_row][0][0][1] <= event.pos[1] < plus_minus_list[min((p_m_row+1), 3)][0][0][1] + ((p_m_row//3)*((yellow_W / 2) * 2)):

                            for p_m_col in range(0, 7, 2):
                                if plus_minus_list[0][p_m_col][0][0] <= event.pos[0] < (plus_minus_list[0][p_m_col][0][0] + (yellow_W / 2)):
                                    pm_names[p_m_row][int(p_m_col/2)] += 1
                                    background()
                                elif plus_minus_list[0][p_m_col][0][0] + (yellow_W / 2) <= event.pos[0] < (plus_minus_list[0][p_m_col][0][0] + (yellow_W / 2) * 2):
                                    if pm_names[p_m_row][int(p_m_col/2)] > 0:
                                        pm_names[p_m_row][int(p_m_col/2)] -= 1
                                        background()

        pygame.display.update()


def leaderboard():
    global current_screen
    global purple_gets, red_gets, green_gets, black_gets

    current_screen = "Leaderboard"

    background()

    while current_screen == "Leaderboard":
        for event in pygame.event.get():
            # Exit Game
            if event.type == pygame.QUIT:
                game_exit()

        # Add players up to the number that played to the leaderboard_list in a tuple (name, score)
        leaderboard_list = [(player_list[0], purple_gets), (player_list[1], red_gets)]
        if player_amount_num >= 3:
            leaderboard_list.append((player_list[2], green_gets))
            if player_amount_num == 4:
                leaderboard_list.append((player_list[3], black_gets))

        # Sorts the leaderboard_list by the second element in the tuples (score), reverses the sorted list to put higher scores first (descending),
        # and puts the scores, along with the name and the position in the ranking on the screen
        for rank in range(player_amount_num):
            global ranking_text
            ranking_text = text_write_centered_x(("#" + str(rank+1) + ": " + sorted(leaderboard_list, key=lambda score: score[1], reverse=True)[rank][0] + " with " +
                                                  str(sorted(leaderboard_list, key=lambda nr: nr[1], reverse=True)[rank][1]) + " Points!"), PA_font_big, 225+(40*rank))

        # Creates transparent surface and border for scores
        alpha_score_surf = pygame.Surface((40+ranking_text.width, 100+(25*player_amount_num)), pygame.SRCALPHA, 32)
        alpha_score_surf.fill((100, 100, 100, 1))
        gameDisplay.blit(alpha_score_surf, (display_width/2-(40+ranking_text.width)/2, 180))
        pygame.draw.rect(gameDisplay, black, pygame.Rect(display_width/2-(40+ranking_text.width)/2, 180, 40+ranking_text.width, 100+(25*player_amount_num)), 1)

        # Draw Leaderboard box and write "Leaderboard", centered on the screen
        leaderboard_sqr = draw_square(display_width/2-175, 100, 350, 70, (255, 255, 50), white)
        text_write_centered_x("Leaderboard", 60, leaderboard_sqr.centery)

        pygame.display.update()


start_screen()
