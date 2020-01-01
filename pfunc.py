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

# FPS related variables
cSec = 0
cFrame = 0
FPS = 0

screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))

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


####### ---------------------------------------------------------------------##########
####### something to do with updating text field buttons                                                                ##########
####### ---------------------------------------------------------------------##########

def enumerateButtons():
	for i, button in enumerate(my_buttons):
		button.display()	


####### ---------------------------------------------------------------------##########
####### Redraw the backgroundm, buttons, screen, etc.                                                                 ##########
####### ---------------------------------------------------------------------##########

def redrawEverything():
	print lineNum(), "redrawEverything() - started"
	
	print lineNum(), "drawing background"
	screen.fill(pgvar.color_background)

	###*** ALERT ALERT ALERT -> re-enable below to get drid and origin working ***
	# check if draw grids is enabled, and draw if so
	if pgui.buttonGrid["enabled"] == True:
		drawGrid()

	
	# check if draw origin is enabled, and draw if so. 
	if pgui.buttonOrigin["enabled"] == True:
		drawOrigin()

		
	print lineNum(), "drawing borders and frames"
	pygame.draw.rect(screen, pgvar.UI_background_color, (0, 0, pgvar.pygame_window_width, pgvar.UI_topBar_height))
	pygame.draw.rect(screen, pgvar.UI_background_color, (0,0, pgvar.UI_sideBar_width, pgvar.pygame_window_height))

	print lineNum(), "redifining buttons and redrawing"
	defineButtons()
	for i, button in enumerate(my_buttons):
		button.display()

	print lineNum(), "redrawEverything() - completed"


####### ---------------------------------------------------------------------##########
####### Functions for counting and displaying FPS (frames per second)                               ##########
####### ---------------------------------------------------------------------##########
def show_fps():
	fps_overlay = pgvar.fps_font.render("FPS:"+str(FPS), True, pgvar.UI_button_txt_color)
	screen.blit(fps_overlay, (pgvar.pygame_window_width - 100, pgvar.pygame_window_height - 30))

def count_fps():
	global cSec, cFrame, FPS, deltatime
	if cSec == time.strftime("%S"):
		cFrame += 1
	else:
		FPS = cFrame
		cFrame = 0
		cSec = time.strftime("%S")


####### ---------------------------------------------------------------------##########
####### Draw Grid lines                                                                                                                                       ##########
####### ---------------------------------------------------------------------##########
def drawGrid():
	# # Draw grid
	grid_width = pgvar.pygame_window_width / 10
	grid_height = pgvar.pygame_window_height / 10

	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [((pgvar.pygame_window_width / 2),0),((pgvar.pygame_window_width / 2 ),pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width,0),(grid_width,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 2,0),(grid_width * 2,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 3,0),(grid_width * 3,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 4,0),(grid_width * 4,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 6,0),(grid_width * 6,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 7,0),(grid_width * 7,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 8,0),(grid_width * 8,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 9,0),(grid_width * 9,pgvar.pygame_window_height)],1)

	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,(pgvar.pygame_window_height / 2)),(pgvar.pygame_window_width, (pgvar.pygame_window_height / 2))],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height), (pgvar.pygame_window_height,grid_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 2), (pgvar.pygame_window_height,grid_height * 2)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 3), (pgvar.pygame_window_height,grid_height * 3)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 4), (pgvar.pygame_window_height,grid_height * 4)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 6), (pgvar.pygame_window_height,grid_height * 6)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 7), (pgvar.pygame_window_height,grid_height * 7)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 8), (pgvar.pygame_window_height,grid_height * 8)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 9), (pgvar.pygame_window_height,grid_height * 9)],1)

####### ---------------------------------------------------------------------##########
####### Draw Origin Lines                                                                                                                                  ##########
####### ---------------------------------------------------------------------##########

def drawOrigin():
	pygame.draw.lines(screen, pgvar.color_red, False, [((pgvar.pygame_window_width / 2),0),((pgvar.pygame_window_width / 2 ),pgvar.pygame_window_height)],2)
	pygame.draw.lines(screen, pgvar.color_red, False, [(0,(pgvar.pygame_window_height / 2)),(pgvar.pygame_window_width, (pgvar.pygame_window_height / 2))],2)



