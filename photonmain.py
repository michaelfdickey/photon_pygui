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
#	/photon_ref.py 		# references, dev notes, style guide, modification instructions

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
import pclass

# ************************************************************************************************#
# ************************************************************************************************#
#	inistial variables (for this module)
# ************************************************************************************************#
# ************************************************************************************************#

moduleName = "photonmain.py"

# ************************************************************************************************#
# ************************************************************************************************#
#	MAIN CODE
# ************************************************************************************************#
# ************************************************************************************************#

####### INITIALIZE DISPLAY ##########

pfunc.initializeDisplay()


####### MAIN PROGRAM LOOP ##########

running = True

while running:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:		
			(mouseX, mouseY) = pygame.mouse.get_pos()						# will run continually while button is held down
			print moduleName, pfunc.lineNum(), "mouseX = ", mouseX, "mouseY = ", mouseY			# this if.even MOUSEBUTTONDOWN **MUST** be under the for event in pygame.event.get() to run only once
			selected_button = pfunc.findButton(pfunc.my_buttons, mouseX, mouseY)
			print moduleName, pfunc.lineNum(), "selected button = ", selected_button

			if selected_button != None:

				if selected_button.button_label_txt == "EXIT":
					print moduleName,  pfunc.lineNum(), "you pressed exit"
					running = False


	# always do this last
	pygame.display.flip()