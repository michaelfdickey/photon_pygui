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

# pbproc.py

moduleName = "pbproc.py"

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
#import pclass
#import pbproc


# ************************************************************************************************#
# ************************************************************************************************#
#	Local Variables
# ************************************************************************************************#
# ************************************************************************************************#

screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))


# ************************************************************************************************#
# ************************************************************************************************#
#	Button Processing
# ************************************************************************************************#
# ************************************************************************************************#


####### -------------------------------------##########
####### Sticky Buttons 					           ##########
####### -------------------------------------##########

def updateStickyButtons(selected_button):
	print moduleName, pfunc.lineNum(), "updateStickyButtons() - started"
	print moduleName, pfunc.lineNum(), "selected_button = ", selected_button

	"""
	# for sticky buttons, iterate through nested allButtons dictionary and flip buttonEnabled
	for allButtonsID, allButtonsValue in allButtons.items():
		for key in allButtonsValue:
			#print moduleName, pfunc.lineNum(), "key", key
			#buttonToCheck[key] = allButtonsValue[key]
			#print moduleName, pfunc.lineNum(), "buttonToCheck", key, allButtonsValue[key]
			if allButtonsValue[key] == "sticky":
				print moduleName, pfunc.lineNum(), "found a sticky button"
				print moduleName, pfunc.lineNum(), "key, ", key, "value", allButtonsValue[key]
				#print moduleName, pfunc.lineNum(), "buttonToCheck", key, allButtonsValue[key]
	"""
	
	if selected_button == "sticky01":
		if pgui.buttonSticky01["enabled"] == False:
			print moduleName, pfunc.lineNum(), "sticky01 button found"
			pgui.buttonSticky01["enabled"] = True
			pgui.buttonSticky01["color"] = pgvar.UI_button_selected_color
			print moduleName, pfunc.lineNum(), "flipped sticky01 from false to true"
			pfunc.defineButtons()	
			
		elif pgui.buttonSticky01["enabled"] == True:
			print moduleName, pfunc.lineNum(), "sticky01 button found"
			pgui.buttonSticky01["enabled"] = False
			pgui.buttonSticky01["color"] = pgvar.UI_button_color
			print moduleName, pfunc.lineNum(), "flipped stick01 from true to false"
			pfunc.defineButtons()

	if selected_button == "sticky02":
		if pgui.buttonSticky02["enabled"] == False:
			print moduleName, pfunc.lineNum(), "sticky02 button found"
			pgui.buttonSticky02["enabled"] = True
			pgui.buttonSticky02["color"] = pgvar.UI_button_selected_color
			print moduleName, pfunc.lineNum(), "flipped sticky02 from false to true"
			pfunc.defineButtons()	
			
		elif pgui.buttonSticky02["enabled"] == True:
			print moduleName, pfunc.lineNum(), "sticky02 button found"
			pgui.buttonSticky02["enabled"] = False
			pgui.buttonSticky02["color"] = pgvar.UI_button_color
			print moduleName, pfunc.lineNum(), "flipped sticky02 from true to false"
			pfunc.defineButtons()

	if selected_button == "sticky03":
		if pgui.buttonSticky03["enabled"] == False:
			print moduleName, pfunc.lineNum(), "sticky03 button found"
			pgui.buttonSticky03["enabled"] = True
			pgui.buttonSticky03["color"] = pgvar.UI_button_selected_color
			print moduleName, pfunc.lineNum(), "flipped sticky03 from false to true"
			pfunc.defineButtons()	
			
		elif pgui.buttonSticky03["enabled"] == True:
			print moduleName, pfunc.lineNum(), "sticky03 button found"
			pgui.buttonSticky03["enabled"] = False
			pgui.buttonSticky03["color"] = pgvar.UI_button_color
			print moduleName, pfunc.lineNum(), "flipped sticky03 from true to false"
			pfunc.defineButtons()		


	# # # FPS BUTTON
	if selected_button == "fps":
		if pgui.buttonFPS["enabled"] == False:
			pgui.buttonFPS["enabled"] = True
			pgui.buttonFPS["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
			
		elif pgui.buttonFPS["enabled"] == True:
			pgui.buttonFPS["enabled"] = False
			pgui.buttonFPS["color"] = pgvar.UI_button_color
			pfunc.redrawEverything()

	# # # Scale BUTTON
	if selected_button == "scale":
		if pgui.buttonScale["enabled"] == False:
			pgui.buttonScale["enabled"] = True
			pgui.buttonScale["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
			
		elif pgui.buttonScale["enabled"] == True:
			pgui.buttonScale["enabled"] = False
			pgui.buttonScale["color"] = pgvar.UI_button_color
			pfunc.redrawEverything()

	# # # GRID BUTTON
	if selected_button == "grid":
		if pgui.buttonGrid["enabled"] == False:
			pgui.buttonGrid["enabled"] = True
			pgui.buttonGrid["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
			pfunc.redrawEverything()
			
		elif pgui.buttonGrid["enabled"] == True:
			pgui.buttonGrid["enabled"] = False
			pgui.buttonGrid["color"] = pgvar.UI_button_color
			pfunc.defineButtons()
			pfunc.redrawEverything()


	# # # ORIGIN BUTTON
	if selected_button == "origin":
		if pgui.buttonOrigin["enabled"] == False:
			pgui.buttonOrigin["enabled"] = True
			pgui.buttonOrigin["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
			pfunc.redrawEverything()
			
		elif pgui.buttonOrigin["enabled"] == True:
			pgui.buttonOrigin["enabled"] = False
			pgui.buttonOrigin["color"] = pgvar.UI_button_color
			pfunc.defineButtons()
			pfunc.redrawEverything()



####### -------------------------------------##########
####### Group Buttons 					           ##########
####### -------------------------------------##########

def updateGroupButtons(selected_button):
	print moduleName, pfunc.lineNum(), "running update group buttons"

	# # Group 01 processing
	if selected_button == "Group01Button01":
		
		if pgui.bGroup01Button01["enabled"] == True:
			pgui.bGroup01Button01["enabled"] = False
			pgui.bGroup01Button01["color"] = pgvar.UI_button_color
			pgui.bGroup01Button02["enabled"] = True
			pgui.bGroup01Button02["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
		
		elif pgui.bGroup01Button01["enabled"] == False:
			pgui.bGroup01Button01["enabled"] = True
			pgui.bGroup01Button01["color"] = pgvar.UI_button_selected_color
			pgui.bGroup01Button02["enabled"] = False
			pgui.bGroup01Button02["color"] = pgvar.UI_button_color
			pfunc.defineButtons()	

	if selected_button == "Group01Button02":
		
		if pgui.bGroup01Button02["enabled"] == True:
			pgui.bGroup01Button02["enabled"] = False
			pgui.bGroup01Button02["color"] = pgvar.UI_button_color
			pgui.bGroup01Button01["enabled"] = True
			pgui.bGroup01Button01["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
		
		elif pgui.bGroup01Button02["enabled"] == False:
			pgui.bGroup01Button02["enabled"] = True
			pgui.bGroup01Button02["color"] = pgvar.UI_button_selected_color
			pgui.bGroup01Button01["enabled"] = False
			pgui.bGroup01Button01["color"] = pgvar.UI_button_color
			pfunc.defineButtons()

	# # Group 02 processing
	if selected_button == "Group02Button01":
		
		if pgui.bGroup02Button01["enabled"] == True:
			pgui.bGroup02Button01["enabled"] = False
			pgui.bGroup02Button01["color"] = pgvar.UI_button_color
			pgui.bGroup02Button02["enabled"] = True
			pgui.bGroup02Button02["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
		
		elif pgui.bGroup02Button01["enabled"] == False:
			pgui.bGroup02Button01["enabled"] = True
			pgui.bGroup02Button01["color"] = pgvar.UI_button_selected_color
			pgui.bGroup02Button02["enabled"] = False
			pgui.bGroup02Button02["color"] = pgvar.UI_button_color
			pfunc.defineButtons()	

	if selected_button == "Group02Button02":
		
		if pgui.bGroup02Button02["enabled"] == True:
			pgui.bGroup02Button02["enabled"] = False
			pgui.bGroup02Button02["color"] = pgvar.UI_button_color
			pgui.bGroup02Button01["enabled"] = True
			pgui.bGroup02Button01["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
		
		elif pgui.bGroup02Button02["enabled"] == False:
			pgui.bGroup02Button02["enabled"] = True
			pgui.bGroup02Button02["color"] = pgvar.UI_button_selected_color
			pgui.bGroup02Button01["enabled"] = False
			pgui.bGroup02Button01["color"] = pgvar.UI_button_color
			pfunc.defineButtons()

	# # Group 03 processing
	if selected_button == "Group03Button01":
		
		if pgui.bGroup03Button01["enabled"] == False:
			pgui.bGroup03Button01["enabled"] = True
			pgui.bGroup03Button01["color"] = pgvar.UI_button_selected_color
			
			pgui.bGroup03Button02["enabled"] = False
			pgui.bGroup03Button02["color"] = pgvar.UI_button_color
			
			pgui.bGroup03Button03["enabled"] = False
			pgui.bGroup03Button03["color"] = pgvar.UI_button_color

			pfunc.defineButtons()	

	if selected_button == "Group03Button02":
		
		if pgui.bGroup03Button02["enabled"] == False:
			pgui.bGroup03Button02["enabled"] = True
			pgui.bGroup03Button02["color"] = pgvar.UI_button_selected_color
			
			pgui.bGroup03Button01["enabled"] = False
			pgui.bGroup03Button01["color"] = pgvar.UI_button_color
			
			pgui.bGroup03Button03["enabled"] = False
			pgui.bGroup03Button03["color"] = pgvar.UI_button_color

			pfunc.defineButtons()	

	if selected_button == "Group03Button03":
		
		if pgui.bGroup03Button03["enabled"] == False:
			pgui.bGroup03Button03["enabled"] = True
			pgui.bGroup03Button03["color"] = pgvar.UI_button_selected_color
			
			pgui.bGroup03Button01["enabled"] = False
			pgui.bGroup03Button01["color"] = pgvar.UI_button_color
			
			pgui.bGroup03Button02["enabled"] = False
			pgui.bGroup03Button02["color"] = pgvar.UI_button_color

			pfunc.defineButtons()	

## ############################################################################################
## UPDATE DROPDOWN BUTTONS
## ############################################################################################

def updateDropdownButtons(selected_button):
	print pfunc.lineNum(), "running update Dropdown buttons"

	if selected_button == "dropdown01opener":
		if pgui.bDropdown01opener["enabled"] == False:
			print pfunc.lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			# update this button
			pgui.bDropdown01opener["enabled"] = True
			pgui.bDropdown01opener["color"] = pgvar.UI_button_selected_color
			pgui.bDropdown01opener["label_txt"] = "<<"

			# update associated buttons
			pgui.bDropdown01option01["visible"] = True	
			pgui.bDropdown01option02["visible"] = True
			pgui.bDropdown01option03["visible"] = True

			pfunc.defineButtons()	

			print pfunc.lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			print pfunc.lineNum(), pgui.bDropdown01opener["name"], "enabled:", pgui.bDropdown01opener["enabled"], "visible:", pgui.bDropdown01opener["visible"]
			
		elif pgui.bDropdown01opener["enabled"] == True:
			print " --------------------------------------- "
			print pfunc.lineNum(), "STARTED dropdown true to false "
			print " --------------------------------------- "

			# udapte this button
			print pfunc.lineNum(), pgui.bDropdown01opener["name"], "enabled was: ", pgui.bDropdown01opener["enabled"]
			pgui.bDropdown01opener["enabled"] = False
			pgui.bDropdown01opener["color"] = pgvar.UI_button_color
			pgui.bDropdown01opener["label_txt"] = ">>"
			print pfunc.lineNum(), pgui.bDropdown01opener["name"], "enabled:", pgui.bDropdown01opener["enabled"], "visible:", pgui.bDropdown01opener["visible"]

			# update associated buttons
			pgui.bDropdown01option01["visible"] = False
			pgui.bDropdown01option02["visible"] = False
			pgui.bDropdown01option03["visible"] = False
			print pfunc.lineNum(), "buttons27,28,29 visible:", pgui.bDropdown01option01["visible"], pgui.bDropdown01option02["visible"], pgui.bDropdown01option03["visible"]

			#screen.fill(pgvar.background_color)
			pfunc.defineButtons()
			pfunc.redrawEverything()

			print pfunc.lineNum(), pgui.bDropdown01opener["name"], "enabled:", pgui.bDropdown01opener["enabled"], "visible:", pgui.bDropdown01opener["visible"]
			print " --------------------------------------- "
			print pfunc.lineNum(), "FINISHED dropdown true to false "
			print " --------------------------------------- "
			print type(pgui.bDropdown01option01["visible"])

	if selected_button == "dropdown01option01":
		if pgui.bDropdown01opener["enabled"] == True:
			pgui.lDropdown01TEXT["label_txt"] = "Option 01"
			pgui.bDropdown01option01["color"] = pgvar.UI_button_selected_color
			pgui.bDropdown01option02["color"] = pgvar.UI_button_color
			pgui.bDropdown01option03["color"] = pgvar.UI_button_color
			pfunc.defineButtons()

	if selected_button == "dropdown01option02":
		if pgui.bDropdown01opener["enabled"] == True: 
			pgui.lDropdown01TEXT["label_txt"] = "Option 02"
			pgui.bDropdown01option01["color"] = pgvar.UI_button_color
			pgui.bDropdown01option02["color"] = pgvar.UI_button_selected_color
			pgui.bDropdown01option03["color"] = pgvar.UI_button_color		
			pfunc.defineButtons()

	if selected_button == "dropdown01option03":
		if pgui.bDropdown01opener["enabled"] == True:
			pgui.lDropdown01TEXT["label_txt"] = "Option 03"
			pgui.bDropdown01option01["color"] = pgvar.UI_button_color
			pgui.bDropdown01option02["color"] = pgvar.UI_button_color
			pgui.bDropdown01option03["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()

	if selected_button == "dropdown01TEXT":
		if pgui.lDropdown01TEXT["label_txt"] != "- select -":
			if pgui.lDropdown01TEXT["enabled"] == False:
				pgui.lDropdown01TEXT["enabled"] = True
				pgui.lDropdown01TEXT["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()	
				pfunc.redrawEverything()
				
			elif pgui.lDropdown01TEXT["enabled"] == True:
				pgui.lDropdown01TEXT["enabled"] = False
				pgui.lDropdown01TEXT["color"] = pgvar.UI_button_color
				pfunc.defineButtons()
				pfunc.redrawEverything()


## ############################################################################################
## UPDATE TEXT ENTRY BUTTONS
## ############################################################################################

def updateTextEntry(selected_button):
	if selected_button == "textField01":
		if pgui.textField01["enabled"] == False:
			pgui.textField01["enabled"] = True
			pgui.textField01["color"] = pgvar.UI_text_entry_box_color_active
			pfunc.defineButtons()
			#enumerateButtons()

		elif pgui.textField01["enabled"] == True:
			pgui.textField01["enabled"] = False
			pgui.textField01["color"] = pgvar.UI_text_entry_box_color
			pfunc.defineButtons()


## ############################################################################################
## UPDATE MENU BUTTONS
## ############################################################################################

def updateMenuButtons(selected_button):
	print pfunc.lineNum(), "running updateMenuButtons"

	## START MENU 01 HANDLING

	if selected_button == "menu01":
		print pfunc.lineNum(), "menu01 was clicked on"
		print pfunc.lineNum(), pgui.bMenu01["name"], "is ", pgui.bMenu01["enabled"]
		
		if pgui.bMenu01["enabled"] == False:
			print "was false, turning to true"
			
			pgui.bMenu01["enabled"] = True
			pgui.bMenu01["color"] = pgvar.UI_button_selected_color
			pgui.bMenu01option01["visible"] = True
			pgui.bMenu01option02["visible"] = True
			pgui.bMenu01option03["visible"] = True			
			pgui.bMenu01option04["visible"] = True
			pgui.bMenu01option05["visible"] = True

			print pfunc.lineNum(), "~", pgui.bMenu01option01["name"], "Visible=", pgui.bMenu01option01["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option02["name"], "Visible=", pgui.bMenu01option02["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option03["name"], "Visible=", pgui.bMenu01option03["visible"]			
			print pfunc.lineNum(), "~", pgui.bMenu01option04["name"], "Visible=", pgui.bMenu01option04["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option05["name"], "Visible=", pgui.bMenu01option05["visible"]

			pfunc.defineButtons()
			
		elif pgui.bMenu01["enabled"] == True:
			print pfunc.lineNum(), "was true, turning to false"
			pgui.bMenu01["enabled"] = False
			pgui.bMenu01["color"] = pgvar.UI_button_color
			pgui.bMenu01option01["visible"] = False
			pgui.bMenu01option02["visible"] = False
			pgui.bMenu01option03["visible"] = False			
			pgui.bMenu01option04["visible"] = False
			pgui.bMenu01option05["visible"] = False		
			
			print pfunc.lineNum(), "~", pgui.bMenu01option01["name"], "Visible=", pgui.bMenu01option01["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option02["name"], "Visible=", pgui.bMenu01option02["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option03["name"], "Visible=", pgui.bMenu01option03["visible"]			
			print pfunc.lineNum(), "~", pgui.bMenu01option04["name"], "Visible=", pgui.bMenu01option04["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option05["name"], "Visible=", pgui.bMenu01option05["visible"]

			pfunc.defineButtons()
			pfunc.redrawEverything()

	if selected_button == "menu01option01":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Monday ~~"
			if pgui.bMenu01option01["enabled"] == False:
				pgui.bMenu01option01["enabled"] = True
				pgui.bMenu01option01["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option01["enabled"] == True:
				pgui.bMenu01option01["enabled"] = False
				pgui.bMenu01option01["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option02":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Tuesday ~~"
			if pgui.bMenu01option02["enabled"] == False:
				pgui.bMenu01option02["enabled"] = True
				pgui.bMenu01option02["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option02["enabled"] == True:
				pgui.bMenu01option02["enabled"] = False
				pgui.bMenu01option02["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option03":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Wednesday ~~"
			if pgui.bMenu01option03["enabled"] == False:
				pgui.bMenu01option03["enabled"] = True
				pgui.bMenu01option03["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option03["enabled"] == True:
				pgui.bMenu01option03["enabled"] = False
				pgui.bMenu01option03["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option04":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Thursday ~~"
			if pgui.bMenu01option04["enabled"] == False:
				pgui.bMenu01option04["enabled"] = True
				pgui.bMenu01option04["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option04["enabled"] == True:
				pgui.bMenu01option04["enabled"] = False
				pgui.bMenu01option04["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option05":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Friday ~~"
			if pgui.bMenu01option05["enabled"] == False:
				pgui.bMenu01option05["enabled"] = True
				pgui.bMenu01option05["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option05["enabled"] == True:
				pgui.bMenu01option05["enabled"] = False
				pgui.bMenu01option05["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	## END MENU 01 HANDLING

	## START MENU 02 HANDLING

	if selected_button == "menu02":
		if pgui.bMenu02["enabled"] == False:
			# flip this menu button
			pgui.bMenu02["enabled"] = True
			pgui.bMenu02["color"] = pgvar.UI_button_selected_color
			
			# flip related buttons in the group
			pgui.bMenu02popup01["visible"] = True
			pgui.bMenu02popup02["visible"] = True
			pgui.bMenu02popup03["visible"] = True			

			pfunc.defineButtons()

		elif pgui.bMenu02["enabled"] == True:
			# flip this menu button
			pgui.bMenu02["enabled"] = False
			pgui.bMenu02["color"] = pgvar.UI_button_color
			
			# flip related buttons in the group
			pgui.bMenu02popup01["visible"] = False
			pgui.bMenu02popup02["visible"] = False
			pgui.bMenu02popup03["visible"] = False			

			pfunc.defineButtons()
			pfunc.redrawEverything()	

	if selected_button == "menu02popup01":
		if pgui.bMenu02["enabled"] == True:
			if pgui.bMenu02popup01["enabled"] == False:
				#flip this menu buttone
				pgui.bMenu02popup01["enabled"] = True
				pgui.bMenu02popup01["color"] = pgvar.UI_button_selected_color

				#flip related buttons
				pgui.menu02popup01element01["visible"] = True
				pgui.menu02popup01element02["visible"] = True
				pgui.menu02popup01element03["visible"] = True
				pgui.menu02popup01element04["visible"] = True
				pgui.menu02popup01element05["visible"] = True
				pgui.menu02popup01element06["visible"] = True
				pgui.menu02popup01element07["visible"] = True	
				pgui.menu02popup01element08["visible"] = True

				pfunc.defineButtons()
				#pfunc.redrawEverything()	
		
			elif pgui.bMenu02popup01["enabled"] == True:
				#flop this menu buttone
				pgui.bMenu02popup01["enabled"] = False
				pgui.bMenu02popup01["color"] = pgvar.UI_button_color

				pgui.menu02popup01element01["visible"] = False
				pgui.menu02popup01element02["visible"] = False
				pgui.menu02popup01element03["visible"] = False
				pgui.menu02popup01element04["visible"] = False
				pgui.menu02popup01element05["visible"] = False
				pgui.menu02popup01element06["visible"] = False
				pgui.menu02popup01element07["visible"] = False	
				pgui.menu02popup01element08["visible"] = False

				pfunc.defineButtons()
				pfunc.redrawEverything()	

	## END START MENU 02 HANDLING