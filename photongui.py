#************************************************************************************
#  	dev notes
#	09-27-2019 - currently incorporating menu_physics_garage_005b.py - DONE
#	10-19-2019 - currently integrating menu_physics_garage_006.py
#	10-21-2019 - working on getting it to not close when you click somewhere else. it's trying to find the button type attrib for no button
# 	10-22-2019 - sticky buttons working
#	10-22-2019 - get command button to do something - add FPS display (menu_physics_garage_007.py)



#************************************************************************************
#	MODIFYING YOUR UI
#	- ADD A BUTTON - PUSHY 
#		1) pushy is a temporary button active only while it is being clicked on, typically to invoke a command
#		2) under "# 	define buttons" copy and paste another button, modifying values accordingly
#	- ADD A BUTTON - STICKY
#		1) under "# 	define buttons" copy and paste another button, modifying values accordingly
#		2a) if a button is sticky, the 'matchButton' funtion is run to check if the button is enabled and toggle it's state
#		2b) copy and paste in a sticky button section, update values:
#		2c) be sure to update the button_origin_y and width value to match your new button in both the if enabled=true and enabled=false sections
#		3) add function for the buttons utility
#		4) add link to function somewhere in the main program loop
#	- ADD A LABEL
#		1) under "# 	define buttons" copy and paste another button, modifying values accordingly, buttonType = label
#	- ADD A NEW BUTTON TYPE
#		1) under 	button class ## displays buttons def display(self): copy and paste button type into new section, update values
#		2) under main program loop \  if selected_button != None: add a new group for that button type
#	- ADD A GROUP AND GROUP BUTTONS
#		group buttons are part of an option group, when one is selected, the others are disabled
#		0) if not done allready and necessary, create a label for the button group
#		1a) under "# 	define buttons" copy and paste the additional buttons, modifying values accordingly
#		1b) you till need to change the button name, location, variable names, etc
#		2) create a new entry under  'def matchButton(selected_button):' for the new button group
#		2b) each condition (enabled / disabled) needs to be setup for each button, e.g. if button 1 is enabled and clicked on, button 2 is turned to false (or all other buttons in group)
#		2c) each button that is updated will need to have it's  "my_buttons.append(created_button)" updated as well
#		2d) be sure to update the position, size of each button if / when applicable (origin x & y, width and height)
#		3) if the group has more than 2 buttons, and only one should be selected, you don't need the if true then false and turn the others true section, since that would enable 2/3
#		3b) see button group 04 as an example in the def matchButton section	
#	- MOVE A BUTTON
#	- 

# ************************************************************************************
# 	import modules	#

import pygame
import random
import math
import sys
import time 			# for FPS functions
# ************************************************************************************


# ************************************************************************************
#	initial variables	#

#py game font
pygame.font.init()							# needs to be called at the start of the program
myfont = pygame.font.SysFont('Arial',15)		# GUI font type and size


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
fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 15)

# global button_clicked
# button_clicked = False

# ************************************************************************************



# ************************************************************************************
#	initial lists	#

my_uiObjects = []							# this list will hold all the UI elements
# ************************************************************************************



# ************************************************************************************
# 	initial dictionaries 		#
selectedButton = {}



# ************************************************************************************
#	functions	#

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





# # Button Related Functions

# # # this finds what button you clicked on
def findButton(buttons, x, y):
	for b in buttons:
		print "x = ", x, "y = ", y
		print "b.x = ", b.x, "b.x width = ", b.x + b.x_width
		print "b.y = ", b.y, "b.y height = ", b.y + b.y_height
		if x <= b.x + b.x_width:
			if x >= b.x:
				print "x ok"
				if y >= b.y:
					if y <= b.y + b.y_height:
						print "Y ok, button found"
						print "selected button label_txt = ", b.button_name
						print "this is return b", b 
						return b
	return None








