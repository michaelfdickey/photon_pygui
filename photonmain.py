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
import pfunc
import pgui
import pclass
import pbproc

# ************************************************************************************************#
# ************************************************************************************************#
#	inistial variables (for this module)
# ************************************************************************************************#
# ************************************************************************************************#

moduleName = "photonmain.py"
screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))

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

	
	if pgui.buttonFPS["enabled"] == True:
		pygame.draw.rect(screen, pgvar.color_blue, (pgvar.pygame_window_width - 100, pgvar.pygame_window_height - 30, 80, 20))   
		pfunc.count_fps()
		pfunc.show_fps()


	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False




		if event.type == pygame.MOUSEBUTTONDOWN:		
			(mouseX, mouseY) = pygame.mouse.get_pos()											# will run continually while button is held down
			print moduleName, pfunc.lineNum(), "mouseX = ", mouseX, "mouseY = ", mouseY			# this if.even MOUSEBUTTONDOWN **MUST** be under the for event in pygame.event.get() to run only once
			selected_button = pfunc.findButton(pfunc.my_buttons, mouseX, mouseY)
			print moduleName, pfunc.lineNum(), "selected button = ", selected_button

			if selected_button != None:

				if selected_button.button_label_txt == "EXIT":
					print moduleName,  pfunc.lineNum(), "you pressed exit"
					running = False

				
				# # # PUSHY EVENT processing # # # 

				if selected_button.buttonType == "pushy":
					print moduleName, pfunc.lineNum(), "running MOUSEBUTTONDOWN pushy event"
					print moduleName, pfunc.lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = pgvar.UI_button_click_color
					print moduleName, pfunc.lineNum(), "selected_button.color now : ", selected_button.color			
					selected_button.buttonEnabled = True
					print moduleName, pfunc.lineNum(), "clicked button is a pushy temporary button"

					if selected_button.button_name == "command01":
						print moduleName, pfunc.lineNum(), "you clicked command01"
						pgui.buttonCommand01["enabled"] = True
						pgui.buttonCommand01["color"] = pgvar.UI_button_click_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()
						print moduleName, pfunc.lineNum(), "running code for Command01"
						# command01 function call goes here:

					if selected_button.button_name == "command02":
						print moduleName, pfunc.lineNum(), "you clicked command02"
						pgui.buttonCommand02["enabled"] = True
						pgui.buttonCommand02["color"] = pgvar.UI_button_click_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()
						print moduleName, pfunc.lineNum(), "running code for Command02"
						# command02 function call goes here:

					if selected_button.button_name == "command03":
						print moduleName, pfunc.lineNum(), "you clicked command03"
						pgui.buttonCommand03["enabled"] = True
						pgui.buttonCommand03["color"] = pgvar.UI_button_click_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()
						print moduleName, pfunc.lineNum(), "running code for Command03"
						# command03 function call goes here:

				# # # OTHER BUTTON TYPES # # #

				if selected_button.buttonType == "sticky":
					print moduleName, pfunc.lineNum(), "running sticky event"
					pbproc.updateStickyButtons(selected_button.button_name)

				if selected_button.buttonType == "group":
					print moduleName, pfunc.lineNum(), "running group type button event"
					pbproc.updateGroupButtons(selected_button.button_name)

				if selected_button.buttonType == "dropdown":
					print moduleName, pfunc.lineNum(), "running dropdown button event"
					pbproc.updateDropdownButtons(selected_button.button_name)

				if selected_button.buttonType == "textEntry":
					print moduleName, pfunc.lineNum(), "running text entry event"
					pbproc.updateTextEntry(selected_button.button_name)

				if selected_button.buttonType == "menu":
					print pfunc.lineNum(), "running menu button event"
					pbproc.updateMenuButtons(selected_button.button_name)



		if event.type == pygame.KEYDOWN:
		 	print "you pressed a key"
		 	if pgui.textField01["enabled"] == True:

			 	if event.key == pygame.K_RETURN:
			 		print(pgvar.entered_text)
			 		#entered_text = ""
					pgui.textField01["label_txt"] = pgvar.entered_text
					pgui.textField01["enabled"] = False
					pgui.textField01["color"] = pgvar.UI_text_entry_box_color
					pfunc.defineButtons()
					pfunc.enumerateButtons()

				elif event.key == pygame.K_BACKSPACE:
					pgvar.entered_text = pgvar.entered_text[:-1]
					pgui.textField01["label_txt"] = pgvar.entered_text
					pfunc.defineButtons()
					pfunc.enumerateButtons()

				else:
			 		if len(pgvar.entered_text) <= 15:
						pgvar.entered_text += event.unicode
						print "entered_text", pgvar.entered_text
						pgui.textField01["label_txt"] = pgvar.entered_text
						pfunc.defineButtons()
						pfunc.enumerateButtons()


		if event.type == pygame.MOUSEBUTTONUP:

			if selected_button != None:
				
				if selected_button.buttonType == "pushy":
					print moduleName,pfunc.lineNum(), "running MOUSEBUTTONUP pushy event"
					print moduleName, pfunc.lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = pgvar.UI_button_color 			#reverts button back to normal color after letting go of mouse
					print moduleName, pfunc.lineNum(), "selected_button.color now : ", selected_button.color	
			
					if selected_button.button_name == "command01":
						print moduleName, pfunc.lineNum(), "you clicked command01"
						pgui.buttonCommand01["enabled"] = False
						pgui.buttonCommand01["color"] = pgvar.UI_button_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event command01"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()

					if selected_button.button_name == "command02":
						print moduleName, pfunc.lineNum(), "you clicked command02"
						pgui.buttonCommand02["enabled"] = False
						pgui.buttonCommand02["color"] = pgvar.UI_button_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event command02"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()

					if selected_button.button_name == "command03":
						print moduleName, pfunc.lineNum(), "you clicked command03"
						pgui.buttonCommand03["enabled"] = False
						pgui.buttonCommand03["color"] = pgvar.UI_button_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event command03"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()


			for i, button in enumerate(pfunc.my_buttons):
				button.display()	


	# always do this last
	pygame.display.flip()