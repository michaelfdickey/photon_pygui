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

allButtons = {}
allButtons[0] = buttonExit			# exit button