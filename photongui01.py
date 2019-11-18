# DEV LOG
# 2019-11-03 - next, move pushy button processing out of main loop into it's own function call
# - will need a call in mousebuttondown and mousebutton up
# - then create function for group processing

# ************************************************************************************
# 	import modules	#
# ************************************************************************************

import pygame
import random
import math
import sys
import time 			# for FPS functions
import inspect		# for displaying the line number of the code in print commands


# ************************************************************************************
#	initial variables	#
# ************************************************************************************


#py game font
pygame.font.init()							# needs to be called at the start of the program
myfont = pygame.font.SysFont('Arial',15)		# GUI font type and size
fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 15)


#pre-defined colors
black = (0,0,0)
red = (255,0,0)
darkRed = (128,0,0)
green = (0,255,0)
darkGreen = (0,128,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
pink = (255,200,200)
gray = (128,128,128)
yellow = (255,255,0)
gridYellow = (128,128,0)


# interface colors
background_color = (0,0,0)
UI_background_color = (102, 0, 51)				# the color of the bar along the side and top
UI_button_border_color = (153, 127, 76)		# color of the border box around the button
UI_button_color = (204, 0, 102)				# the default color of the button
UI_button_click_color = (255, 128 , 255)		# the color a button turns temporarily when clicked on
UI_label_color = (150,50,100)					# label color 

# interface colors 2
UI_button_group_color = (125, 50, 100)			
UI_button_txt_color = (255,255,0)				# color of text label of button
UI_button_selected_color = (225,100,225)		# color button turns to when toggled on 

## interface formatting
UI_topBar_height = 20
UI_sideBar_width = 120  

# Screen size
pygame_window_width = 1200
pygame_window_height = 1200

# by default, no UI objects are selected at start
selected_uiObject = None					
selected_button = None

# FPS related variables
cSec = 0
cFrame = 0
FPS = 0


# ************************************************************************************
#	initial lists	#

my_uiObjects = []							# this list will hold all the UI elements
display_overlay_origin = []				# list containing the origin line elements
display_overlay_grid = []					# list containing the grid line elements
# ************************************************************************************



# ************************************************************************************
# 	initial dictionaries 		#
selectedButton = {}



# ************************************************************************************************************************
# ************************************************************************************************************************
# 	button dictionaries	#
# ************************************************************************************************************************
# ************************************************************************************************************************


button00 = {}
button00[0] = "exit"
button00[1] = 0
button00[2] = pygame_window_height - 20
button00[3] = UI_sideBar_width
button00[4] = 20
button00[5] = "EXIT"
button00[6] = "pushy"
button00[7] = True
button00[8] = UI_button_color
button00[9] = "button00"
button00[10] = True

button01 = {}
button01[0] = "command01"
button01[1] = 0
button01[2] = pygame_window_height - 60
button01[3] = UI_sideBar_width
button01[4] = 20
button01[5] = "Command 01"
button01[6] = "pushy"
button01[7] = True
button01[8] = UI_button_color
button01[9] = "command01"
button01[10] = True

button02 = {}
button02[0] = "command02"
button02[1] = 0
button02[2] = pygame_window_height - 80
button02[3] = UI_sideBar_width
button02[4] = 20
button02[5] = "Command 02"
button02[6] = "pushy"
button02[7] = True
button02[8] = UI_button_color
button02[9] = "command02"
button02[10] = True

button03 = {}
button03[0] = "command03"
button03[1] = 0
button03[2] = pygame_window_height - 100
button03[3] = UI_sideBar_width
button03[4] = 20
button03[5] = "Command 03"
button03[6] = "pushy"
button03[7] = True
button03[8] = UI_button_color
button03[9] = "command03"
button03[10] = True

button04 = {}
button04[0] = "sticky01"
button04[1] = 0
button04[2] = pygame_window_height - 160
button04[3] = UI_sideBar_width
button04[4] = 20
button04[5] = "Sticky 01"
button04[6] = "sticky"
button04[7] = False
button04[8] = UI_button_color
button04[9] = "sticky01"
button04[10] = True

button05 = {}
button05[0] = "sticky02"
button05[1] = 0
button05[2] = pygame_window_height - 180
button05[3] = UI_sideBar_width
button05[4] = 20
button05[5] = "Sticky 02"
button05[6] = "sticky"
button05[7] = False
button05[8] = UI_button_color
button05[9] = "sticky02"
button05[10] = True

button06 = {}
button06[0] = "sticky03"						# button_name
button06[1] = 0								# button_origin_x
button06[2] = pygame_window_height - 200		# button_origin_y
button06[3] = UI_sideBar_width				# button_width
button06[4] = 20								# button_height
button06[5] = "Sticky 03"						# button_label_txt
button06[6] = "sticky"						# buttonType
button06[7] = False							# buttonEnabled
button06[8] = UI_button_color 				# buttonColor
button06[9] = "sticky03"						# buttonGroup
button06[10] = True							# buttonVisible

button07 = {}
button07[0] = "pushy_label"
button07[1] = 0
button07[2] = pygame_window_height - 120
button07[3] = UI_sideBar_width
button07[4] = 20
button07[5] = "Pushy Buttons"
button07[6] = "label"
button07[7] = True
button07[8] = UI_label_color
button07[9] = "pushy_buttons"
button07[10] = True

button08 = {}
button08[0] = "sticky_label"
button08[1] = 0
button08[2] = pygame_window_height - 220
button08[3] = UI_sideBar_width
button08[4] = 20
button08[5] = "Sticky Buttons"
button08[6] = "label"
button08[7] = True
button08[8] = UI_label_color
button08[9] = "sticky_buttons"
button08[10] = True

button09 = {}
button09[0] = "group01_label"					# button_name
button09[1] = 0								# button_origin_x
button09[2] = pygame_window_height - 300		# button_origin_y
button09[3] = UI_sideBar_width				# button_width
button09[4] = 20								# button_height
button09[5] = "Group 01"						# button_label_txt
button09[6] = "label"							# buttonType
button09[7] = False							# buttonEnabled
button09[8] = UI_label_color 					# buttonColor
button09[9] = "group01"						# buttonGroup
button09[10] = True							# buttonVisible

button10 = {}
button10[0] = "Group01Button01"				# button_name
button10[1] = 0								# button_origin_x
button10[2] = pygame_window_height - 280		# button_origin_y
button10[3] = UI_sideBar_width				# button_width
button10[4] = 20								# button_height
button10[5] = "Group 01 Button 01"				# button_label_txt
button10[6] = "group"							# buttonType
button10[7] = True							# buttonEnabled
button10[8] = UI_button_selected_color		# buttonColor
button10[9] = "group01"						# buttonGroup
button10[10] = True							# buttonVisible

button11 = {}
button11[0] = "Group01Button02"				# button_name
button11[1] = 0								# button_origin_x
button11[2] = pygame_window_height - 260		# button_origin_y
button11[3] = UI_sideBar_width				# button_width
button11[4] = 20								# button_height
button11[5] = "Group 01 Button 02"				# button_label_txt
button11[6] = "group"							# buttonType
button11[7] = False							# buttonEnabled
button11[8] = UI_button_color					# buttonColor
button11[9] = "group01"						# buttonGroup
button11[10] = True							# buttonVisible

button12 = {}
button12[0] = "group02_label"					# button_name
button12[1] = 0								# button_origin_x
button12[2] = pygame_window_height - 360		# button_origin_y
button12[3] = UI_sideBar_width				# button_width
button12[4] = 20								# button_height
button12[5] = "Group 02"						# button_label_txt
button12[6] = "label"							# buttonType
button12[7] = False							# buttonEnabled
button12[8] = UI_label_color 					# buttonColor
button12[9] = "group02"						# buttonGroup
button12[10] = True							# buttonVisible

button13 = {}
button13[0] = "Group02Button01"				# button_name
button13[1] = 0								# button_origin_x
button13[2] = pygame_window_height - 340		# button_origin_y
button13[3] = UI_sideBar_width / 2				# button_width
button13[4] = 20								# button_height
button13[5] = "OptionA"						# button_label_txt
button13[6] = "group"							# buttonType
button13[7] = True							# buttonEnabled
button13[8] = UI_button_selected_color		# buttonColor
button13[9] = "group02"						# buttonGroup
button13[10] = True							# buttonVisible

button14 = {}
button14[0] = "Group02Button02"				# button_name
button14[1] = UI_sideBar_width / 2				# button_origin_x
button14[2] = pygame_window_height - 340		# button_origin_y
button14[3] = UI_sideBar_width / 2				# button_width
button14[4] = 20								# button_height
button14[5] = "OptionB"						# button_label_txt
button14[6] = "group"							# buttonType
button14[7] = False							# buttonEnabled
button14[8] = UI_button_color					# buttonColor
button14[9] = "group02"						# buttonGroup
button14[10] = True							# buttonVisible

button15 = {}
button15[0] = "group03_label"					# button_name
button15[1] = 0								# button_origin_x
button15[2] = pygame_window_height - 420		# button_origin_y
button15[3] = UI_sideBar_width				# button_width
button15[4] = 20								# button_height
button15[5] = "Group 03"						# button_label_txt
button15[6] = "label"							# buttonType
button15[7] = False							# buttonEnabled
button15[8] = UI_label_color 					# buttonColor
button15[9] = "group03"						# buttonGroup
button15[10] = True							# buttonVisible

button16 = {}
button16[0] = "Group03Button01"				# button_name
button16[1] = 0								# button_origin_x
button16[2] = pygame_window_height - 400		# button_origin_y
button16[3] = UI_sideBar_width / 3				# button_width
button16[4] = 20								# button_height
button16[5] = " A "							# button_label_txt
button16[6] = "group"							# buttonType
button16[7] = True							# buttonEnabled
button16[8] = UI_button_selected_color		# buttonColor
button16[9] = "group03"						# buttonGroup
button16[10] = True							# buttonVisible

button17 = {}
button17[0] = "Group03Button02"				# button_name
button17[1] = UI_sideBar_width / 3				# button_origin_x
button17[2] = pygame_window_height - 400		# button_origin_y
button17[3] = UI_sideBar_width / 3				# button_width
button17[4] = 20								# button_height
button17[5] = " B "					 		# button_label_txt
button17[6] = "group"							# buttonType
button17[7] = False							# buttonEnabled
button17[8] = UI_button_color					# buttonColor
button17[9] = "group03"						# buttonGroup
button17[10] = True							# buttonVisible

button18 = {}
button18[0] = "Group03Button03"				# button_name
button18[1] = (UI_sideBar_width / 3) * 2		# button_origin_x
button18[2] = pygame_window_height - 400		# button_origin_y
button18[3] = UI_sideBar_width / 3				# button_width
button18[4] = 20								# button_height
button18[5] = " C "							# button_label_txt
button18[6] = "group"							# buttonType
button18[7] = False							# buttonEnabled
button18[8] = UI_button_color					# buttonColor
button18[9] = "group03"						# buttonGroup
button18[10] = True							# buttonVisible

button19 = {}
button19[0] = "fps"							# button_name
button19[1] = 0								# button_origin_x
button19[2] = pygame_window_height - 460		# button_origin_y
button19[3] = UI_sideBar_width				# button_width
button19[4] = 20								# button_height
button19[5] = " FPS "							# button_label_txt
button19[6] = "sticky"						# buttonType
button19[7] = False							# buttonEnabled
button19[8] = UI_button_color					# buttonColor
button19[9] = "fps"							# buttonGroup
button19[10] = True							# buttonVisible

button20 = {}
button20[0] = "scale"							# button_name
button20[1] = 0								# button_origin_x
button20[2] = pygame_window_height - 480		# button_origin_y
button20[3] = UI_sideBar_width				# button_width
button20[4] = 20								# button_height
button20[5] = "Scale          |<-  --  ->|"			# button_label_txt
button20[6] = "sticky"						# buttonType
button20[7] = False							# buttonEnabled
button20[8] = UI_button_color					# buttonColor
button20[9] = "scale"							# buttonGroup
button20[10] = True							# buttonVisible

button21 = {}
button21[0] = "grid"							# button_name
button21[1] = 0								# button_origin_x
button21[2] = pygame_window_height - 500		# button_origin_y
button21[3] = UI_sideBar_width				# button_width
button21[4] = 20								# button_height
button21[5] = "Grid                          #"				# button_label_txt
button21[6] = "sticky"						# buttonType
button21[7] = False							# buttonEnabled
button21[8] = UI_button_color					# buttonColor
button21[9] = "grid"							# buttonGroup
button21[10] = True							# buttonVisible

button22 = {}
button22[0] = "origin"						# button_name
button22[1] = 0								# button_origin_x
button22[2] = pygame_window_height - 520		# button_origin_y
button22[3] = UI_sideBar_width				# button_width
button22[4] = 20								# button_height
button22[5] = "Origin                      +"				# button_label_txt
button22[6] = "sticky"						# buttonType
button22[7] = False							# buttonEnabled
button22[8] = UI_button_color					# buttonColor
button22[9] = "origin"						# buttonGroup
button22[10] = True							# buttonVisible

button23 = {}
button23[0] = "displayLabel"					# button_name
button23[1] = 0								# button_origin_x
button23[2] = pygame_window_height - 540		# button_origin_y
button23[3] = UI_sideBar_width				# button_width
button23[4] = 20								# button_height
button23[5] = "Display"						# button_label_txt
button23[6] = "label"							# buttonType
button23[7] = False							# buttonEnabled
button23[8] = UI_button_color					# buttonColor
button23[9] = "origin"						# buttonGroup
button23[10] = True							# buttonVisible

button24 = {}
button24[0] = "dropdownLabel"					# button_name
button24[1] = 0								# button_origin_x
button24[2] = pygame_window_height - 600		# button_origin_y
button24[3] = UI_sideBar_width				# button_width
button24[4] = 20								# button_height
button24[5] = "Dropdown 01"					# button_label_txt
button24[6] = "label"							# buttonType
button24[7] = False							# buttonEnabled
button24[8] = UI_button_color					# buttonColor
button24[9] = "dropdown01"					# buttonGroup
button24[10] = True							# buttonVisible

button25 = {}
button25[0] = "dropdown01Label"				# button_name
button25[1] = 0								# button_origin_x
button25[2] = pygame_window_height - 580		# button_origin_y
button25[3] = UI_sideBar_width - 20			# button_width
button25[4] = 20								# button_height
button25[5] = "- select -"						# button_label_txt
button25[6] = "dropdown"						# buttonType
button25[7] = False							# buttonEnabled
button25[8] = UI_button_color					# buttonColor
button25[9] = "dropdown01"					# buttonGroup
button25[10] = True							# buttonVisible

button26 = {}
button26[0] = "dropdown01opener"				# button_name
button26[1] = UI_sideBar_width - 20			# button_origin_x
button26[2] = pygame_window_height - 580		# button_origin_y
button26[3] = 20								# button_width
button26[4] = 20								# button_height
button26[5] = ">>"							# button_label_txt
button26[6] = "dropdown"						# buttonType
button26[7] = False							# buttonEnabled
button26[8] = UI_button_color					# buttonColor
button26[9] = "dropdown01"					# buttonGroup
button26[10] = True							# buttonVisible

button27 = {}
button27[0] = "dropdown01option01"			# button_name
button27[1] = UI_sideBar_width				# button_origin_x
button27[2] = pygame_window_height - 580		# button_origin_y
button27[3] = 140								# button_width
button27[4] = 20								# button_height
button27[5] = " Option 1"						# button_label_txt
button27[6] = "dropdown"						# buttonType
button27[7] = False							# buttonEnabled
button27[8] = UI_button_color					# buttonColor
button27[9] = "dropdown01"					# buttonGroup
button27[10] = False							# buttonVisible

button28 = {}
button28[0] = "dropdown01option02"			# button_name
button28[1] = UI_sideBar_width				# button_origin_x
button28[2] = pygame_window_height - 560		# button_origin_y
button28[3] = 140								# button_width
button28[4] = 20								# button_height
button28[5] = " Option 2"						# button_label_txt
button28[6] = "dropdown"						# buttonType
button28[7] = False							# buttonEnabled
button28[8] = UI_button_color					# buttonColor
button28[9] = "dropdown01"					# buttonGroup
button28[10] = False						# buttonVisible

button29 = {}
button29[0] = "dropdown01option03"			# button_name
button29[1] = UI_sideBar_width				# button_origin_x
button29[2] = pygame_window_height - 540		# button_origin_y
button29[3] = 140								# button_width
button29[4] = 20								# button_height
button29[5] = " Option 3"						# button_label_txt
button29[6] = "dropdown"						# buttonType
button29[7] = False							# buttonEnabledsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
button29[8] = UI_button_color					# buttonColor
button29[9] = "dropdown01"					# buttonGroup
button29[10] = False							# buttonVisible


allButtons = {}
allButtons[0] = button00		# exit button
allButtons[1] = button01		# command 01
allButtons[2] = button02		# command 02
allButtons[3] = button03		# command 03
allButtons[4] = button04		# sticky 01
allButtons[5] = button05		# sticky 02
allButtons[6] = button06		# sticky 03
allButtons[7] = button07		# pushy button group label
allButtons[8] = button08		# stick button group label
allButtons[9] = button09		# group01 label
allButtons[10] = button10 	# group01 button 01
allButtons[11] = button11		# group01 button 02
allButtons[12] = button12		# group02 label
allButtons[13] = button13 	# group02 button 01
allButtons[14] = button14		# group02 button 02
allButtons[15] = button15		# group03 label
allButtons[16] = button16 	# group03 button 01
allButtons[17] = button17		# group03 button 02
allButtons[18] = button18		# group03 button 03
allButtons[19] = button19		# FPS display
allButtons[20] = button20 	# display scale
allButtons[21] = button21 	# display grid
allButtons[22] = button22 	# display origin
allButtons[23] = button23		# display options label
allButtons[24] = button24 	# Dropdown01 - Label
allButtons[25] = button25		# Dropdown01 - selected display
allButtons[26] = button26		# Dropdown01 - opener
allButtons[27] = button27		# Dropdown01 - option1
allButtons[28] = button28		# Dropdown01 - option2
allButtons[29] = button29		# Dropdown01 - option3

# ************************************************************************************************************************
# ************************************************************************************************************************
# 	functions  
# ************************************************************************************************************************
# ************************************************************************************************************************


my_buttons = []			#initializes my_buttons list, each button is added to this for display
buttonToDraw = {}			#each button is loaded into this dictionary, added to my_buttons list


def lineNum():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


# # #########################################################################################
# # # DEFINE BUTTONS
# # #########################################################################################

def defineButtons():
	# source info for this part: https://realpython.com/iterate-through-dictionary-python/
	print lineNum(), "defineButtons() - started" 
	# iterates through the nested button dictionary, dumps each button into buttonToDraw, then displays ads to the list
	for allButtonsID, allButtonsValue in allButtons.items():
		for key in allButtonsValue:
			buttonToDraw[key] = allButtonsValue[key]

		### -------------------------- ###
		button_name = buttonToDraw[0]
		button_origin_x = buttonToDraw[1]
		button_origin_y = buttonToDraw[2]
		button_width = buttonToDraw[3]
		button_height = buttonToDraw[4]
		button_label_txt = buttonToDraw[5]
		buttonType = buttonToDraw[6]
		buttonEnabled = buttonToDraw[7]
		buttonColor = buttonToDraw[8]
		buttonGroup = buttonToDraw[9]
		buttonVisible = buttonToDraw[10]

		# define button then add button to display list
		created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
		my_buttons.append(created_button)


	print lineNum(), "defineButtons() - completed"




# # #########################################################################################
# # This figures out which button was clicked
def findButton(buttons, x, y):
	for b in buttons:
		if x <= b.x + b.x_width:
			if x >= b.x:
				if y >= b.y:
					if y <= b.y + b.y_height:
						print lineNum(), "selected button label_txt = ", b.button_name
						return b
	return None




# # #########################################################################################
# # this updates pushy buttons
def updatePushyButtons(selected_button):
	print lineNum(), "updating pushy buttons"

"""
	MOVE PUSHY BUTTON PROCESSING HERE
"""



############################################################################################
# # UPDATE STICKY BUTTONS
# # this updates sticky buttons  based on actions taken
############################################################################################
buttonToCheck = {}
def updateStickyButtons(selected_button):
	print lineNum(), "updateStickyButtons() - started"
	print lineNum(), "selected_button = ", selected_button

	"""
	# for sticky buttons, iterate through nested allButtons dictionary and flip buttonEnabled
	for allButtonsID, allButtonsValue in allButtons.items():
		for key in allButtonsValue:
			#print lineNum(), "key", key
			#buttonToCheck[key] = allButtonsValue[key]
			#print lineNum(), "buttonToCheck", key, allButtonsValue[key]
			if allButtonsValue[key] == "sticky":
				print lineNum(), "found a sticky button"
				print lineNum(), "key, ", key, "value", allButtonsValue[key]
				#print lineNum(), "buttonToCheck", key, allButtonsValue[key]
	"""
	
	if selected_button == "sticky01":
		if button04[7] == False:
			print lineNum(), "sticky01 button found"
			button04[7] = True
			button04[8] = UI_button_selected_color
			print lineNum(), "flipped sticky01 from false to true"
			defineButtons()	
			
		elif button04[7] == True:
			print lineNum(), "sticky01 button found"
			button04[7] = False
			button04[8] = UI_button_color
			print lineNum(), "flipped stick01 from true to false"
			defineButtons()

	if selected_button == "sticky02":
		if button05[7] == False:
			print lineNum(), "sticky02 button found"
			button05[7] = True
			button05[8] = UI_button_selected_color
			print lineNum(), "flipped sticky02 from false to true"
			defineButtons()	
			
		elif button05[7] == True:
			print lineNum(), "sticky02 button found"
			button05[7] = False
			button05[8] = UI_button_color
			print lineNum(), "flipped sticky02 from true to false"
			defineButtons()


	if selected_button == "sticky03":
		if button06[7] == False:
			print lineNum(), "sticky03 button found"
			button06[7] = True
			button06[8] = UI_button_selected_color
			print lineNum(), "flipped sticky03 from false to true"
			defineButtons()	
			
		elif button06[7] == True:
			print lineNum(), "sticky03 button found"
			button06[7] = False
			button06[8] = UI_button_color
			print lineNum(), "flipped sticky03 from true to false"
			defineButtons()			


	# # # FPS BUTTON
	if selected_button == "fps":
		if button19[7] == False:
			button19[7] = True
			button19[8] = UI_button_selected_color
			defineButtons()	
			
		elif button19[7] == True:
			button19[7] = False
			button19[8] = UI_button_color
			redrawEverything()

	# # # ORIGIN BUTTON
	if selected_button == "origin":
		if button22[7] == False:
			button22[7] = True
			button22[8] = UI_button_selected_color
			defineButtons()	
			redrawEverything()
			
		elif button22[7] == True:
			button22[7] = False
			button22[8] = UI_button_color
			defineButtons()
			redrawEverything()


	# # # GRID BUTTON
	if selected_button == "grid":
		if button21[7] == False:
			button21[7] = True
			button21[8] = UI_button_selected_color
			defineButtons()	
			redrawEverything()
			
		elif button21[7] == True:
			button21[7] = False
			button21[8] = UI_button_color
			defineButtons()
			redrawEverything()


	print lineNum(), "updateStickyButtons() - completed"
	return
	



## ############################################################################################
## UPDATE GROUP BUTTONS
## ############################################################################################

def updateGroupButtons(selected_button):
	print lineNum(), "running update group buttons"

	# # Group 01 processing
	if selected_button == "Group01Button01":
		
		if button10[7] == True:
			button10[7] = False
			button10[8] = UI_button_color
			button11[7] = True
			button11[8] = UI_button_selected_color
			defineButtons()	
		
		elif button10[7] == False:
			button10[7] = True
			button10[8] = UI_button_selected_color
			button11[7] = False
			button11[8] = UI_button_color
			defineButtons()	

	if selected_button == "Group01Button02":
		
		if button11[7] == True:
			button11[7] = False
			button11[8] = UI_button_color
			button10[7] = True
			button10[8] = UI_button_selected_color
			defineButtons()	
		
		elif button11[7] == False:
			button11[7] = True
			button11[8] = UI_button_selected_color
			button10[7] = False
			button10[8] = UI_button_color
			defineButtons()


	# # Group 02 processing
	if selected_button == "Group02Button01":
		
		if button13[7] == True:
			button13[7] = False
			button13[8] = UI_button_color
			button14[7] = True
			button14[8] = UI_button_selected_color
			defineButtons()	
		
		elif button13[7] == False:
			button13[7] = True
			button13[8] = UI_button_selected_color
			button14[7] = False
			button14[8] = UI_button_color
			defineButtons()	

	if selected_button == "Group02Button02":
		
		if button14[7] == True:
			button14[7] = False
			button14[8] = UI_button_color
			button13[7] = True
			button13[8] = UI_button_selected_color
			defineButtons()	
		
		elif button14[7] == False:
			button14[7] = True
			button14[8] = UI_button_selected_color
			button13[7] = False
			button13[8] = UI_button_color
			defineButtons()


	# # Group 03 processing
	if selected_button == "Group03Button01":
		
		if button16[7] == False:
			button16[7] = True
			button16[8] = UI_button_selected_color
			
			button17[7] = False
			button17[8] = UI_button_color
			
			button18[7] = False
			button18[8] = UI_button_color

			defineButtons()	

	if selected_button == "Group03Button02":
		
		if button17[7] == False:
			button17[7] = True
			button17[8] = UI_button_selected_color
			
			button16[7] = False
			button16[8] = UI_button_color
			
			button18[7] = False
			button18[8] = UI_button_color

			defineButtons()	

	if selected_button == "Group03Button03":
		
		if button18[7] == False:
			button18[7] = True
			button18[8] = UI_button_selected_color
			
			button16[7] = False
			button16[8] = UI_button_color
			
			button17[7] = False
			button17[8] = UI_button_color

			defineButtons()	


## ############################################################################################
## UPDATE DROPDOWN BUTTONS
## ############################################################################################

def updateDropdownButtons(selected_button):
	print lineNum(), "running update Dropdown buttons"

	if selected_button == "dropdown01opener":
		if button26[7] == False:
			print lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			# update this button
			button26[7] = True
			button26[8] = UI_button_selected_color
			button26[5] = "<<"

			# update associated buttons
			button27[10] = True	
			button28[10] = True
			button29[10] = True

			defineButtons()	

			print lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			print lineNum(), button26[0], "enabled:", button26[7], "visible:", button26[10]
			
		elif button26[7] == True:
			print " --------------------------------------- "
			print lineNum(), "STARTED dropdown true to false "
			print " --------------------------------------- "

			# udapte this button
			print lineNum(), button26[0], "enabled was: ", button26[7]
			button26[7] = False
			button26[8] = UI_button_color
			button26[5] = ">>"
			print lineNum(), button26[0], "enabled:", button26[7], "visible:", button26[10]

			# update associated buttons
			button27[10] = False
			button28[10] = False
			button29[10] = False
			print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]

			screen.fill(background_color)
			defineButtons()
			redrawEverything()

			print lineNum(), button26[0], "enabled:", button26[7], "visible:", button26[10]
			print " --------------------------------------- "
			print lineNum(), "FINISHED dropdown true to false "
			print " --------------------------------------- "
			print type(button27[10])



