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
pygame_window_width = 1200
pygame_window_height = 1200

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









# ************************************************************************************************************************
# ************************************************************************************************************************
# 	functions  
# ************************************************************************************************************************
# ************************************************************************************************************************


my_buttons = []			#initializes my_buttons list, each button is added to this for display
buttonToDraw = {}			#each button is loaded into this dictionary, added to my_buttons list

def defineButtons():
	# source info for this part: https://realpython.com/iterate-through-dictionary-python/
	print "defineButtons() - started"
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


	print "defineButtons() - completed"




# # This figures out which button was clicked
def findButton(buttons, x, y):
	for b in buttons:
		if x <= b.x + b.x_width:
			if x >= b.x:
				if y >= b.y:
					if y <= b.y + b.y_height:
						print "selected button label_txt = ", b.button_name
						return b
	return None




# # this updates buttons and any buttons in the same button group based on actions taken
buttonToCheck = {}
def updateButton(selected_button):
	print "updateButton() - started"
	print "selected_button = ", selected_button

	"""
	# for sticky buttons, iterate through nested allButtons dictionary and flip buttonEnabled
	for allButtonsID, allButtonsValue in allButtons.items():
		for key in allButtonsValue:
			#print "key", key
			#buttonToCheck[key] = allButtonsValue[key]
			#print "buttonToCheck", key, allButtonsValue[key]
			if allButtonsValue[key] == "sticky":
				print "found a sticky button"
				print "key, ", key, "value", allButtonsValue[key]
				#print "buttonToCheck", key, allButtonsValue[key]
	"""

	
	if selected_button == "sticky01":
		if button04[7] == False:
			print "sticky 01 button found"
			button04[7] = True
			button04[8] = UI_button_selected_color
			print "flipped sticky01 from false to true"
			
			defineButtons()	#if this is uncommented, sticky buttons work, but stop pushy buttons from working. 
			
		elif button04[7] == True:
			print "sticky 01 button found"
			button04[7] = False
			button04[8] = UI_button_color
			print "flipped stick01 from true to false"
			
			defineButtons()
			

	print "updateButton() - completed"
	return
	

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
			print "drawing pushy button: ", self.button_name
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "sticky" type buttons
		elif self.buttonType == "sticky":	
			print "drawing sticky button: ", self.button_name	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "label" type buttons
		elif self.buttonType == "label":
			print "drawing label: ", self.button_name
			self.color = UI_label_color																	# since self.color = buttonColor by default, this overwrites that for labels
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			#pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))







# ************************************************************************************************************************
# ************************************************************************************************************************
# 	MAIN code	#
# ************************************************************************************************************************
# ************************************************************************************************************************

####### INITIALIZE DISPLAY ##########
## If this is in the main loop, FPS goes way down, only refresh what's needed ##

# # Pygame display
print "initializing pygame display"
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption('My Program Name')


# # #  draw background
print "drawing background"
screen.fill(background_color)

# # draw borders & frames for interface
print "drawing borders and frames"
pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))

# # draw buttons!
print "____drawing buttons in initialization"
defineButtons()
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
			print "mouseX = ", mouseX, "mouseY = ", mouseY			# this if.even MOUSEBUTTONDOWN **MUST** be under the for event in pygame.event.get() to run only once
			selected_button = findButton(my_buttons, mouseX, mouseY)
			print "selected button = ", selected_button

			if selected_button.button_label_txt == "EXIT":
				print "you pressed exit"
				running = False

			if selected_button != None:

				if selected_button.buttonType == "pushy":
					print "running MOUSEBUTTONDOWN pushy event"
					print "selected_button.color  was :", selected_button.color	
					selected_button.color = UI_button_click_color
					print "selected_button.color now : ", selected_button.color			
					selected_button.buttonEnabled = True
					print "clicked button is a pushy temporary button"
					

					if selected_button.button_name == "command01":
						print "you clicked command01"
						button01[7] = True
						button01[8] = UI_button_click_color
						defineButtons()

						print "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()


				if selected_button.buttonType == "sticky":
					print "running sticky event"
					updateButton(selected_button.button_name)
				

		if event.type == pygame.MOUSEBUTTONUP:

			if selected_button != None:
				
				if selected_button.buttonType == "pushy":
					print "running MOUSEBUTTONUP pushy event"
					print "selected_button.color  was :", selected_button.color	
					selected_button.color = UI_button_color 			#reverts button back to normal color after letting go of mouse
					print "selected_button.color now : ", selected_button.color	
			
					if selected_button.button_name == "command01":
						print "you clicked command01"
						button01[7] = False
						button01[8] = UI_button_color
						defineButtons()

						print "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()


					if selected_button.button_name == "command01":
						print "running code for Command01"


			selected_button = None
			print "selected_button = ", selected_button

			
			# # re draw buttons!
			# # without this here, pushy buttons don't return to normal on mouseup
			print "____drawing buttons in MOUSEBUTTONUP call"
			for i, button in enumerate(my_buttons):
				button.display()		
			
			

	# always do this last
	pygame.display.flip()