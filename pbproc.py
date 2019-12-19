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