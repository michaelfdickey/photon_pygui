#

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

# ************************************************************************************


# ************************************************************************************
#	initial lists	#

my_uiObjects = []							# this list will hold all the UI elements
# ************************************************************************************



# ************************************************************************************
#	functions	#

def finduiObject(objects,x,y):
	for o in objects.objects:
		if x >= xmin:
			if x <= xmax:
				print "clicked"
				return o
	return None

# ************************************************************************************


# ************************************************************************************
#	classes		#

class uiObjects:
	def __init__ (self, (x,y), width, height):
		self.xmin = x
		self.xmax = x + width
		self.ymin = y
		self.ymax = y + height
		self.color = (0,0,255)
		self.thickness = 0

# ************************************************************************************


# ************************************************************************************
# 	MAIN code	#


# Pygame display
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption('My Program Name')

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# DRAW SCREEN

	# py grame will draw the elements from start to finish based on the order below, background first
	# then foreground elements. Each one will draw over the one before it. if you draw the background last
	# the whole screen is overwritten

	# # draw background
	screen.fill(background_color)

	# # draw reference or background lines, like grids here



	# # draw borders & frames for interface
	
	# # # top bar of interface
	UI_topBar_height = 40			# menu bar along the top of the screen
	pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))

	# # # side bar of itetrface
	UI_sideBar_width = 120		# menu bar along the side of the screen
	pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))



	# # draw buttons

	
	# # # exit button
	# # # # button variables
	exit_button_origin_x = 0
	exit_button_origin_y = pygame_window_height - 40
	exit_button_width = UI_sideBar_width
	exit_button_height = 20
	# # # # button body
	pygame.draw.rect(screen, UI_button_color, (exit_button_origin_x, exit_button_origin_y, exit_button_width, exit_button_height)) #button
	pygame.draw.rect(screen, UI_button_border_color, (0,(pygame_window_height - 40), UI_sideBar_width, 20), 2) #border
	# # # # button text/label
	exit_label_txt = " EXIT"
	exit_label = myfont.render(str(exit_label_txt), 0, (255,255,0))
	# # # # draw button
	screen.blit(exit_label, (10, (pygame_window_height-40)))

	# # # # create object using the uiObjects class then add it to the my_uiObjects list
	newObject = uiObjects((exit_button_origin_x, exit_button_origin_y), exit_button_width, exit_button_height)
	my_uiObjects.append(newObject)


	# # # debug button
	# # # # button variables
	debug_button_origin_x = 0
	debug_button_origin_y = pygame_window_height - 20
	debug_button_width = UI_sideBar_width
	debug_button_height = 20
	# # # # button body
	pygame.draw.rect(screen, UI_button_color, (debug_button_origin_x, debug_button_origin_y, debug_button_width, debug_button_height)) #button
	pygame.draw.rect(screen, UI_button_border_color, (0,(pygame_window_height - 20), UI_sideBar_width, 20), 2) #border
	# # # # button text/label
	debug_label_txt = " debug"
	debug_label = myfont.render(str(debug_label_txt), 0, (255,255,0))
	# # # # draw button
	screen.blit(debug_label, (10, (pygame_window_height-20)))

	# # # # create object using the uiObjects class then add it to the my_uiObjects list
	newObject = uiObjects((debug_button_origin_x, debug_button_origin_y), debug_button_width, debug_button_height)
	my_uiObjects.append(newObject)





	pygame.display.flip()		 # updates and draws the screen & launch pygame window

#
