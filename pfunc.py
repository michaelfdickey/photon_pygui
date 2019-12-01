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

# pfunc.py

moduleName = "pfunc.py"

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
import pgui
import pclass
#import pbproc

# ************************************************************************************************#
# ************************************************************************************************#
#	initial variables for this module
# ************************************************************************************************#
# ************************************************************************************************#

my_buttons = []			#initializes my_buttons list, each button is added to this for display
buttonToDraw = {}			#each button is loaded into this dictionary, added to my_buttons list

# ************************************************************************************************#
# ************************************************************************************************#
#	functions
# ************************************************************************************************#
# ************************************************************************************************#

####### -------------------------------------##########
####### for printing Linu Number when debugging  ##########
####### -------------------------------------##########

def lineNum():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


####### -------------------------------------##########
####### Initializes the UI and display screen       ##########
####### -------------------------------------##########

def initializeDisplay():
	print moduleName, lineNum(), "starting MAIN code"
	print moduleName, lineNum(), "- initializing pygame display"

	# # Pygame display	
	screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))
	pygame.display.set_caption('My Program Name')

	# # #  draw background
	print moduleName, lineNum(), "- drawing background"
	screen.fill(pgvar.color_background)

	# # draw borders & frames for interface
	print moduleName, lineNum(), "- drawing borders and frames"
	pygame.draw.rect(screen, pgvar.UI_background_color, (0, 0, pgvar.pygame_window_width, pgvar.UI_topBar_height))
	pygame.draw.rect(screen, pgvar.UI_background_color, (0,0, pgvar.UI_sideBar_width, pgvar.pygame_window_height))

	# # draw buttons!
	print moduleName, lineNum(), "- drawing buttons"

	defineButtons()
	
	for i, button in enumerate(my_buttons):
		button.display()
	
	print moduleName, lineNum(), "initializing display completed"



####### ---------------------------------------------------------------------##########
####### takes all buttons defined in dictionary and adds them to a list  for drawing   ##########
####### ---------------------------------------------------------------------##########
def defineButtons():
	del my_buttons[:] 	# this clears and resets the my_buttons list, other it just keeps getting appended

	# source info for this part: https://realpython.com/iterate-through-dictionary-python/
	print moduleName, lineNum(), "defineButtons() - started" 
	# iterates through the nested button dictionary, dumps each button into buttonToDraw, then displays ads to the list
	for allButtonsID, allButtonsValue in pgui.allButtons.items():
		for key in allButtonsValue:
			buttonToDraw[key] = allButtonsValue[key]

		### -------------------------- ###
		button_name = buttonToDraw["name"]
		button_origin_x = buttonToDraw["origin_x"]
		button_origin_y = buttonToDraw["origin_y"]
		button_width = buttonToDraw["width"]
		button_height = buttonToDraw["height"]
		button_label_txt = buttonToDraw["label_txt"]
		buttonType = buttonToDraw["type"]
		buttonEnabled = buttonToDraw["enabled"]
		buttonColor = buttonToDraw["color"]
		buttonGroup = buttonToDraw["group"]
		buttonVisible = buttonToDraw["visible"]

		# define button then add button to display list
		created_button = pclass.Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
		my_buttons.append(created_button)
		#print " my_buttons length: ", len(my_buttons)


	print moduleName, lineNum(), "defineButtons() - completed"


####### ---------------------------------------------------------------------##########
####### this determines what button has been clicked on                                                                ##########
####### ---------------------------------------------------------------------##########
def findButton(buttons, x, y):
	for b in buttons:
		if x <= b.x + b.x_width:
			if x >= b.x:
				if y >= b.y:
					if y <= b.y + b.y_height:
						print moduleName, lineNum(), "selected button label_txt = ", b.button_name
						return b
	return None