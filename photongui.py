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






#
print "this ran ok"