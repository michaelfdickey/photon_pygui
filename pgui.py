# ************************************************************************************************#
# ************************************************************************************************#
#	Directory Structure
# ************************************************************************************************#
# ************************************************************************************************#

#	/photonmain.py 		# primary program
#	/pgvar.py 			# global variable declarations
#	/pgui.py 			# photon gui elements and buttons
#	/pfunc.py 			# functions
#	/pclass.py 			# button processing class that handles drawing / displaying UI
#	/pbproc.py 			# processing sticky, group, dropdown etc button actions
#	/photon_ref.py 		# references, dev notes, style guide, modification instructions

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
#import pfunc
#import pgui
#import pclass
#import pbproc

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

buttonSticky01 = {}
buttonSticky01["name"] = "sticky01"
buttonSticky01["origin_x"] = 0
buttonSticky01["origin_y"] = pgvar.pygame_window_height - 160
buttonSticky01["width"] = pgvar.UI_sideBar_width
buttonSticky01["height"] = 20
buttonSticky01["label_txt"] = "Sticky 01"
buttonSticky01["type"] = "sticky"
buttonSticky01["enabled"] = False
buttonSticky01["color"] = pgvar.UI_button_color
buttonSticky01["group"] = "sticky01"
buttonSticky01["visible"] = True

buttonSticky02 = {}
buttonSticky02["name"] = "sticky02"
buttonSticky02["origin_x"] = 0
buttonSticky02["origin_y"] = pgvar.pygame_window_height - 180
buttonSticky02["width"] = pgvar.UI_sideBar_width
buttonSticky02["height"] = 20
buttonSticky02["label_txt"] = "Sticky 02"
buttonSticky02["type"] = "sticky"
buttonSticky02["enabled"] = False
buttonSticky02["color"] = pgvar.UI_button_color
buttonSticky02["group"] = "sticky02"
buttonSticky02["visible"] = True

buttonSticky03 = {}
buttonSticky03["name"] = "sticky03"								# button_name
buttonSticky03["origin_x"] = 0									# button_origin_x
buttonSticky03["origin_y"] = pgvar.pygame_window_height - 200		# button_origin_y
buttonSticky03["width"] = pgvar.UI_sideBar_width					# button_width
buttonSticky03["height"] = 20										# button_height
buttonSticky03["label_txt"] = "Sticky 03"							# button_label_txt
buttonSticky03["type"] = "sticky"									# buttonType
buttonSticky03["enabled"] = False									# buttonEnabled
buttonSticky03["color"] = pgvar.UI_button_color 					# buttonColor
buttonSticky03["group"] = "sticky03"								# buttonGroup
buttonSticky03["visible"] = True									# buttonVisible

labelSticky = {}
labelSticky["name"] = "sticky_label"
labelSticky["origin_x"] = 0
labelSticky["origin_y"] = pgvar.pygame_window_height - 220
labelSticky["width"] = pgvar.UI_sideBar_width
labelSticky["height"] = 20
labelSticky["label_txt"] = "Sticky Buttons"
labelSticky["type"] = "label"
labelSticky["enabled"] = True
labelSticky["color"] = pgvar.UI_label_color
labelSticky["group"] = "sticky_buttons"
labelSticky["visible"] = True

labelGroup01 = {}
labelGroup01["name"] = "group01_label"					# button_name
labelGroup01["origin_x"] = 0								# button_origin_x
labelGroup01["origin_y"] = pgvar.pygame_window_height - 300		# button_origin_y
labelGroup01["width"] = pgvar.UI_sideBar_width					# button_width
labelGroup01["height"] = 20								# button_height
labelGroup01["label_txt"] = "Group 01"					# button_label_txt
labelGroup01["type"] = "label"							# buttonType
labelGroup01["enabled"] = False							# buttonEnabled
labelGroup01["color"] = pgvar.UI_label_color 					# buttonColor
labelGroup01["group"] = "group01"							# buttonGroup
labelGroup01["visible"] = True							# buttonVisible