# # FPS related Functions
def show_fps():
	fps_overlay = fps_font.render("FPS:"+str(FPS), True, UI_button_txt_color)
	screen.blit(fps_overlay, (pygame_window_width - 100,pygame_window_height - 30))

def count_fps():
	global cSec, cFrame, FPS, deltatime
	if cSec == time.strftime("%S"):
		cFrame += 1
	else:
		FPS = cFrame
		cFrame = 0
		cSec = time.strftime("%S")

# # Redraw the backgroundm, buttons, screen, etc. 
def redrawEverything():
	print lineNum(), "redrawEverything() - started"
	
	print lineNum(), "drawing background"
	screen.fill(background_color)

	# check if draw grids is enabled, and draw if so
	if button21[7] == True:
		drawGrid()

	# check if draw origin is enabled, and draw if so. 
	if button22[7] == True:
		drawOrigin()

	print lineNum(), "drawing borders and frames"
	pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
	pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))

	print lineNum(), "redifining buttons and redrawing"
	defineButtons()
	for i, button in enumerate(my_buttons):
		button.display()

	print lineNum(), "redrawEverything() - completed"

# # Draw origin lines
def drawOrigin():
	pygame.draw.lines(screen, red, False, [((pygame_window_width / 2),0),((pygame_window_width / 2 ),pygame_window_height)],2)
	pygame.draw.lines(screen, red, False, [(0,(pygame_window_height / 2)),(pygame_window_width, (pygame_window_height / 2))],2)


