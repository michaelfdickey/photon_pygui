#************************************************************************************
#  	dev notes
#	09-27-2019 - currently incorporating menu_physics_garage_005b.py


# ************************************************************************************
# 	import modules	#

import pygame
import random
import math
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


selected_uiObject = None					# by default, no UI objects are selected at start
selected_button = None

# ************************************************************************************


# ************************************************************************************
#	initial lists	#

my_uiObjects = []							# this list will hold all the UI elements
# ************************************************************************************



# ************************************************************************************
#	functions	#

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
						print "selected button label_txt = ", b.label_txt
						return b
	return None


# ************************************************************************************


# ************************************************************************************
#	classes		#

class Button:
	def __init__ (self, (x,y), x_width, y_height, label_txt, buttonType):
		self.x = x
		self.x_width = x_width
		self.y = y
		self.y_height = y_height
		self.color = UI_button_color
		self.thickness = 0
		self.label_txt = label_txt
		self.colorBorder = UI_button_border_color
		self.buttonType = buttonType  #pushy, sticky, checky, label (label is just text, not a button)

	def display(self):
		#pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size, self.thickness)
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
		pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

		exit_label = myfont.render(str(label_txt), 0, UI_button_txt_color)
		screen.blit(exit_label, (10, (pygame_window_height-20)))

# ************************************************************************************


# ************************************************************************************
# 	define buttons

number_of_buttons = 20
my_buttons = []

for n in range(1):

	# create exit button
	button_exit_origin_x = 0
	button_exit_origin_y = pygame_window_height - 20
	button_exit_width = UI_sideBar_width
	button_exit_height = 20
	label_txt = "EXIT"
	buttonType = "sticky"
	# define button
	created_button = Button((button_exit_origin_x,button_exit_origin_y), button_exit_width, button_exit_height, label_txt, buttonType)
	# add button to dictionary
	my_buttons.append(created_button)
	print "button origin x", button_exit_origin_x, "button width pos", button_exit_origin_x + button_exit_width






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


	# # draw background
	screen.fill(background_color)

	# # draw reference or background lines, like grids here

	# # draw borders & frames for interface
	pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
	pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))


	# # draw buttons!
	for i, button in enumerate(my_buttons):
		button.display()


	# pygame event monitoring
	# pygame scans for mouse and keyboard events and takes actions accordingly

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			(mouseX, mouseY) = pygame.mouse.get_pos()
			print "mouseX = ", mouseX, "mouseY = ", mouseY
			selected_button = findButton(my_buttons, mouseX, mouseY)
			print "selected button = ", selected_button

		elif event.type == pygame.MOUSEBUTTONUP:
			if selected_button != None:
				selected_button.color = UI_button_color #reverts button back to normal color after letting go of mouse
			selected_button = None

	if selected_button != None:
		(mouseX, mouseY) = pygame.mouse.get_pos()
		selected_button.color = (255,128,255)
		print selected_button.color
		pygame.display.flip()

		if selected_button.label_txt == "EXIT":
			print "you pressed exit"
			running = False


	pygame.display.flip()		 # updates and draws the screen & launch pygame window

#
