# gui test

# ************************************************************************************
# 	import modules	#
# ************************************************************************************

import pygame
import random
import math
import sys
import time 			# for FPS functions


# ************************************************************************************
#	initial variables	#
# ************************************************************************************


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
pygame_window_width = 800
pygame_window_height = 800

# by default, no UI objects are selected at start
selected_uiObject = None					
selected_button = None


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
# 	functions  
# ************************************************************************************************************************
# ************************************************************************************************************************



def findButton(buttons, x, y):
	for b in buttons:
		#print "x = ", x, "y = ", y
		#print "b.x = ", b.x, "b.x width = ", b.x + b.x_width
		#print "b.y = ", b.y, "b.y height = ", b.y + b.y_height
		if x <= b.x + b.x_width:
			if x >= b.x:
				#print "x ok"
				if y >= b.y:
					if y <= b.y + b.y_height:
						#print "Y ok, button found"
						print "selected button label_txt = ", b.button_name
						#print "this is return b", b 
						return b
	return None





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



# ************************************************************************************************************************
# ************************************************************************************************************************
# 	button dictionaries	#
# ************************************************************************************************************************
# ************************************************************************************************************************

button00 = {}
button00[0] = "button00"
button00[1] = 0
button00[2] = 100
button00[3] = UI_sideBar_width
button00[4] = 20
button00[5] = "Button 00"
button00[6] = "pushy"
button00[7] = True
button00[8] = UI_button_color
button00[9] = "button00"
button00[10] = True

button01 = {}
button01[0] = "button01"
button01[1] = 0
button01[2] = 200
button01[3] = UI_sideBar_width
button01[4] = 20
button01[5] = "Button 01"
button01[6] = "pushy"
button01[7] = True
button01[8] = UI_button_color
button01[9] = "button01"
button01[10] = True

button02 = {}
button02[0] = "button02"
button02[1] = 0
button02[2] = 300
button02[3] = UI_sideBar_width
button02[4] = 20
button02[5] = "Button 02"
button02[6] = "pushy"
button02[7] = True
button02[8] = UI_button_color
button02[9] = "button02"
button02[10] = True

button03 = {}
button03[0] = "button03"
button03[1] = 0
button03[2] = 400
button03[3] = UI_sideBar_width
button03[4] = 20
button03[5] = "Button 03"
button03[6] = "pushy"
button03[7] = True
button03[8] = UI_button_color
button03[9] = "button03"
button03[10] = True

button04 = {}
button04[0] = "button04"
button04[1] = 0
button04[2] = 500
button04[3] = UI_sideBar_width
button04[4] = 20
button04[5] = "Button 04"
button04[6] = "pushy"
button04[7] = True
button04[8] = UI_button_color
button04[9] = "button04"
button04[10] = True


allButtons = {}
allButtons[0] = button00
allButtons[1] = button01
allButtons[2] = button02
allButtons[3] = button03
allButtons[4] = button04

"""
#for reference only
button02 = {}
button02[0] = button_name
button02[1] = button_origin_x
button02[2] = button_origin_y
button02[3] = button_width
button02[4] = button_height
button02[5] = button_label_txt
button02[6] = buttonType
button02[7] = buttonEnabled
button02[8] = buttonColor
button02[9] = buttonGroup
button02[10] = buttonVisible
"""


# ************************************************************************************************************************
# ************************************************************************************************************************
# 	create buttons	#
# ************************************************************************************************************************
# ************************************************************************************************************************

buttonToDraw = {}
#number_of_buttons = 2
my_buttons = []

for n in range(1):
	# source info for this part: https://realpython.com/iterate-through-dictionary-python/

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
		print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width

"""
	buttonToDraw = button03

	### -------------------------- ###
	# button02 
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
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width



	### -------------------------- ###
	# drop down button
	button_name = "Dropdown01option"
	button_origin_x = UI_sideBar_width - 20
	button_origin_y = pygame_window_height - 300
	button_width = 20
	button_height = 20
	button_label_txt = ">>"
	buttonType = "pushy"
	buttonEnabled = False
	buttonColor = UI_button_color
	buttonGroup = "Dropdown01"
	buttonVisible = True

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width


	### -------------------------- ###
	# drop down button
	button_name = "Dropdown01option"
	button_origin_x = 0
	button_origin_y = pygame_window_height - 300
	button_width = UI_sideBar_width - 20
	button_height = 20
	button_label_txt = "select option"
	buttonType = "pushy"
	buttonEnabled = False
	buttonColor = UI_button_color
	buttonGroup = "Dropdown01"
	buttonVisible = True

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible)
	my_buttons.append(created_button)
	print "button origin x", button_origin_x, "button width pos", button_origin_x + button_width




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

"""





# ************************************************************************************************************************
# ************************************************************************************************************************
# 	MAIN code	#
# ************************************************************************************************************************
# ************************************************************************************************************************

####### INITIALIZE DISPLAY ##########

# # Pygame display
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption('My Program Name')


# # #  draw background
screen.fill(background_color)

# # draw borders & frames for interface
pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))

# # draw buttons!
for i, button in enumerate(my_buttons):
	button.display()


########## EVENT MONITORING / UPDATE DISPLAY ########### 


running = True

while running:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if event.type == pygame.MOUSEBUTTONDOWN:					#mousebuttondown only runs once, things run outside if this if loop
		(mouseX, mouseY) = pygame.mouse.get_pos()				# will run continually while button is held down
		print "mouseX = ", mouseX, "mouseY = ", mouseY
		selected_button = findButton(my_buttons, mouseX, mouseY)
		print "selected button = ", selected_button

		#if selected_button != None:
		# process clicked buttons


	if selected_button != None:
		(mouseX, mouseY) = pygame.mouse.get_pos()
		selected_button.color = UI_button_click_color
		pygame.display.flip()


		if selected_button.button_label_txt == "EXIT":
			print "you pressed exit"
			running = False

	# always do this last
	pygame.display.flip()