# # Draw grid lines
def drawGrid():
	# # Draw grid
	grid_width = pygame_window_width / 10
	grid_height = pygame_window_height / 10

	pygame.draw.lines(screen, yellow, False, [((pygame_window_width / 2),0),((pygame_window_width / 2 ),pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width,0),(grid_width,pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width * 2,0),(grid_width * 2,pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width * 3,0),(grid_width * 3,pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width * 4,0),(grid_width * 4,pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width * 6,0),(grid_width * 6,pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width * 7,0),(grid_width * 7,pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width * 8,0),(grid_width * 8,pygame_window_height)],1)
	pygame.draw.lines(screen, yellow, False, [(grid_width * 9,0),(grid_width * 9,pygame_window_height)],1)

	pygame.draw.lines(screen, yellow, False, [(0,(pygame_window_height / 2)),(pygame_window_width, (pygame_window_height / 2))],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height), (pygame_window_height,grid_height)],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height * 2), (pygame_window_height,grid_height * 2)],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height * 3), (pygame_window_height,grid_height * 3)],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height * 4), (pygame_window_height,grid_height * 4)],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height * 6), (pygame_window_height,grid_height * 6)],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height * 7), (pygame_window_height,grid_height * 7)],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height * 8), (pygame_window_height,grid_height * 8)],1)
	pygame.draw.lines(screen, yellow, False, [(0,grid_height * 9), (pygame_window_height,grid_height * 9)],1)	








