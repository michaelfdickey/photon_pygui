# ************************************************************************************************************************
# ************************************************************************************************************************
# 	Static Element dictionary 	#
# ************************************************************************************************************************
# ************************************************************************************************************************


staticElement0 = {}
staticElement0[0] = "originHorizontal"			# elementName
staticElement0[1] = 0								# x_start
staticElement0[2] = pygame_window_width			# x_end or x_width
staticElement0[3] = pygame_window_height / 2		# y_start
staticElement0[4] = pygame_window_height / 2		# y_end or y_width
staticElement0[5] = 1								# thickness or...
staticElement0[6] = red							# color
staticElement0[7] = "line"						# elementType (line, box, circle, etc)
staticElement0[8] = "origin"						# elementGroup
staticElement0[9] = True							# elementVisible

staticElement1 = {}
staticElement1[0] = "originVertical"				# elementName
staticElement1[1] = pygame_window_width / 2		# x_start
staticElement1[2] = pygame_window_width / 2		# x_end or x_width
staticElement1[3] = 0								# y_start
staticElement1[4] = pygame_window_height			# y_end or y_width
staticElement1[5] = 1								# thickness or...
staticElement1[6] = red							# color
staticElement1[7] = "line"						# elementType (line, box, circle, etc)
staticElement1[8] = "origin"						# elementGroup
staticElement1[9] = True							# elementVisible

allStaticElements = {}
allStaticElements[0] = staticElement0				# origin X axis
allStaticElements[1] = staticElement1				# origin Y axis


# # #########################################################################################
# # # DEFINE STATIC ELEMENTS
# # #########################################################################################

my_staticElements = []			#initializes my_staticElements list, each element is added to this for display
elementToDraw = {}			#each element is loaded into this dictionary, added to my_elements list

def defineStaticElements():
	# source info for this part: https://realpython.com/iterate-through-dictionary-python/
	print "defineStaticElements() - started"
	# iterates through the nested element dictionary, dumps each element into elementToDraw, then displays ads to the list
	for allStaticElementsID, allStaticElementsValue in allStaticElements.items():
		for key in allStaticElementsValue:
			elementToDraw[key] = allStaticElementsValue[key]

		### -------------------------- ###
		element_name = elementToDraw[0]
		element_x_start = elementToDraw[1]
		element_x_end = elementToDraw[2]
		element_y_start = elementToDraw[3]
		element_y_end = elementToDraw[4]
		element_thickness = elementToDraw[5]
		elementColor= elementToDraw[6]
		elementType = elementToDraw[7]
		elementGroup = elementToDraw[8]
		elementVisible = elementToDraw[9]

		# define element then add element to display list
		created_element = StaticElements((element_x_start,element_y_start), element_name, element_x_end, element_y_end, element_thickness, elementColor, elementType, elementGroup, elementVisible)
		my_staticElements.append(created_element)


	print "defineStaticElements() - completed"

# # #########################################################################################
# # # DISPLAY STATIC ELEMENTS
# # #########################################################################################

class StaticElements:
	def __init__ (self, (element_x_start,element_y_start), element_x_end, element_y_end, element_name, element_thickness, elementColor, elementType, elementGroup, elementVisible):
		self.element_x_start = element_x_start
		self.element_y_start = element_y_start
		self.element_x_end = element_x_end
		self.element_y_end = element_y_end
		self.element_name = element_name
		self.element_thickness = element_thickness
		self.elementColor = elementColor
		self.elementType = elementType
		self.elementGroup = elementGroup
		self.elementVisible = elementVisible

	def display(self):
		print "drawing static element line"
		print "self.element_x_start = ", self.element_x_start
		if self.elementType == "line":
			pygame.draw.lines(screen, self.elementColor, True, [(self.element_x_start,self.element_y_start), (self.element_x_end,self.element_y_end)], self.element_thickness)