# for sticky and group buttons to find and update buttonEnabled = then redraw buttons
def matchButton(selected_button):					


	# # # Check Dropdown01Display  button
	if selected_button == Dropdown01Display[0]:
		print "clicked button is", Dropdown01Display[0]
		if Dropdown01Display[7] == False:
			Dropdown01Display[7] = True
			Dropdown01Display[8] = UI_button_selected_color
			
			### -------------------------- ###
			# UPDATE Dropdown01Display button
			
			button_name =  Dropdown01Display[0]							# button variables updated to prepare for updating display
			button_origin_x = Dropdown01Display[1]									
			button_origin_y = Dropdown01Display[2]
			button_width = Dropdown01Display[3]
			button_height = Dropdown01Display[4]
			button_label_txt = Dropdown01Display[5]
			buttonType = Dropdown01Display[6]
			buttonEnabled = Dropdown01Display[7]
			buttonColor = Dropdown01Display[8]
			buttonVisible = Dropdown01Display[10]

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		
		if Dropdown01Display[7] == True:
			Dropdown01Display[7] = False
			Dropdown01Display[8] = UI_button_color

			### -------------------------- ###
			# UPDATE Dropdown01Display button
			
			button_name =  Dropdown01Display[0]							# button variables updated to prepare for updating display
			button_origin_x = Dropdown01Display[1]									
			button_origin_y = Dropdown01Display[2]
			button_width = Dropdown01Display[3]
			button_height = Dropdown01Display[4]
			button_label_txt = Dropdown01Display[5]
			buttonType = Dropdown01Display[6]
			buttonEnabled = Dropdown01Display[7]
			buttonColor = Dropdown01Display[8]
			buttonVisible = Dropdown01Display[10]

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
			
			return




	# updates the displayed text of dropdown01display when an option is selected
	if selected_button == Dropdown01option03[0]:							# if the selected button is Dropdown01option03
		if Dropdown01opener[7] == True:									# AND Dropdown01opener is enabled and displayed
			Dropdown01Display[5] = Dropdown01option03[5]					# the label text for Dropdown01Display is updated with the label text of option01

			button_name =  Dropdown01Display[0]							# button variables updated to prepare for updating display
			button_origin_x = Dropdown01Display[1]									
			button_origin_y = Dropdown01Display[2]
			button_width = Dropdown01Display[3]
			button_height = Dropdown01Display[4]
			button_label_txt = Dropdown01Display[5]
			buttonType = Dropdown01Display[6]
			buttonEnabled = Dropdown01Display[7]
			buttonColor = Dropdown01Display[8]
			buttonVisible = Dropdown01Display[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			for i, button in enumerate(my_buttons):
				button.display()
						
			return


	# updates the displayed text of dropdown01display when an option is selected
	if selected_button == Dropdown01option02[0]:							# if the selected button is Dropdown01option02
		if Dropdown01opener[7] == True:									# AND Dropdown01opener is enabled and displayed
			Dropdown01Display[5] = Dropdown01option02[5]					# the label text for Dropdown01Display is updated with the label text of option01

			button_name =  Dropdown01Display[0]							# button variables updated to prepare for updating display
			button_origin_x = Dropdown01Display[1]									
			button_origin_y = Dropdown01Display[2]
			button_width = Dropdown01Display[3]
			button_height = Dropdown01Display[4]
			button_label_txt = Dropdown01Display[5]
			buttonType = Dropdown01Display[6]
			buttonEnabled = Dropdown01Display[7]
			buttonColor = Dropdown01Display[8]
			buttonVisible = Dropdown01Display[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			for i, button in enumerate(my_buttons):
				button.display()
						
			return

	# updates the displayed text of dropdown01display when an option is selected
	print "selected_button = ", selected_button
	print "Dropdown01option01[0] = ", Dropdown01option01[0]

	if selected_button == Dropdown01option01[0]:							# if the selected button is Dropdown01option01
		print "dropdown 01 option 01 selected, running..."
		if Dropdown01opener[7] == True:									# AND Dropdown01opener is enabled and displayed
			print "Dropdown01Display[5] was:", Dropdown01Display[5]
			Dropdown01Display[5] = Dropdown01option01[5]					# the label text for Dropdown01Display is updated with the label text of option01
			print "Dropdown01Display[5] is:", Dropdown01Display[5]

			button_name =  Dropdown01Display[0]							# button variables updated to prepare for updating display
			button_origin_x = Dropdown01Display[1]									
			button_origin_y = Dropdown01Display[2]
			button_width = Dropdown01Display[3]
			button_height = Dropdown01Display[4]
			button_label_txt = Dropdown01Display[5]
			buttonType = Dropdown01Display[6]
			buttonEnabled = Dropdown01Display[7]
			buttonColor = Dropdown01Display[8]
			buttonVisible = Dropdown01Display[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			for i, button in enumerate(my_buttons):
				button.display()
						
			return




	# # # Check Dropdown 01  button
	if selected_button == Dropdown01opener[0]:
		if Dropdown01opener[7] == False:
			Dropdown01opener[7] = True
			Dropdown01opener[8] = UI_button_selected_color

			# Update the other buttons in the group			
			Dropdown01option01[10] = True
			Dropdown01option02[10] = True
			Dropdown01option03[10] = True

			### -------------------------- ###
			# UPDATE Dropdown01opener button
			
			button_name =  "Dropdown01opener"
			button_origin_x = UI_sideBar_width - 20									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 480
			button_width = 20
			button_height = 20
			button_label_txt = "<<"
			buttonType = "sticky"
			buttonEnabled = Dropdown01opener[7]
			buttonColor = Dropdown01opener[8]
			buttonVisible = True

			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			# UPDATE related option buttons to visible
			### ### ------------------- ### ###
			button_name =  Dropdown01option01[0]
			button_origin_x = Dropdown01option01[1]									#x0, y0 is upper left corner
			button_origin_y = Dropdown01option01[2]
			button_width = Dropdown01option01[3]
			button_height = Dropdown01option01[4]
			button_label_txt = Dropdown01option01[5]
			buttonType = Dropdown01option01[6]
			buttonEnabled = Dropdown01option01[7]
			buttonColor = Dropdown01option01[8]
			buttonVisible = Dropdown01option01[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			button_name =  Dropdown01option02[0]
			button_origin_x = Dropdown01option02[1]									#x0, y0 is upper left corner
			button_origin_y = Dropdown01option02[2]
			button_width = Dropdown01option02[3]
			button_height = Dropdown01option02[4]
			button_label_txt = Dropdown01option02[5]
			buttonType = Dropdown01option02[6]
			buttonEnabled = Dropdown01option02[7]
			buttonColor = Dropdown01option02[8]
			buttonVisible = Dropdown01option02[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)


			button_name =  Dropdown01option03[0]
			button_origin_x = Dropdown01option03[1]									#x0, y0 is upper left corner
			button_origin_y = Dropdown01option03[2]
			button_width = Dropdown01option03[3]
			button_height = Dropdown01option03[4]
			button_label_txt = Dropdown01option03[5]
			buttonType = Dropdown01option03[6]
			buttonEnabled = Dropdown01option03[7]
			buttonColor = Dropdown01option03[8]
			buttonVisible = Dropdown01option03[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### ### ------------------- ### ###
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		


		if Dropdown01opener[7] == True:
			Dropdown01opener[7] = False
			Dropdown01opener[8] = UI_button_color

			# Update the other buttons in the group			
			print "Dropdown01option01[10] before", Dropdown01option01[10]
			Dropdown01option01[10] = False
			Dropdown01option02[10] = False
			Dropdown01option03[10] = False
			print "Dropdown01option01[10] after", Dropdown01option01[10]

			### -------------------------- ###
			# UPDATE Dropdown01opener button
			
			button_name =  "Dropdown01opener"
			button_origin_x = UI_sideBar_width - 20									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 480
			button_width = 20
			button_height = 20
			button_label_txt = ">>"
			buttonType = "sticky"
			buttonEnabled = Dropdown01opener[7]
			buttonColor = Dropdown01opener[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
	
			### -------------------------- ###	

			button_name =  Dropdown01option01[0]
			button_origin_x = Dropdown01option01[1]									#x0, y0 is upper left corner
			button_origin_y = Dropdown01option01[2]
			button_width = Dropdown01option01[3]
			button_height = Dropdown01option01[4]
			button_label_txt = Dropdown01option01[5]
			buttonType = Dropdown01option01[6]
			buttonEnabled = Dropdown01option01[7]
			buttonColor = Dropdown01option01[8]
			buttonVisible = Dropdown01option01[10]
			print "Dropdown01option01[10] 305", Dropdown01option01[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			button_name =  Dropdown01option02[0]
			button_origin_x = Dropdown01option02[1]									#x0, y0 is upper left corner
			button_origin_y = Dropdown01option02[2]
			button_width = Dropdown01option02[3]
			button_height = Dropdown01option02[4]
			button_label_txt = Dropdown01option02[5]
			buttonType = Dropdown01option02[6]
			buttonEnabled = Dropdown01option02[7]
			buttonColor = Dropdown01option02[8]
			buttonVisible = Dropdown01option02[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)


			button_name =  Dropdown01option03[0]
			button_origin_x = Dropdown01option03[1]									#x0, y0 is upper left corner
			button_origin_y = Dropdown01option03[2]
			button_width = Dropdown01option03[3]
			button_height = Dropdown01option03[4]
			button_label_txt = Dropdown01option03[5]
			buttonType = Dropdown01option03[6]
			buttonEnabled = Dropdown01option03[7]
			buttonColor = Dropdown01option03[8]
			buttonVisible = Dropdown01option03[10]
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)


			for i, button in enumerate(my_buttons):
				button.display()
			
			return


	#####################################################################
	# # # ------------------------- START BUTTON GROUP04 ------------------ # # # 
	#####################################################################		


	# # # for group buttons, be sure to update the other button in the button group before updating the display (see next "NOTE HERE")
	if selected_button == Group04Button01[0]:
		if Group04Button01[7] == False:						# condition for this section to run, this processes only when the button WAS FALSE and was clicked

			# confirming conditions
			print "WAS:"
			print "Group04Button01[7] = ", Group04Button01[7]
			print "Group04Button02[7] = ", Group04Button02[7]
			print "Group04Button03[7] = ", Group04Button03[7]	

			
			# update dictionary for  this button
			Group04Button01[7] = True							# it's been clicked, it was false, this flips it to True
			Group04Button01[8] = UI_button_selected_color		# it's been clicked, it was false, this changes the color to clicked color
			
			# update dictionary for other buttons in group
			Group04Button02[7] = False 						# flips the corresponding button(s) in the group
			Group04Button03[7] = False

			# confirming conditions
			print "IS NOW:"
			print "Group04Button01[7] = ", Group04Button01[7]
			print "Group04Button02[7] = ", Group04Button02[7]
			print "Group04Button03[7] = ", Group04Button03[7]			
			
			### -------------------------- ###
			
			# UPDATE Group04Button01 button
			# restarting variables to use in .append below
			
			button_name =  "Group04Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "   A   "
			buttonType = "group"
			buttonEnabled = Group04Button01[7]
			buttonColor = Group04Button01[8]
			buttonVisible = True

			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			# NOTE HERE:
			# this next part updates the OTHER button, both this section adn the define button then add button to display lit are necessary. 
			# updates the OTHER button in the group			
			button_name =  "Group04Button02"
			button_origin_x = UI_sideBar_width / 3								#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "   B   "
			buttonType = "group"
			buttonEnabled = Group04Button02[7]
			buttonColor = Group04Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			
			button_name =  "Group04Button03"
			button_origin_x = (UI_sideBar_width / 3) + (UI_sideBar_width / 3)		#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "   C   "
			buttonType = "group"
			buttonEnabled = Group04Button03[7]
			buttonColor = Group04Button03[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			### -------------------------- ###	


			for i, button in enumerate(my_buttons):
				button.display()
						
			return





			##############################################


	if selected_button == Group04Button02[0]:
		if Group04Button02[7] == False:

			# confirming conditions
			print "WAS:"
			print "Group04Button01[7] = ", Group04Button01[7]
			print "Group04Button02[7] = ", Group04Button02[7]
			print "Group04Button03[7] = ", Group04Button03[7]	

			Group04Button02[7] = True
			Group04Button02[8] = UI_button_selected_color
			
			# flip the other buttons
			Group04Button01[7] = False
			Group04Button03[7] = False

			# confirming conditions
			print "IN NOW:"
			print "Group04Button01[7] = ", Group04Button01[7]
			print "Group04Button02[7] = ", Group04Button02[7]
			print "Group04Button03[7] = ", Group04Button03[7]
			
			### -------------------------- ###
			# UPDATE Group04Button02 button
			
			button_name =  "Group04Button02"
			button_origin_x = UI_sideBar_width / 3									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3 
			button_height = 20
			button_label_txt = "   B   "
			buttonType = "group"
			buttonEnabled = Group04Button02[7]
			buttonColor = Group04Button02[8]
			buttonVisible = True
					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group04Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "   A   "
			buttonType = "group"
			buttonEnabled = Group04Button01[7]
			buttonColor = Group04Button01[8]
			buttonVisible = True

			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			button_name =  "Group04Button03"
			button_origin_x = (UI_sideBar_width /3) * 2									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "   C   "
			buttonType = "group"
			buttonEnabled = Group04Button01[7]
			buttonColor = Group04Button01[8]
			buttonVisible = True

			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			### -------------------------- ###


			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		



	############################################################

	if selected_button == Group04Button03[0]:
		if Group04Button03[7] == False:

			# confirming conditions
			print "WAS:"
			print "Group04Button01[7] = ", Group04Button01[7]
			print "Group04Button02[7] = ", Group04Button02[7]
			print "Group04Button03[7] = ", Group04Button03[7]	

			Group04Button03[7] = True
			Group04Button03[8] = UI_button_selected_color
			
			# flip the other buttons
			Group04Button01[7] = False
			Group04Button02[7] = False

			# confirming conditions
			print "IS NOW:"
			print "Group04Button01[7] = ", Group04Button01[7]
			print "Group04Button02[7] = ", Group04Button02[7]
			print "Group04Button03[7] = ", Group04Button03[7]

			### -------------------------- ###
			# UPDATE Group04Button02 button
			
			button_name =  "Group04Button03"
			button_origin_x = (UI_sideBar_width / 3) * 2									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3 
			button_height = 20
			button_label_txt = "   C   "
			buttonType = "group"
			buttonEnabled = Group04Button03[7]
			buttonColor = Group04Button03[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group04Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "   A   "
			buttonType = "group"
			buttonEnabled = Group04Button01[7]
			buttonColor = Group04Button01[8]
			buttonVisible = True

			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			button_name =  "Group04Button02"
			button_origin_x = UI_sideBar_width /3									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 420
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "   B   "
			buttonType = "group"
			buttonEnabled = Group04Button01[7]
			buttonColor = Group04Button01[8]
			buttonVisible = True

			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			### -------------------------- ###


			for i, button in enumerate(my_buttons):
				button.display()
						
			return
	


	#####################################################################
	# # # ------------------------- END BUTTON GROUP04 ------------------ # # # 
	#####################################################################










	#####################################################################
	# # # ------------------------- START BUTTON GROUP03 ------------------ # # # 
	#####################################################################		


	# # # for group buttons, be sure to update the other button in the button group before updating the display (see next "NOTE HERE")
	if selected_button == Group03Button01[0]:
		print "clicked button is", Group03Button01[0]
		if Group03Button01[7] == False:
			
			print "Group03Button01 enabled was ", Group03Button01[7]
			Group03Button01[7] = True
			print "Group03Button01 enabled now ", Group03Button01[7]
			
			# turns off the corresponding button in the group
			print "Group03Button02enabled was ", Group03Button02[7]
			Group03Button02[7] = False
			print "Group03Button02enabled now ", Group03Button02[7]


			print "old color", Group03Button01[8]
			Group03Button01[8] = UI_button_selected_color
			print "new color", Group03Button01[8]
			
			### -------------------------- ###
			# UPDATE Group03Button01 button
			
			button_name =  "Group03Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group03Button01[7]
			buttonColor = Group03Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			# NOTE HERE:
			# this next part updates the OTHER button, both this section adn the define button then add button to display lit are necessary. 
			# updates the OTHER button in the group			
			button_name =  "Group03Button02"
			button_origin_x = UI_sideBar_width / 2								#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group03Button02[7]
			buttonColor = Group03Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	


			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		
		if Group03Button01[7] == True:
			print "Group03Button01 enabled was ", Group03Button01[7]
			Group03Button01[7] = False
			Group03Button02[7] = True
			print "Group03Button01 enabled now", Group03Button01[7]
			print "old color", Group03Button01[8]
			Group03Button01[8] = UI_button_color
			print "new color", Group03Button01[8]

			### -------------------------- ###
			# UPDATE Group03Button01 button
			
			button_name =  "Group03Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group03Button01[7]
			buttonColor = Group03Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group03Button02"
			button_origin_x = UI_sideBar_width / 2									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group03Button02[7]
			buttonColor = Group03Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
			
			return

	if selected_button == Group03Button02[0]:
		print "clicked button is", Group03Button02[0]
		if Group03Button02[7] == False:
			print "Group03Button02 enabled was ", Group03Button02[7]
			Group03Button02[7] = True
			Group03Button01[7] = False
			print "Group03Button02 enabled now ", Group03Button02[7]
			print "old color", Group03Button02[8]
			Group03Button02[8] = UI_button_selected_color
			print "new color", Group03Button02[8]
			
			### -------------------------- ###
			# UPDATE Group03Button02 button
			
			button_name =  "Group03Button02"
			button_origin_x = UI_sideBar_width / 2									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2 
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group03Button02[7]
			buttonColor = Group03Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group03Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group03Button01[7]
			buttonColor = Group03Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###


			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		
		if Group03Button02[7] == True:
			print "Group03Button02 enabled was ", Group03Button02[7]
			Group03Button02[7] = False
			Group03Button01[7] = True
			print "Group03Button02 enabled now", Group03Button02[7]
			print "old color", Group03Button02[8]
			Group03Button02[8] = UI_button_color
			print "new color", Group03Button02[8]

			### -------------------------- ###
			# UPDATE Group03Button02 button
			
			button_name =  "Group03Button02"
			button_origin_x = UI_sideBar_width / 2									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group03Button02[7]
			buttonColor = Group03Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group03Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 360
			button_width = UI_sideBar_width / 2
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group03Button01[7]
			buttonColor = Group03Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###

			for i, button in enumerate(my_buttons):
				button.display()
			
			return

	#####################################################################
	# # # ------------------------- END BUTTON GROUP03 ------------------ # # # 
	#####################################################################


	#####################################################################
	# # # ------------------------- START BUTTON GROUP02 ------------------ # # # 
	#####################################################################		


	# # # for group buttons, be sure to update the other button in the button group before updating the display (see next "NOTE HERE")
	if selected_button == Group02Button01[0]:
		print "clicked button is", Group02Button01[0]
		if Group02Button01[7] == False:
			
			print "Group02Button01 enabled was ", Group02Button01[7]
			Group02Button01[7] = True
			print "Group02Button01 enabled now ", Group02Button01[7]
			
			# turns off the corresponding button in the group
			print "Group02Button02enabled was ", Group02Button02[7]
			Group02Button02[7] = False
			print "Group02Button02enabled now ", Group02Button02[7]


			print "old color", Group02Button01[8]
			Group02Button01[8] = UI_button_selected_color
			print "new color", Group02Button01[8]
			
			### -------------------------- ###
			# UPDATE Group02Button01 button
			
			button_name =  "Group02Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 300
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group02Button01[7]
			buttonColor = Group02Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)

			# NOTE HERE:
			# this next part updates the OTHER button, both this section adn the define button then add button to display lit are necessary. 
			# updates the OTHER button in the group			
			button_name =  "Group02Button02"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 280
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group02Button02[7]
			buttonColor = Group02Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	


			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		
		if Group02Button01[7] == True:
			print "Group02Button01 enabled was ", Group02Button01[7]
			Group02Button01[7] = False
			Group02Button02[7] = True
			print "Group02Button01 enabled now", Group02Button01[7]
			print "old color", Group02Button01[8]
			Group02Button01[8] = UI_button_color
			print "new color", Group02Button01[8]

			### -------------------------- ###
			# UPDATE Group02Button01 button
			
			button_name =  "Group02Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 300
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group02Button01[7]
			buttonColor = Group02Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group02Button02"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 280
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group02Button02[7]
			buttonColor = Group02Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
			
			return

	if selected_button == Group02Button02[0]:
		print "clicked button is", Group02Button02[0]
		if Group02Button02[7] == False:
			print "Group02Button02 enabled was ", Group02Button02[7]
			Group02Button02[7] = True
			Group02Button01[7] = False
			print "Group02Button02 enabled now ", Group02Button02[7]
			print "old color", Group02Button02[8]
			Group02Button02[8] = UI_button_selected_color
			print "new color", Group02Button02[8]
			
			### -------------------------- ###
			# UPDATE Group02Button02 button
			
			button_name =  "Group02Button02"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 280
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group02Button02[7]
			buttonColor = Group02Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group02Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 300
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group02Button01[7]
			buttonColor = Group02Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###


			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		
		if Group02Button02[7] == True:
			print "Group02Button02 enabled was ", Group02Button02[7]
			Group02Button02[7] = False
			Group02Button01[7] = True
			print "Group02Button02 enabled now", Group02Button02[7]
			print "old color", Group02Button02[8]
			Group02Button02[8] = UI_button_color
			print "new color", Group02Button02[8]

			### -------------------------- ###
			# UPDATE Group02Button02 button
			
			button_name =  "Group02Button02"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 280
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option B"
			buttonType = "group"
			buttonEnabled = Group02Button02[7]
			buttonColor = Group02Button02[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			# updates the OTHER button in the group			
			button_name =  "Group02Button01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 300
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Option A"
			buttonType = "group"
			buttonEnabled = Group02Button01[7]
			buttonColor = Group02Button01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###

			for i, button in enumerate(my_buttons):
				button.display()
			
			return

	#####################################################################
	# # # ------------------------- END BUTTON GROUP02 ------------------ # # # 
	#####################################################################		

	
	# # # Check FPS button
	if selected_button == fps[0]:
		print "clicked button is", fps[0]
		if fps[7] == False:
			print "fps enabled was ", fps[7]
			fps[7] = True
			print "fps enabled now ", fps[7]
			print "old color", fps[8]
			fps[8] = UI_button_selected_color
			print "new color", fps[8]
			
			### -------------------------- ###
			# UPDATE fps button
			
			button_name =  "fps"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 180
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "FPS"
			buttonType = "sticky"
			buttonEnabled = fps[7]
			buttonColor = fps[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		
		if fps[7] == True:
			print "fps enabled was ", fps[7]
			fps[7] = False
			print "fps enabled now", fps[7]
			print "old color", fps[8]
			fps[8] = UI_button_color
			print "new color", fps[8]

			### -------------------------- ###
			# UPDATE fps button
			
			button_name =  "fps"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 180
			button_width = UI_sideBar_width / 3
			button_height = 20
			button_label_txt = "FPS"
			buttonType = "sticky"
			buttonEnabled = fps[7]
			buttonColor = fps[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
			
			return


	# # # Check sticky01 button
	if selected_button == sticky01[0]:
		print "clicked button is", sticky01[0]
		if sticky01[7] == False:
			print "sticky01 enabled was ", sticky01[7]
			sticky01[7] = True
			print "sticky01 enabled now ", sticky01[7]
			print "old color", sticky01[8]
			sticky01[8] = UI_button_selected_color
			print "new color", sticky01[8]
			
			### -------------------------- ###
			# UPDATE sticky01 button
			
			button_name =  "Sticky01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 120
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Sticky Button 01"
			buttonType = "sticky"
			buttonEnabled = sticky01[7]
			buttonColor = sticky01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
						
			return
		


		if sticky01[7] == True:
			print "sticky01 enabled was ", sticky01[7]
			sticky01[7] = False
			print "sticky01 enabled now", sticky01[7]
			print "old color", sticky01[8]
			sticky01[8] = UI_button_color
			print "new color", sticky01[8]

			### -------------------------- ###
			# UPDATE sticky01 button
			
			button_name =  "Sticky01"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 120
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Sticky Button 01"
			buttonType = "sticky"
			buttonEnabled = sticky01[7]
			buttonColor = sticky01[8]
			buttonVisible = True

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
			
			return

	### --- check sticky02 button, enable / disable when clicked --- ###

	if selected_button == sticky02[0]:
		print "clicked button is", sticky02[0]
		if sticky02[7] == False:
			print "sticky02 enabled was ", sticky02[7]
			sticky02[7] = True
			print "sticky02 enabled now ", sticky02[7]
			print "old color", sticky02[8]
			sticky02[8] = UI_button_selected_color
			print "new color", sticky02[8]
			
			### -------------------------- ###
			# UPDATE sticky02 button
			
			button_name =  "Sticky02"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 140
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Sticky Button 02"
			buttonType = "sticky"
			buttonEnabled = sticky02[7]
			buttonColor = sticky02[8]
			buttonVisible = True
		
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
			
			return
		


		if sticky02[7] == True:
			print "sticky01 enabled was ", sticky02[7]
			sticky02[7] = False
			print "sticky02 enabled now", sticky02[7]
			print "old color", sticky02[8]
			sticky02[8] = UI_button_color
			print "new color", sticky02[8]

			### -------------------------- ###
			# UPDATE sticky02 button
			
			button_name =  "Sticky02"
			button_origin_x = 0									#x0, y0 is upper left corner
			button_origin_y = pygame_window_height - 140
			button_width = UI_sideBar_width
			button_height = 20
			button_label_txt = "Sticky Button 02"
			buttonType = "sticky"
			buttonEnabled = sticky02[7]
			buttonColor = sticky02[8]
			buttonVisible = True
		
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()

			return	

# ************************************************************************************


# ************************************************************************************
#	classes		#

## takes button info and prepares it for displaying
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

	## displays buttons
	def display(self):

		# render "pushy" type buttons
		if self.buttonType == "pushy":
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))
		
		# render "sticky" type buttons
		if self.buttonType == "sticky":		
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))
		
		# render "label" type buttons
		if self.buttonType == "label":
			self.color = UI_label_color																	# since self.color = buttonColor by default, this overwrites that for labels
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			#pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "group" type buttons
		if self.buttonType == "group":		
			if self.buttonEnabled == True:
				self.color = UI_button_selected_color
			if self.buttonEnabled == False:
				self.color = UI_button_color
			
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))


		# render "dropdown" type buttons
		if self.buttonType == "dropdown":		
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "dropdown - lists" type buttons
		if self.buttonType == "dropdown_option":
			if self.buttonVisible == True:		
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 1)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))
		
			if self.buttonVisible == False:
				self.color = black
				self.colorBorder = black
				self.button_label_txt = ""

				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 1)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))

		# render "sticky" type buttons
		if self.buttonType == "menu":		
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))


		# render "dropdown - lists" type buttons
		if self.buttonType == "menu_option":
			if self.buttonVisible == True:		
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 1)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))
		
			if self.buttonVisible == False:
				self.color = black
				self.colorBorder = black
				self.button_label_txt = ""

				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 1)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))