# ************************************************************************************************************************
# ************************************************************************************************************************
# 	Classes                    #
# ************************************************************************************************************************
# ************************************************************************************************************************




class Button:
	def __init__ (self, (x,y), button_name, x_width, y_height, button_label_txt, buttonType, buttonEnabled, buttonColor, buttonVisible):
		self.button_name = button_name
		self.x = x
		self.x_width = x_width
		self.y = y
		self.y_height = y_height
		self.color = buttonColor
		self.thickness = 0
		self.button_label_txt = button_label_txt
		self.colorBorder = UI_button_border_color
		self.buttonType = buttonType  
		self.buttonEnabled = buttonEnabled
		self.buttonVisible = buttonVisible

	# # displays buttons
	def display(self):

		# render "pushy" type buttons
		if self.buttonType == "pushy":
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "sticky" type buttons
		elif self.buttonType == "sticky":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "label" type buttons
		elif self.buttonType == "label":
			self.color = UI_label_color																	# since self.color = buttonColor by default, this overwrites that for labels
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "group" type buttons
		elif self.buttonType == "group":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# checking when this flips back to true
		#print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]

		# render "dropdown" type buttons
		if self.buttonType == "dropdown":	
			
			# next three are added because for some reason buttonVisible flips from false to true during iteration through class. 
			# figure the cause our later, for now it works. 
			if self.button_name == "dropdown01option01":
				self.buttonVisible = button27[10]
			if self.button_name == "dropdown01option02":
				self.buttonVisible = button28[10]
			if self.button_name == "dropdown01option03":
				self.buttonVisible = button29[10]
			
			#print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]
			#print lineNum(), self.button_name, "buttonVisible?:", self.buttonVisible
			#raw_input("Press Enter to continue...")
			print "self.buttonVisible type = ", type(self.buttonVisible)
			if self.buttonVisible == True:
				#print lineNum(), "rendering dropdown type buttons, button: ", self.button_name, "buttonVisible?:", self.buttonVisible
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)						# set label
				screen.blit(label, (self.x + 5, self.y))														# draw label

			#elif self.buttonVisible == False:
			#	print lineNum(), self.button_name, "visible is: ", self.buttonVisible
				#print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]