bGroup01Button01 = {}
bGroup01Button01["name"] = "Group01Button01"					# button_name
bGroup01Button01["origin_x"] = 0								# button_origin_x
bGroup01Button01["origin_y"] = pgvar.pygame_window_height - 280		# button_origin_y
bGroup01Button01["width"] = pgvar.UI_sideBar_width					# button_width
bGroup01Button01["height"] = 20								# button_height
bGroup01Button01["label_txt"] = "Group 01 Button 01"			# button_label_txt
bGroup01Button01["type"] = "group"							# buttonType
bGroup01Button01["enabled"] = True							# buttonEnabled
bGroup01Button01["color"] = pgvar.UI_button_selected_color			# buttonColor
bGroup01Button01["group"] = "group01"							# buttonGroup
bGroup01Button01["visible"] = True							# buttonVisible

bGroup01Button02 = {}
bGroup01Button02["name"] = "Group01Button02"						# button_name
bGroup01Button02["origin_x"] = 0									# button_origin_x
bGroup01Button02["origin_y"] = pgvar.pygame_window_height - 260	# button_origin_y
bGroup01Button02["width"] = pgvar.UI_sideBar_width				# button_width
bGroup01Button02["height"] = 20									# button_height
bGroup01Button02["label_txt"] = "Group 01 Button 02"				# button_label_txt
bGroup01Button02["type"] = "group"								# buttonType
bGroup01Button02["enabled"] = False								# buttonEnabled
bGroup01Button02["color"] = pgvar.UI_button_color					# buttonColor
bGroup01Button02["group"] = "group01"								# buttonGroup
bGroup01Button02["visible"] = True								# buttonVisible

labelGroup02 = {}
labelGroup02["name"] = "group02_label"							# button_name
labelGroup02["origin_x"] = 0										# button_origin_x
labelGroup02["origin_y"] = pgvar.pygame_window_height - 360		# button_origin_y
labelGroup02["width"] = pgvar.UI_sideBar_width					# button_width
labelGroup02["height"] = 20										# button_height
labelGroup02["label_txt"] = "Group 02"							# button_label_txt
labelGroup02["type"] = "label"									# buttonType
labelGroup02["enabled"] = False									# buttonEnabled
labelGroup02["color"] = pgvar.UI_label_color 						# buttonColor
labelGroup02["group"] = "group02"									# buttonGroup
labelGroup02["visible"] = True									# buttonVisible

bGroup02Button01 = {}
bGroup02Button01["name"] = "Group02Button01"						# button_name
bGroup02Button01["origin_x"] = 0									# button_origin_x
bGroup02Button01["origin_y"] = pgvar.pygame_window_height - 340	# button_origin_y
bGroup02Button01["width"] = pgvar.UI_sideBar_width / 2				# button_width
bGroup02Button01["height"] = 20									# button_height
bGroup02Button01["label_txt"] = "OptionA"							# button_label_txt
bGroup02Button01["type"] = "group"								# buttonType
bGroup02Button01["enabled"] = True								# buttonEnabled
bGroup02Button01["color"] = pgvar.UI_button_selected_color		# buttonColor
bGroup02Button01["group"] = "group02"								# buttonGroup
bGroup02Button01["visible"] = True								# buttonVisible

bGroup02Button02 = {}
bGroup02Button02["name"] = "Group02Button02"						# button_name
bGroup02Button02["origin_x"] = pgvar.UI_sideBar_width / 2			# button_origin_x
bGroup02Button02["origin_y"] = pgvar.pygame_window_height - 340	# button_origin_y
bGroup02Button02["width"] = pgvar.UI_sideBar_width / 2				# button_width
bGroup02Button02["height"] = 20									# button_height
bGroup02Button02["label_txt"] = "OptionB"							# button_label_txt
bGroup02Button02["type"] = "group"								# buttonType
bGroup02Button02["enabled"] = False								# buttonEnabled
bGroup02Button02["color"] = pgvar.UI_button_color					# buttonColor
bGroup02Button02["group"] = "group02"								# buttonGroup
bGroup02Button02["visible"] = True								# buttonVisible

