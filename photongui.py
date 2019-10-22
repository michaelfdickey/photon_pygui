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
#		- pushy is a temporary button active only while it is being clicked on, typically to invoke a command
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


def matchButton(selected_button):					# for sticky buttons to find and update buttonEnabled =

	### --- check sticky01 button, enable / disable when clicked --- ###

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

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
			my_buttons.append(created_button)
			### -------------------------- ###	

			for i, button in enumerate(my_buttons):
				button.display()
			
			return


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

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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

					
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
		
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
		
			# define button then add button to display list
			created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
	def __init__ (self, (x,y), button_name, x_width, y_height, button_label_txt, buttonType, buttonEnabled, buttonColor):
		self.button_name = button_name
		self.x = x
		self.x_width = x_width
		self.y = y
		self.y_height = y_height
		self.color = buttonColor
		self.thickness = 0
		self.button_label_txt = button_label_txt
		self.colorBorder = UI_button_border_color
		self.buttonType = buttonType  #pushy, sticky, checky, label (label is just text, not a button)
		self.buttonEnabled = buttonEnabled

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


# ************************************************************************************


# ************************************************************************************
# 	define buttons

number_of_buttons = 20
my_buttons = []

for n in range(1):

	### these are all the buttons, the my_buttons.append(created_button) iterates through displaying them and
	### a seperate dictionary is created for each button

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
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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

	# define button then add button to display list
	created_button = Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled, buttonColor)
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
					# match the clicked button with it's dictionary
					matchButton(selected_button.button_name)

				if selected_button.buttonType == "pushy":
					selected_button.color = UI_button_click_color
					print "clicked button is a pushy temporary button"

				if selected_button.buttonType == "label":
					selected_button.color = UI_label_color
					print "clicked button is a label, not a button"

		if event.type == pygame.MOUSEBUTTONUP:
			if selected_button != None:
				selected_button.color = UI_button_color #reverts button back to normal color after letting go of mouse
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