# ************************************************************************************



# ************************************************************************************
#	BUTTON TYPES
#
#	pushy 	- a button that activates temporarily when clicked, does not stay on, or is linked to any other buttons
#	sticky 	- a button that when click stays on, like a check box, when clicked again, turns off
#	label 	- label is just text, not a button)
#	group 	- a button that is part of an option group, when clicked, only that one button enables, and disables the others in the group







# ************************************************************************************
# 	V       DEFINE BUTTONS HERE    V
# ************************************************************************************

number_of_buttons = 20
my_buttons = []

for n in range(1):

	### these are all the buttons, the my_buttons.append(created_button) iterates through displaying them and
	### a seperate dictionary is created for each button





	### -------------------------- ###
	# create Menu02 button
	button_name = "Menu02"
	button_origin_x = UI_sideBar_width + 100								#x0, y0 is upper left corner
	button_origin_y = 0
	button_width = 100
	button_height = 20
	button_label_txt = "Menu 02"
	buttonType = "menu"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Menu02"
	buttonVisible = True

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	# create button dictionary
	menu02 = {}
	menu02[0] = button_name
	menu02[1] = button_origin_x
	menu02[2] = button_origin_y
	menu02[3] = button_width
	menu02[4] = button_height
	menu02[5] = button_label_txt
	menu02[6] = buttonType
	menu02[7] = buttonEnabled
	menu02[8] = buttonColor
	menu02[9] = buttonGroup
	menu02[10] = buttonVisible
	### -------------------------- ###



	###################################################################
	######                                           START OF MENU 01 GROUP                                            ######
	###################################################################

	### -------------------------- ###

	# create Menu 01  option 02
	button_name =  "Menu01option02"
	button_origin_x = UI_sideBar_width								#x0, y0 is upper left corner
	button_origin_y = 40
	button_width = 150				
	button_height = 20
	button_label_txt = "Menu Option 2"
	buttonType = "menu_option"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Menu01"
	buttonVisible = True
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Menu01option02 = {}
	Menu01option02[0] = button_name
	Menu01option02[1] = button_origin_x
	Menu01option02[2] = button_origin_y
	Menu01option02[3] = button_width
	Menu01option02[4] = button_height
	Menu01option02[5] = button_label_txt
	Menu01option02[6] = buttonType
	Menu01option02[7] = buttonEnabled
	Menu01option02[8] = buttonColor
	Menu01option02[9] = buttonGroup
	Menu01option02[10] = buttonVisible

	### -------------------------- ###



	# create Menu 01  option 01
	button_name =  "Menu01option01"
	button_origin_x = UI_sideBar_width								#x0, y0 is upper left corner
	button_origin_y = 20
	button_width = 150				
	button_height = 20
	button_label_txt = "Menu Option 1"
	buttonType = "menu_option"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Menu01"
	buttonVisible = True
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Menu01option01 = {}
	Menu01option01[0] = button_name
	Menu01option01[1] = button_origin_x
	Menu01option01[2] = button_origin_y
	Menu01option01[3] = button_width
	Menu01option01[4] = button_height
	Menu01option01[5] = button_label_txt
	Menu01option01[6] = buttonType
	Menu01option01[7] = buttonEnabled
	Menu01option01[8] = buttonColor
	Menu01option01[9] = buttonGroup
	Menu01option01[10] = buttonVisible

	### -------------------------- ###



	### -------------------------- ###
	# create Menu01 button
	button_name = "Menu01"
	button_origin_x = UI_sideBar_width								#x0, y0 is upper left corner
	button_origin_y = 0
	button_width = 100
	button_height = 20
	button_label_txt = "Menu 01"
	buttonType = "menu"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Menu01"
	buttonVisible = True

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	# create button dictionary
	menu01 = {}
	menu01[0] = button_name
	menu01[1] = button_origin_x
	menu01[2] = button_origin_y
	menu01[3] = button_width
	menu01[4] = button_height
	menu01[5] = button_label_txt
	menu01[6] = buttonType
	menu01[7] = buttonEnabled
	menu01[8] = buttonColor
	menu01[9] = buttonGroup
	menu01[10] = buttonVisible
	### -------------------------- ###

	###################################################################
	######                                            END OF MENU 01 GROUP                                               ######
	###################################################################





	###################################################################
	######                                            START OF DROPDOWN01 GROUP                                  ######
	###################################################################


	### -------------------------- ###
	# create Dropdown 01  option 03
	button_name =  "Dropdown01option03"
	button_origin_x = UI_sideBar_width								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 440
	button_width = 100					
	button_height = 20
	button_label_txt = "Option 3"
	buttonType = "dropdown_option"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Dropdown01"
	buttonVisible = False
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Dropdown01option03 = {}
	Dropdown01option03[0] = button_name
	Dropdown01option03[1] = button_origin_x
	Dropdown01option03[2] = button_origin_y
	Dropdown01option03[3] = button_width
	Dropdown01option03[4] = button_height
	Dropdown01option03[5] = button_label_txt
	Dropdown01option03[6] = buttonType
	Dropdown01option03[7] = buttonEnabled
	Dropdown01option03[8] = buttonColor
	Dropdown01option03[9] = buttonGroup
	Dropdown01option03[10] = buttonVisible

	### -------------------------- ###


	### -------------------------- ###
	# create Dropdown 01  
	button_name =  "Dropdown01option02"
	button_origin_x = UI_sideBar_width								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 460
	button_width = 100					
	button_height = 20
	button_label_txt = "Option 2"
	buttonType = "dropdown_option"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Dropdown01"
	buttonVisible = False
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Dropdown01option02 = {}
	Dropdown01option02[0] = button_name
	Dropdown01option02[1] = button_origin_x
	Dropdown01option02[2] = button_origin_y
	Dropdown01option02[3] = button_width
	Dropdown01option02[4] = button_height
	Dropdown01option02[5] = button_label_txt
	Dropdown01option02[6] = buttonType
	Dropdown01option02[7] = buttonEnabled
	Dropdown01option02[8] = buttonColor
	Dropdown01option02[9] = buttonGroup
	Dropdown01option02[10] = buttonVisible

	### -------------------------- ###


	### -------------------------- ###
	# create Dropdown 01  
	button_name =  "Dropdown01option01"
	button_origin_x = UI_sideBar_width								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 480
	button_width = 100 					
	button_height = 20
	button_label_txt = "Option 1"
	buttonType = "dropdown_option"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Dropdown01"
	buttonVisible = False
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Dropdown01option01 = {}
	Dropdown01option01[0] = button_name
	Dropdown01option01[1] = button_origin_x
	Dropdown01option01[2] = button_origin_y
	Dropdown01option01[3] = button_width
	Dropdown01option01[4] = button_height
	Dropdown01option01[5] = button_label_txt
	Dropdown01option01[6] = buttonType
	Dropdown01option01[7] = buttonEnabled
	Dropdown01option01[8] = buttonColor
	Dropdown01option01[9] = buttonGroup
	Dropdown01option01[10] = buttonVisible

	### -------------------------- ###


	### -------------------------- ###
	# create Dropdown 01  
	button_name =  "Dropdown01opener"
	button_origin_x = UI_sideBar_width - 20								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 480
	button_width = 20 					
	button_height = 20
	button_label_txt = ">>"
	buttonType = "sticky"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Dropdown01"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Dropdown01opener = {}
	Dropdown01opener[0] = button_name
	Dropdown01opener[1] = button_origin_x
	Dropdown01opener[2] = button_origin_y
	Dropdown01opener[3] = button_width
	Dropdown01opener[4] = button_height
	Dropdown01opener[5] = button_label_txt
	Dropdown01opener[6] = buttonType
	Dropdown01opener[7] = buttonEnabled
	Dropdown01opener[8] = buttonColor
	Dropdown01opener[9] = buttonGroup

	### -------------------------- ###

	### -------------------------- ###
	# create Dropdown 01  
	button_name =  "Dropdown01Display"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 480
	button_width = UI_sideBar_width - 20 					
	button_height = 20
	button_label_txt = "select option"
	buttonType = "sticky"							# this should be sticky, but no fucntionality for it yet in match button. 
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Dropdown01"
	buttonVisible = True
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Dropdown01Display = {}
	Dropdown01Display[0] = button_name
	Dropdown01Display[1] = button_origin_x
	Dropdown01Display[2] = button_origin_y
	Dropdown01Display[3] = button_width
	Dropdown01Display[4] = button_height
	Dropdown01Display[5] = button_label_txt
	Dropdown01Display[6] = buttonType
	Dropdown01Display[7] = buttonEnabled
	Dropdown01Display[8] = buttonColor
	Dropdown01Display[9] = buttonGroup
	Dropdown01Display[10] = buttonVisible

	### -------------------------- ###


	### -------------------------- ###
	# create Dropdown 01 Label  
	button_name =  "Dropdown01Label"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 500
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Dropdown 01"
	buttonType = "label"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Dropdown01 = {}
	Dropdown01[0] = button_name
	Dropdown01[1] = button_origin_x
	Dropdown01[2] = button_origin_y
	Dropdown01[3] = button_width
	Dropdown01[4] = button_height
	Dropdown01[5] = button_label_txt
	Dropdown01[6] = buttonType
	Dropdown01[7] = buttonEnabled
	Dropdown01[8] = buttonColor

	### -------------------------- ###

	###################################################################
	######                                            END OF DROPDOWN01 GROUP                                       ######
	###################################################################



	### -------------------------- ###
	# create Group 04 Button 03  
	button_name =  "Group04Button03"
	button_origin_x = (UI_sideBar_width / 3) + (UI_sideBar_width / 3)								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 420
	button_width = UI_sideBar_width / 3					
	button_height = 20
	button_label_txt = "   C   "
	buttonType = "group"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Group04"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group04Button03 = {}
	Group04Button03[0] = button_name
	Group04Button03[1] = button_origin_x
	Group04Button03[2] = button_origin_y
	Group04Button03[3] = button_width
	Group04Button03[4] = button_height
	Group04Button03[5] = button_label_txt
	Group04Button03[6] = buttonType
	Group04Button03[7] = buttonEnabled
	Group04Button03[8] = buttonColor
	Group04Button03[9] = buttonGroup
	### -------------------------- ###




	### -------------------------- ###
	# create Group 04 Button 02  
	button_name =  "Group04Button02"
	button_origin_x = UI_sideBar_width / 3								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 420
	button_width = UI_sideBar_width / 3					
	button_height = 20
	button_label_txt = "   B   "
	buttonType = "group"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Group04"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group04Button02 = {}
	Group04Button02[0] = button_name
	Group04Button02[1] = button_origin_x
	Group04Button02[2] = button_origin_y
	Group04Button02[3] = button_width
	Group04Button02[4] = button_height
	Group04Button02[5] = button_label_txt
	Group04Button02[6] = buttonType
	Group04Button02[7] = buttonEnabled
	Group04Button02[8] = buttonColor
	Group04Button02[9] = buttonGroup
	### -------------------------- ###



	### -------------------------- ###
	# create Group 04 Button 01  
	button_name =  "Group04Button01"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 420
	button_width = UI_sideBar_width / 3					
	button_height = 20
	button_label_txt = "   A   "
	buttonType = "group"
	buttonEnabled = True 
	buttonColor = UI_button_color
	buttonGroup = "Group04"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group04Button01 = {}
	Group04Button01[0] = button_name
	Group04Button01[1] = button_origin_x
	Group04Button01[2] = button_origin_y
	Group04Button01[3] = button_width
	Group04Button01[4] = button_height
	Group04Button01[5] = button_label_txt
	Group04Button01[6] = buttonType
	Group04Button01[7] = buttonEnabled
	Group04Button01[8] = buttonColor
	Group04Button01[9] = buttonGroup
	### -------------------------- ###




	### -------------------------- ###
	# create Group 04 Label  
	button_name =  "Group04Label"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 440
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Group 04"
	buttonType = "label"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group04Label = {}
	Group04Label[0] = button_name
	Group04Label[1] = button_origin_x
	Group04Label[2] = button_origin_y
	Group04Label[3] = button_width
	Group04Label[4] = button_height
	Group04Label[5] = button_label_txt
	Group04Label[6] = buttonType
	Group04Label[7] = buttonEnabled
	Group04Label[8] = buttonColor

	### -------------------------- ###




	### -------------------------- ###
	# create Group 03 Button 02  
	button_name =  "Group03Button02"
	button_origin_x = UI_sideBar_width / 2								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 360
	button_width = UI_sideBar_width / 2 					
	button_height = 20
	button_label_txt = "Option B"
	buttonType = "group"
	buttonEnabled = False
	buttonColor = UI_button_color
	buttonGroup = "Group03"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group03Button02 = {}
	Group03Button02[0] = button_name
	Group03Button02[1] = button_origin_x
	Group03Button02[2] = button_origin_y
	Group03Button02[3] = button_width
	Group03Button02[4] = button_height
	Group03Button02[5] = button_label_txt
	Group03Button02[6] = buttonType
	Group03Button02[7] = buttonEnabled
	Group03Button02[8] = buttonColor
	Group03Button02[9] = buttonGroup
	### -------------------------- ###


	### -------------------------- ###
	# create Group 03 Button 01  
	button_name =  "Group03Button01"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 360
	button_width = UI_sideBar_width / 2 					
	button_height = 20
	button_label_txt = "Option A"
	buttonType = "group"
	buttonEnabled = True 
	buttonColor = UI_button_color
	buttonGroup = "Group03"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group03Button01 = {}
	Group03Button01[0] = button_name
	Group03Button01[1] = button_origin_x
	Group03Button01[2] = button_origin_y
	Group03Button01[3] = button_width
	Group03Button01[4] = button_height
	Group03Button01[5] = button_label_txt
	Group03Button01[6] = buttonType
	Group03Button01[7] = buttonEnabled
	Group03Button01[8] = buttonColor
	Group03Button01[9] = buttonGroup
	### -------------------------- ###


	### -------------------------- ###
	# create Group 03 Label  
	button_name =  "Group03Label"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 380
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Group 03"
	buttonType = "label"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group03Label = {}
	Group03Label[0] = button_name
	Group03Label[1] = button_origin_x
	Group03Label[2] = button_origin_y
	Group03Label[3] = button_width
	Group03Label[4] = button_height
	Group03Label[5] = button_label_txt
	Group03Label[6] = buttonType
	Group03Label[7] = buttonEnabled
	Group03Label[8] = buttonColor

	### -------------------------- ###



	### -------------------------- ###
	# create Goup 02 Button 02 
	button_name =  "Group02Button02"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 280
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Option B"
	buttonType = "group"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Group02"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group02Button02 = {}
	Group02Button02[0] = button_name
	Group02Button02[1] = button_origin_x
	Group02Button02[2] = button_origin_y
	Group02Button02[3] = button_width
	Group02Button02[4] = button_height
	Group02Button02[5] = button_label_txt
	Group02Button02[6] = buttonType
	Group02Button02[7] = buttonEnabled
	Group02Button02[8] = buttonColor
	Group02Button02[9] = buttonGroup



	### -------------------------- ###



	### -------------------------- ###
	# create Goup 02 Button 01  
	button_name =  "Group02Button01"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 300
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Option A"
	buttonType = "group"
	buttonEnabled = True 
	buttonColor = UI_button_color
	buttonGroup = "Group02"
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group02Button01 = {}
	Group02Button01[0] = button_name
	Group02Button01[1] = button_origin_x
	Group02Button01[2] = button_origin_y
	Group02Button01[3] = button_width
	Group02Button01[4] = button_height
	Group02Button01[5] = button_label_txt
	Group02Button01[6] = buttonType
	Group02Button01[7] = buttonEnabled
	Group02Button01[8] = buttonColor
	Group02Button01[9] = buttonGroup

	print "Group02Button01[0] = ", Group02Button01[0]

	### -------------------------- ###


	### -------------------------- ###
	# create Goup 02 Label  
	button_name =  "Group02Label"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 320
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Group 02"
	buttonType = "label"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group02Label = {}
	Group02Label[0] = button_name
	Group02Label[1] = button_origin_x
	Group02Label[2] = button_origin_y
	Group02Label[3] = button_width
	Group02Label[4] = button_height
	Group02Label[5] = button_label_txt
	Group02Label[6] = buttonType
	Group02Label[7] = buttonEnabled
	Group02Label[8] = buttonColor

	### -------------------------- ###


	### -------------------------- ###
	# create Label 01 Group Button
	button_name =  "Label01ButtonA"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 220
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Button A"
	buttonType = "pushy"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	Group01Button01 = {}
	Group01Button01[0] = button_name
	Group01Button01[1] = button_origin_x
	Group01Button01[2] = button_origin_y
	Group01Button01[3] = button_width
	Group01Button01[4] = button_height
	Group01Button01[5] = button_label_txt
	Group01Button01[6] = buttonType
	Group01Button01[7] = buttonEnabled
	Group01Button01[8] = buttonColor

	### -------------------------- ###


	### -------------------------- ###
	# create Label 01 
	button_name =  "Label01"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 240
	button_width = UI_sideBar_width 					
	button_height = 20
	button_label_txt = "Label 01 Group"
	buttonType = "label"
	buttonEnabled = False 
	buttonColor = UI_label_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	label01 = {}
	label01[0] = button_name
	label01[1] = button_origin_x
	label01[2] = button_origin_y
	label01[3] = button_width
	label01[4] = button_height
	label01[5] = button_label_txt
	label01[6] = buttonType
	label01[7] = buttonEnabled
	label01[8] = buttonColor

	### -------------------------- ###

	### -------------------------- ###
	# create FPS button
	button_name =  "FPS"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 180
	button_width = UI_sideBar_width / 3				# /3 for a small button, 1/3 the bar width
	button_height = 20
	button_label_txt = "FPS"
	buttonType = "sticky"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	fps = {}
	fps[0] = button_name
	fps[1] = button_origin_x
	fps[2] = button_origin_y
	fps[3] = button_width
	fps[4] = button_height
	fps[5] = button_label_txt
	fps[6] = buttonType
	fps[7] = buttonEnabled
	fps[8] = buttonColor

	### -------------------------- ###


	### -------------------------- ###
	# create sticky02 button
	button_name =  "Sticky02"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 140
	button_width = UI_sideBar_width
	button_height = 20
	button_label_txt = "Sticky Button 02"
	buttonType = "sticky"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	# create button dictionary
	sticky02 = {}
	sticky02[0] = button_name
	sticky02[1] = button_origin_x
	sticky02[2] = button_origin_y
	sticky02[3] = button_width
	sticky02[4] = button_height
	sticky02[5] = button_label_txt
	sticky02[6] = buttonType
	sticky02[7] = buttonEnabled
	sticky02[8] = buttonColor

	print "sticky02 button dictionary"
	print sticky02
	### -------------------------- ###




	### -------------------------- ###
	# create sticky01 button
	button_name =  "Sticky01"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 120
	button_width = UI_sideBar_width
	button_height = 20
	button_label_txt = "Sticky Button 01"
	buttonType = "sticky"
	buttonEnabled = False 
	buttonColor = UI_button_color
	
	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	# create button dictionary
	sticky01 = {}
	sticky01[0] = button_name
	sticky01[1] = button_origin_x
	sticky01[2] = button_origin_y
	sticky01[3] = button_width
	sticky01[4] = button_height
	sticky01[5] = button_label_txt
	sticky01[6] = buttonType
	sticky01[7] = buttonEnabled
	sticky01[8] = buttonColor


	print "sticky01 button dictionary"
	print sticky01
	### -------------------------- ###	




	### -------------------------- ###
	# create command02 button
	button_name = "Command02"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 80
	button_width = UI_sideBar_width
	button_height = 20
	button_label_txt = "Command 02"
	buttonType = "pushy"
	buttonEnabled = False 
	buttonColor = UI_button_color

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	# create button dictionary
	cmd02 = {}
	cmd02[0] = button_name
	cmd02[1] = button_origin_x
	cmd02[2] = button_origin_y
	cmd02[3] = button_width
	cmd02[4] = button_height
	cmd02[5] = button_label_txt
	cmd02[6] = buttonType
	cmd02[7] = buttonEnabled
	cmd02[8] = buttonColor
	### -------------------------- ###



	### -------------------------- ###
	# create command01 button
	button_name = "Command01"
	button_origin_x = 0								#x0, y0 is upper left corner
	button_origin_y = pygame_window_height - 60
	button_width = UI_sideBar_width
	button_height = 20
	button_label_txt = "Command 01"
	buttonType = "pushy"
	buttonEnabled = False 
	buttonColor = UI_button_color
	buttonGroup = "Command01"
	buttonVisible = True

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	# create button dictionary
	cmd01 = {}
	cmd01[0] = button_name
	cmd01[1] = button_origin_x
	cmd01[2] = button_origin_y
	cmd01[3] = button_width
	cmd01[4] = button_height
	cmd01[5] = button_label_txt
	cmd01[6] = buttonType
	cmd01[7] = buttonEnabled
	cmd01[8] = buttonColor
	cmd01[9] = buttonGroup
	cmd01[10] = buttonVisible
	### -------------------------- ###




	### -------------------------- ###
	# create exit button
	button_name = "EXIT"
	button_origin_x = 0
	button_origin_y = pygame_window_height - 20
	button_width = UI_sideBar_width
	button_height = 20
	button_label_txt = "EXIT"
	buttonType = "pushy"
	buttonEnabled = False
	buttonColor = UI_button_color
	buttonGroup = "exit"
	buttonVisible = True

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

	# create button dictionary
	exit = {}
	exit[0] = button_name
	exit[1] = button_origin_x
	exit[2] = button_origin_y
	exit[3] = button_width
	exit[4] = button_height
	exit[5] = button_label_txt
	exit[6] = buttonType
	exit[7] = buttonEnabled
	exit[8] = buttonColor
	exit[9] = buttonGroup
	exit[10] = buttonVisible
	### -------------------------- ###



