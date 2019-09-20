#

# ************************************************************************************
# 	import modules	#

import pygame
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


# Screen size
pygame_window_width = 1200
pygame_window_height = 1200


# interface colors
background_color = (0,0,0)
UI_background_color = (102, 0, 51)
UI_button_border_color = (153, 0, 76)
UI_button_color = (204, 0, 102)
UI_button_click_color = (255, 0, 127)

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
	exit_button_origin_y = pygame_window_height - 20
	exit_button_width = UI_sideBar_width
	exit_button_height = 20
	# # # # button body
	pygame.draw.rect(screen, UI_button_color, (exit_button_origin_x, exit_button_origin_y, exit_button_width, exit_button_height)) #button
	pygame.draw.rect(screen, UI_button_border_color, (0,(pygame_window_height - 20), UI_sideBar_width, 20), 2) #border
	# # # # button text/label
	exit_label_txt = " EXIT"
	exit_label = myfont.render(str(exit_label_txt), 0, (255,255,0))
	
	screen.blit(exit_label, (10, (pygame_window_height-20)))

	# # # # create object using the uiObjects class then add it to the my_uiObjects list
	newObject = uiObjects((exit_button_origin_x, exit_button_origin_y), exit_button_width, exit_button_height)
	my_uiObjects.append(newObject)




	pygame.display.flip()		 # updates and draws the screen & launch pygame window

#
print "this ran ok"