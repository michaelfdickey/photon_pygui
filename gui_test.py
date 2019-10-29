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
# 	create buttons	#
# ************************************************************************************************************************
# ************************************************************************************************************************

number_of_buttons = 20
my_buttons = []

for n in range(1):


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

	pygame.display.flip()