# ************************************************************************************
# 	MAIN code	#


# Pygame display
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption('My Program Name')

running = True

while running:

	# DRAW SCREEN
	# py grame will draw the elements from start to finish based on the order below, background first
	# then foreground elements. Each one will draw over the one before it. if you draw the background last
	# the whole screen is overwritten

	# # always running logic (like count FPS)


	# # draw background
	screen.fill(background_color)

	# # draw reference or background lines, like grids here
	if fps[7] == True:
		count_fps()
		show_fps()

	# # draw borders & frames for interface
	pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
	pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))

	# pygame event monitoring
	# pygame scans for mouse and keyboard events and takes actions accordingly

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:					#mousebuttondown only runs once, things run outside if this if loop
			(mouseX, mouseY) = pygame.mouse.get_pos()				# will run continually while button is held down
			print "mouseX = ", mouseX, "mouseY = ", mouseY
			selected_button = findButton(my_buttons, mouseX, mouseY)
			print "selected button = ", selected_button

			if selected_button != None:

				if selected_button.buttonType == "sticky":
					matchButton(selected_button.button_name)

				if selected_button.buttonType == "group":
					matchButton(selected_button.button_name)

				if selected_button.buttonType == "dropdown_option":
					matchButton(selected_button.button_name)

				if selected_button.buttonType == "pushy":
					selected_button.color = UI_button_click_color
					print "clicked button is a pushy temporary button"

				if selected_button.buttonType == "label":
					selected_button.color = UI_label_color
					print "clicked button is a label, not a button"

		if event.type == pygame.MOUSEBUTTONUP:
			if selected_button != None:
				selected_button.color = UI_button_color 			#reverts button back to normal color after letting go of mouse
			selected_button = None


	if selected_button != None:
		(mouseX, mouseY) = pygame.mouse.get_pos()
		selected_button.color = UI_button_click_color
		pygame.display.flip()


		if selected_button.button_label_txt == "EXIT":
			print "you pressed exit"
			running = False

	# # draw buttons!
	for i, button in enumerate(my_buttons):
		button.display()


	pygame.display.flip()		 # updates and draws the screen & launch pygame window


