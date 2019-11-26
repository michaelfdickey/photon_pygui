# pgvar.py

testText = "test string from pgvar.py"


# ************************************************************************************************#
#	Import Modules
# ************************************************************************************************#

import pygame

# ************************************************************************************************#
#	Initial Variables
# ************************************************************************************************#


# # pygame font
pygame.font.init()																# needs to be called at the start of the program
v_myfont = pygame.font.SysFont('Arial',15)										# GUI font type and size
v_fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 15)

# # pre-defined colors
v_color_black = (0,0,0)
v_color_red = (255,0,0)
v_color_red_dark = (128,0,0)
v_color_green = (0,255,0)
v_color_green_dark = (0,128,0)
v_color_blue = (0,0,255)
v_color_blue_dark = (0,0,128)
v_color_white = (255,255,255)
v_color_pink = (255,200,200)
v_color_gray = (128,128,128)
v_color_yellow = (255,255,0)
v_color_yellow_grid = (128,128,0)

# # screen size
v_pygame_window_width = 1200
v_pygame_window_height = 1200

# # interface formatting
UI_topBar_height = 20
UI_sideBar_width = 120  
UI_menuButton_width = 120
UI_popup_small_width = 200
UI_popup_small_height = 200
UI_popup_small_origin_x = (v_pygame_window_width / 2) - (UI_popup_small_width / 2)
UI_popup_small_origin_y = (v_pygame_window_height / 2) - (UI_popup_small_height / 2)
UI_popup_medium_width = 400
UI_popup_medium_height = 400
UI_popup_large_width = 600
UI_popup_large_height = 600