labelGroup03 = {}
labelGroup03["name"] = "group03_label"							# button_name
labelGroup03["origin_x"] = 0										# button_origin_x
labelGroup03["origin_y"] = pgvar.pygame_window_height - 420		# button_origin_y
labelGroup03["width"] = pgvar.UI_sideBar_width					# button_width
labelGroup03["height"] = 20										# button_height
labelGroup03["label_txt"] = "Group 03"							# button_label_txt
labelGroup03["type"] = "label"									# buttonType
labelGroup03["enabled"] = False									# buttonEnabled
labelGroup03["color"] = pgvar.UI_label_color 						# buttonColor
labelGroup03["group"] = "group03"									# buttonGroup
labelGroup03["visible"] = True									# buttonVisible

bGroup03Button01 = {}
bGroup03Button01["name"] = "Group03Button01"						# button_name
bGroup03Button01["origin_x"] = 0									# button_origin_x
bGroup03Button01["origin_y"] = pgvar.pygame_window_height - 400	# button_origin_y
bGroup03Button01["width"] = pgvar.UI_sideBar_width / 3				# button_width
bGroup03Button01["height"] = 20									# button_height
bGroup03Button01["label_txt"] = " A "								# button_label_txt
bGroup03Button01["type"] = "group"								# buttonType
bGroup03Button01["enabled"] = True								# buttonEnabled
bGroup03Button01["color"] = pgvar.UI_button_selected_color		# buttonColor
bGroup03Button01["group"] = "group03"								# buttonGroup
bGroup03Button01["visible"] = True								# buttonVisible

bGroup03Button02 = {}
bGroup03Button02["name"] = "Group03Button02"						# button_name
bGroup03Button02["origin_x"] = pgvar.UI_sideBar_width / 3			# button_origin_x
bGroup03Button02["origin_y"] = pgvar.pygame_window_height - 400	# button_origin_y
bGroup03Button02["width"] = pgvar.UI_sideBar_width / 3				# button_width
bGroup03Button02["height"] = 20									# button_height
bGroup03Button02["label_txt"] = " B "					 			# button_label_txt
bGroup03Button02["type"] = "group"								# buttonType
bGroup03Button02["enabled"] = False								# buttonEnabled
bGroup03Button02["color"] = pgvar.UI_button_color					# buttonColor
bGroup03Button02["group"] = "group03"								# buttonGroup
bGroup03Button02["visible"] = True								# buttonVisible

bGroup03Button03 = {}
bGroup03Button03["name"] = "Group03Button03"						# button_name
bGroup03Button03["origin_x"] = (pgvar.UI_sideBar_width / 3) * 2			# button_origin_x
bGroup03Button03["origin_y"] = pgvar.pygame_window_height - 400	# button_origin_y
bGroup03Button03["width"] = pgvar.UI_sideBar_width / 3				# button_width
bGroup03Button03["height"] = 20									# button_height
bGroup03Button03["label_txt"] = " C "								# button_label_txt
bGroup03Button03["type"] = "group"								# buttonType
bGroup03Button03["enabled"] = False								# buttonEnabled
bGroup03Button03["color"] = pgvar.UI_button_color					# buttonColor
bGroup03Button03["group"] = "group03"								# buttonGroup
bGroup03Button03["visible"] = True								# buttonVisible

allButtons = {}
allButtons[0] = buttonExit			# exit button
allButtons[1] = buttonCommand01		# command 01
allButtons[2] = buttonCommand02		# command 02
allButtons[3] = buttonCommand03		# command 03
allButtons[4] = buttonSticky01		# sticky 01
allButtons[5] = buttonSticky02		# sticky 02
allButtons[6] = buttonSticky03		# sticky 03
allButtons[7] = labelPushy			# pushy button group label
allButtons[8] = labelSticky			# stick button group label
allButtons[9] = labelGroup01			# group01 label
allButtons[10] = bGroup01Button01 	# group01 button 01
allButtons[11] = bGroup01Button02		# group01 button 02
allButtons[12] = labelGroup02 		# group02 label
allButtons[13] = bGroup02Button01 	# group02 Button 01
allButtons[14] = bGroup02Button02 	# group02 Button 02
allButtons[15] = labelGroup03 		# group03 label
allButtons[16] = bGroup03Button01 	# group 03 button 01
allButtons[17] = bGroup03Button02 	# group 03 button 02
allButtons[18] = bGroup03Button03		# group 03 button 03