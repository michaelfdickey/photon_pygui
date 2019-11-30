# pgui.py

moduleName = "pgui.py"

# ************************************************************************************************#
# ************************************************************************************************#
#	Import Modules
# ************************************************************************************************#
# ************************************************************************************************#

# # public python modules
import pygame
import random
import math
import sys
import time 			# for FPS functions
import inspect		# for displaying the line number of the code in print commands

# # unique modules for this app
import pgvar
import pgui
import pfunc

# ************************************************************************************************************************
# ************************************************************************************************************************
# 	button dictionaries	#
# ************************************************************************************************************************
# ************************************************************************************************************************


buttonExit = {}
buttonExit["name"] = "exit"
buttonExit["origin_x"] = 0
buttonExit["origin_y"] = pgvar.pygame_window_height - 20
buttonExit["width"] = pgvar.UI_sideBar_width
buttonExit["height"] = 20
buttonExit["label_txt"] = "EXIT"
buttonExit["type"] = "pushy"
buttonExit["enabled"] = True
buttonExit["color"] = pgvar.UI_button_color
buttonExit["group"] = "buttonExit"
buttonExit["visible"] = True

buttonCommand01 = {}
buttonCommand01["name"] = "command01"
buttonCommand01["origin_x"] = 0
buttonCommand01["origin_y"] = pgvar.pygame_window_height - 60
buttonCommand01["width"] = pgvar.UI_sideBar_width
buttonCommand01["height"] = 20
buttonCommand01["label_txt"] = "Command 01"
buttonCommand01["type"] = "pushy"
buttonCommand01["enabled"] = True
buttonCommand01["color"] = pgvar.UI_button_color
buttonCommand01["group"] = "command01"
buttonCommand01["visible"] = True

buttonCommand02 = {}
buttonCommand02["name"] = "command02"
buttonCommand02["origin_x"] = 0
buttonCommand02["origin_y"] = pgvar.pygame_window_height - 80
buttonCommand02["width"] = pgvar.UI_sideBar_width
buttonCommand02["height"] = 20
buttonCommand02["label_txt"] = "Command 02"
buttonCommand02["type"] = "pushy"
buttonCommand02["enabled"] = True
buttonCommand02["color"] = pgvar.UI_button_color
buttonCommand02["group"] = "command02"
buttonCommand02["visible"] = True

buttonCommand03 = {}
buttonCommand03["name"] = "command03"
buttonCommand03["origin_x"] = 0
buttonCommand03["origin_y"] = pgvar.pygame_window_height - 100
buttonCommand03["width"] = pgvar.UI_sideBar_width
buttonCommand03["height"] = 20
buttonCommand03["label_txt"] = "Command 03"
buttonCommand03["type"] = "pushy"
buttonCommand03["enabled"] = True
buttonCommand03["color"] = pgvar.UI_button_color
buttonCommand03["group"] = "command03"
buttonCommand03["visible"] = True

labelPushy = {}
labelPushy["name"] = "pushy_label"
labelPushy["origin_x"] = 0
labelPushy["origin_y"] = pgvar.pygame_window_height - 120
labelPushy["width"] =pgvar.UI_sideBar_width
labelPushy["height"] = 20
labelPushy["label_txt"] = "Pushy Buttons"
labelPushy["type"] = "label"
labelPushy["enabled"] = True
labelPushy["color"] = pgvar.UI_label_color
labelPushy["group"] = "pushy_buttons"
labelPushy["visible"] = True

allButtons = {}
allButtons[0] = buttonExit			# exit button
allButtons[1] = buttonCommand01		# command 01
allButtons[2] = buttonCommand02		# command 02
allButtons[3] = buttonCommand03		# command 03

allButtons[7] = labelPushy		# pushy button group label