# ************************************************************************************************************************
# ************************************************************************************************************************
# 	MAIN code	#
# ************************************************************************************************************************
# ************************************************************************************************************************

####### INITIALIZE DISPLAY ##########
## If this is in the main loop, FPS goes way down, only refresh what's needed ##

# # Pygame display
print lineNum(), "starting MAIN code"

print lineNum(), "- initializing pygame display"
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption('My Program Name')

# # #  draw background
print lineNum(), "- drawing background"
screen.fill(background_color)

# # draw borders & frames for interface
print lineNum(), "- drawing borders and frames"
pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))

# # draw buttons!
print lineNum(), "- drawing buttons"
defineButtons()
for i, button in enumerate(my_buttons):
	button.display()

print lineNum(), "initializing display completed"


########## EVENT MONITORING / UPDATE DISPLAY ########### 

running = True

while running:

	if button19[7] == True:
		pygame.draw.rect(screen, blue, (pygame_window_width - 100, pygame_window_height - 30, 80, 20))   
		count_fps()
		show_fps()



	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False
		
		

		if event.type == pygame.MOUSEBUTTONDOWN:					#mousebuttondown only runs once, things run outside if this if loop
			(mouseX, mouseY) = pygame.mouse.get_pos()				# will run continually while button is held down
			print lineNum(), "mouseX = ", mouseX, "mouseY = ", mouseY			# this if.even MOUSEBUTTONDOWN **MUST** be under the for event in pygame.event.get() to run only once
			selected_button = findButton(my_buttons, mouseX, mouseY)
			print lineNum(), "selected button = ", selected_button

			if selected_button != None:

				if selected_button.button_label_txt == "EXIT":
					print lineNum(), "you pressed exit"
					running = False

				if selected_button.buttonType == "pushy":
					print lineNum(), "running MOUSEBUTTONDOWN pushy event"
					print lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = UI_button_click_color
					print lineNum(), "selected_button.color now : ", selected_button.color			
					selected_button.buttonEnabled = True
					print lineNum(), "clicked button is a pushy temporary button"
					

					if selected_button.button_name == "command01":
						print lineNum(), "you clicked command01"
						button01[7] = True
						button01[8] = UI_button_click_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print lineNum(), "running code for Command01"
						# command01 function call goes here:


					if selected_button.button_name == "command02":
						print lineNum(), "you clicked command02"
						button02[7] = True
						button02[8] = UI_button_click_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print lineNum(), "running code for Command02"
						#command02 function call goes here:


					if selected_button.button_name == "command03":
						print lineNum(), "you clicked command03"
						button03[7] = True
						button03[8] = UI_button_click_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print lineNum(), "running code for Command03"
						#command03 function call goes here:		

				if selected_button.buttonType == "sticky":
					print lineNum(), "running sticky event"
					updateStickyButtons(selected_button.button_name)

				if selected_button.buttonType == "group":
					print lineNum(), "running group type button event"
					updateGroupButtons(selected_button.button_name)

				if selected_button.buttonType == "dropdown":
					print lineNum(), "running dropdown button event"
					updateDropdownButtons(selected_button.button_name)
				

		if event.type == pygame.MOUSEBUTTONUP:

			if selected_button != None:
				
				if selected_button.buttonType == "pushy":
					print lineNum(), "running MOUSEBUTTONUP pushy event"
					print lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = UI_button_color 			#reverts button back to normal color after letting go of mouse
					print lineNum(), "selected_button.color now : ", selected_button.color	
			
					if selected_button.button_name == "command01":
						print lineNum(), "you clicked command01"
						button01[7] = False
						button01[8] = UI_button_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event command01"
						for i, button in enumerate(my_buttons):
							button.display()



					if selected_button.button_name == "command02":
						print lineNum(), "you clicked command02"
						button02[7] = False
						button02[8] = UI_button_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event command02"
						for i, button in enumerate(my_buttons):
							button.display()



					if selected_button.button_name == "command03":
						print lineNum(), "you clicked command03"
						button03[7] = False
						button03[8] = UI_button_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event command03"
						for i, button in enumerate(my_buttons):
							button.display()

			

			selected_button = None
			print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]
			print lineNum(), "selected_button = ", selected_button
			print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]
			
			# # re draw buttons!
			# # without this here, pushy buttons don't return to normal on mouseup
			print lineNum(), "____drawing buttons in MOUSEBUTTONUP call"
			print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]
			for i, button in enumerate(my_buttons):
				button.display()		
			print lineNum(), "buttons27,28,29 visible:", button27[10], button28[10], button29[10]
			

	# always do this last
	pygame.display.flip()