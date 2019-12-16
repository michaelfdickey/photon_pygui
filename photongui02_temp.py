

# ************************************************************************************
#	initial variables	#
# ************************************************************************************


# ************************************************************************************
#	initial lists	#
# ************************************************************************************



# ************************************************************************************
# 	initial dictionaries 		#




button20 = {}
button20["name"] = "scale"							# button_name
button20["origin_x"] = 0								# button_origin_x
button20["origin_y"] = pgvar.pygame_window_height - 480		# button_origin_y
button20["width"] = pgvar.UI_sideBar_width					# button_width
button20["height"] = 20								# button_height
button20["label_txt"] = "Scale          |<-  --  ->|"			# button_label_txt
button20["type"] = "sticky"							# buttonType
button20["enabled"] = False							# buttonEnabled
button20["color"] = pgvar.UI_button_color					# buttonColor
button20["group"] = "scale"							# buttonGroup
button20["visible"] = True							# buttonVisible

button21 = {}
button21["name"] = "grid"								# button_name
button21["origin_x"] = 0								# button_origin_x
button21["origin_y"] = pgvar.pygame_window_height - 500		# button_origin_y
button21["width"] = pgvar.UI_sideBar_width					# button_width
button21["height"] = 20								# button_height
button21["label_txt"] = "Grid                          #"			# button_label_txt
button21["type"] = "sticky"							# buttonType
button21["enabled"] = False							# buttonEnabled
button21["color"] = pgvar.UI_button_color					# buttonColor
button21["group"] = "grid"							# buttonGroup
button21["visible"] = True							# buttonVisible

button22 = {}
button22["name"] = "origin"							# button_name
button22["origin_x"] = 0								# button_origin_x
button22["origin_y"] = pgvar.pygame_window_height - 520		# button_origin_y
button22["width"] = pgvar.UI_sideBar_width					# button_width
button22["height"] = 20								# button_height
button22["label_txt"] = "Origin                      +"			# button_label_txt
button22["type"] = "sticky"							# buttonType
button22["enabled"] = False							# buttonEnabled
button22["color"] = pgvar.UI_button_color					# buttonColor
button22["group"] = "origin"							# buttonGroup
button22["visible"] = True							# buttonVisible













button24 = {}
button24["name"] = "dropdownLabel"					# button_name
button24["origin_x"] = 0								# button_origin_x
button24["origin_y"] = pgvar.pygame_window_height - 600		# button_origin_y
button24["width"] = pgvar.UI_sideBar_width					# button_width
button24["height"] = 20								# button_height
button24["label_txt"] = "Dropdown 01"					# button_label_txt
button24["type"] = "label"							# buttonType
button24["enabled"] = False							# buttonEnabled
button24["color"] = pgvar.UI_button_color					# buttonColor
button24["group"] = "dropdown01"						# buttonGroup
button24["visible"] = True							# buttonVisible

button25 = {}
button25["name"] = "dropdown01Label"					# button_name
button25["origin_x"] = 0								# button_origin_x
button25["origin_y"] = pgvar.pygame_window_height - 580		# button_origin_y
button25["width"] = pgvar.UI_sideBar_width - 20				# button_width
button25["height"] = 20								# button_height
button25["label_txt"] = "- select -"					# button_label_txt
button25["type"] = "dropdown"							# buttonType
button25["enabled"] = False							# buttonEnabled
button25["color"] = pgvar.UI_button_color					# buttonColor
button25["group"] = "dropdown01"						# buttonGroup
button25["visible"] = True							# buttonVisible

button26 = {}
button26["name"] = "dropdown01opener"					# button_name
button26["origin_x"] = pgvar.UI_sideBar_width - 20			# button_origin_x
button26["origin_y"] = pgvar.pygame_window_height - 580		# button_origin_y
button26["width"] = 20								# button_width
button26["height"] = 20								# button_height
button26["label_txt"] = ">>"							# button_label_txt
button26["type"] = "dropdown"							# buttonType
button26["enabled"] = False							# buttonEnabled
button26["color"] = pgvar.UI_button_color					# buttonColor
button26["group"] = "dropdown01"						# buttonGroup
button26["visible"] = True							# buttonVisible

button27 = {}
button27["name"] = "dropdown01option01"				# button_name
button27["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button27["origin_y"] = pgvar.pygame_window_height - 580		# button_origin_y
button27["width"] = 140								# button_width
button27["height"] = 20								# button_height
button27["label_txt"] = " Option 1"					# button_label_txt
button27["type"] = "dropdown"							# buttonType
button27["enabled"] = False							# buttonEnabled
button27["color"] = pgvar.UI_button_color					# buttonColor
button27["group"] = "dropdown01"						# buttonGroup
button27["visible"] = False							# buttonVisible

button28 = {}
button28["name"] = "dropdown01option02"				# button_name
button28["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button28["origin_y"] = pgvar.pygame_window_height - 560		# button_origin_y
button28["width"] = 140								# button_width
button28["height"] = 20								# button_height
button28["label_txt"] = " Option 2"					# button_label_txt
button28["type"] = "dropdown"							# buttonType
button28["enabled"] = False							# buttonEnabled
button28["color"] = pgvar.UI_button_color					# buttonColor
button28["group"] = "dropdown01"						# buttonGroup
button28["visible"] = False							# buttonVisible

button29 = {}
button29["name"] = "dropdown01option03"				# button_name
button29["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button29["origin_y"] = pgvar.pygame_window_height - 540		# button_origin_y
button29["width"] = 140								# button_width
button29["height"] = 20								# button_height
button29["label_txt"] = " Option 3"					# button_label_txt
button29["type"] = "dropdown"							# buttonType
button29["enabled"] = False							# buttonEnabled
button29["color"] = pgvar.UI_button_color					# buttonColor
button29["group"] = "dropdown01"						# buttonGroup
button29["visible"] = False							# buttonVisible

button30 = {}
button30["name"] = "menu01"							# button_name
button30["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button30["origin_y"] = 0								# button_origin_y
button30["width"] = 125								# button_width
button30["height"] = 20								# button_height
button30["label_txt"] = " Menu 01 Sticky"				# button_label_txt
button30["type"] = "menu"								# buttonType
button30["enabled"] = False							# buttonEnabled
button30["color"] = pgvar.UI_button_color					# buttonColor
button30["group"] = "menu01"							# buttonGroup
button30["visible"] = True							# buttonVisible

button31 = {}
button31["name"] = "menu01option01"					# button_name
button31["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button31["origin_y"] = 20								# button_origin_y
button31["width"] = 150								# button_width
button31["height"] = 20								# button_height
button31["label_txt"] = " Monday "						# button_label_txt
button31["type"] = "menu"								# buttonType
button31["enabled"] = False							# buttonEnabled
button31["color"] = pgvar.UI_button_color					# buttonColor
button31["group"] = "menu01"							# buttonGroup
button31["visible"] = False							# buttonVisible

button32 = {}
button32["name"] = "menu01option02"					# button_name
button32["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button32["origin_y"] = 40								# button_origin_y
button32["width"] = 150								# button_width
button32["height"] = 20								# button_height
button32["label_txt"] = " Tuesday "					# button_label_txt
button32["type"] = "menu"								# buttonType
button32["enabled"] = False							# buttonEnabled
button32["color"] = pgvar.UI_button_color					# buttonColor
button32["group"] = "menu01"							# buttonGroup
button32["visible"] = False							# buttonVisible

button33 = {}
button33["name"] = "menu01option03"					# button_name
button33["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button33["origin_y"] = 60								# button_origin_y
button33["width"] = 150								# button_width
button33["height"] = 20								# button_height
button33["label_txt"] = " Wednesday "					# button_label_txt
button33["type"] = "menu"								# buttonType
button33["enabled"] = False							# buttonEnabled
button33["color"] = pgvar.UI_button_color					# buttonColor
button33["group"] = "menu01"							# buttonGroup
button33["visible"] = False							# buttonVisible

button34 = {}
button34["name"] = "menu01option04"					# button_name
button34["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button34["origin_y"] = 80								# button_origin_y
button34["width"] = 150								# button_width
button34["height"] = 20								# button_height
button34["label_txt"] = " Thursday "					# button_label_txt
button34["type"] = "menu"								# buttonType
button34["enabled"] = False 							# buttonEnabled
button34["color"] = pgvar.UI_button_color					# buttonColor
button34["group"] = "menu01"							# buttonGroup
button34["visible"] = False							# buttonVisible

button35 = {}
button35["name"] = "menu01option05"					# button_name
button35["origin_x"] = pgvar.UI_sideBar_width				# button_origin_x
button35["origin_y"] = 100							# button_origin_y
button35["width"] = 150								# button_width
button35["height"] = 20								# button_height
button35["label_txt"] = " Friday "						# button_label_txt
button35["type"] = "menu"								# buttonType
button35["enabled"] = False							# buttonEnabled
button35["color"] = pgvar.UI_button_color					# buttonColor
button35["group"] = "menu01"							# buttonGroup
button35["visible"] = False							# buttonVisible

button36 = {}
button36["name"] = "menu02"										# button_name
button36["origin_x"] = pgvar.UI_sideBar_width + UI_menuButton_width		# button_origin_x
button36["origin_y"] = 0											# button_origin_y
button36["width"] = 125											# button_width
button36["height"] = 20											# button_height
button36["label_txt"] = " Menu 02"									# button_label_txt
button36["type"] = "menu"											# buttonType
button36["enabled"] = False										# buttonEnabled
button36["color"] = pgvar.UI_button_color								# buttonColor
button36["group"] = "menu02"										# buttonGroup
button36["visible"] = True										# buttonVisible

button37 = {}
button37["name"] = "menu03"							# button_name
button37["origin_x"] = pgvar.UI_sideBar_width * 250			# button_origin_x
button37["origin_y"] = 0								# button_origin_y
button37["width"] = 125								# button_width
button37["height"] = 20								# button_height
button37["label_txt"] = " Menu 03 Popup"				# button_label_txt
button37["type"] = "menu"								# buttonType
button37["enabled"] = False							# buttonEnabled
button37["color"] = pgvar.UI_button_color					# buttonColor
button37["group"] = "menu03"							# buttonGroup
button37["visible"] = False							# buttonVisible

button38 = {}
button38["name"] = "textField01Label"					# button_name
button38["origin_x"] = 0								# button_origin_x
button38["origin_y"] = pgvar.pygame_window_height - 660		# button_origin_y
button38["width"] = pgvar.UI_sideBar_width					# button_width
button38["height"] = 20								# button_height
button38["label_txt"] = "Enter Text:"					# button_label_txt
button38["type"] = "label"							# buttonType
button38["enabled"] = False							# buttonEnabled
button38["color"] = pgvar.UI_label_color					# buttonColor
button38["group"] = "text01"							# buttonGroup
button38["visible"] = True							# buttonVisible

button39 = {}
button39["name"] = "textField01"						# button_name
button39["origin_x"] = 0								# button_origin_x
button39["origin_y"] = pgvar.pygame_window_height - 640		# button_origin_y
button39["width"] = pgvar.UI_sideBar_width					# button_width
button39["height"] = 20								# button_height
button39["label_txt"] = "abc123"						# button_label_txt
button39["type"] = "textEntry"						# buttonType
button39["enabled"] = False							# buttonEnabled
button39["color"] = UI_text_entry_box_color			# buttonColor
button39["group"] = "text01"							# buttonGroup
button39["visible"] = True							# buttonVisible


button40 = {}
button40["name"] = "menu02popup01"							# button_name
button40["origin_x"] = pgvar.UI_sideBar_width + UI_menuButton_width	# button_origin_x
button40["origin_y"] = 20										# button_origin_y
button40["width"] = 150										# button_width
button40["height"] = 20										# button_height
button40["label_txt"] = " Small Popup"							# button_label_txt
button40["type"] = "menu"										# buttonType
button40["enabled"] = False									# buttonEnabled
button40["color"] = pgvar.UI_button_color							# buttonColor
button40["group"] = "menu02"									# buttonGroup
button40["visible"] = False									# buttonVisible


button41 = {}
button41["name"] = "menu02popup02"							# button_name
button41["origin_x"] = pgvar.UI_sideBar_width + UI_menuButton_width	# button_origin_x
button41["origin_y"] = 40										# button_origin_y
button41["width"] = 150										# button_width
button41["height"] = 20										# button_height
button41["label_txt"] = " Medium Popup"						# button_label_txt
button41["type"] = "menu"										# buttonType
button41["enabled"] = False									# buttonEnabled
button41["color"] = pgvar.UI_button_color							# buttonColor
button41["group"] = "menu02"									# buttonGroup
button41["visible"] = False									# buttonVisible

button42 = {}
button42["name"] = "menu02popup03"							# button_name
button42["origin_x"] = pgvar.UI_sideBar_width + UI_menuButton_width	# button_origin_x
button42["origin_y"] = 60										# button_origin_y
button42["width"] = 150										# button_width
button42["height"] = 20										# button_height
button42["label_txt"] = " Large Popup"							# button_label_txt
button42["type"] = "menu"										# buttonType
button42["enabled"] = False									# buttonEnabled
button42["color"] = pgvar.UI_button_color							# buttonColor
button42["group"] = "menu02"									# buttonGroup
button42["visible"] = False									# buttonVisible

button43 = {}
button43["name"] = "menu02popup01element01"					# button_name
button43["origin_x"] = UI_popup_small_origin_x				# button_origin_x
button43["origin_y"] = UI_popup_small_origin_y				# button_origin_y
button43["width"] = UI_popup_small_width						# button_width
button43["height"] = UI_popup_small_height					# button_height
button43["label_txt"] = " Small Popup"							# button_label_txt
button43["type"] = "popup"									# buttonType
button43["enabled"] = False									# buttonEnabled
button43["color"] = UI_background_color						# buttonColor
button43["group"] = "menu02popup01"							# buttonGroup
button43["visible"] = False									# buttonVisible

button44 = {}
button44["name"] = "menu02popup01element02"					# button_name
button44["origin_x"] = UI_popup_small_origin_x				# button_origin_x
button44["origin_y"] = UI_popup_small_origin_y				# button_origin_y
button44["width"] = UI_popup_small_width						# button_width
button44["height"] = 20										# button_height
button44["label_txt"] = " Menu 02 >> Small Popup"				# button_label_txt
button44["type"] = "popup"									# buttonType
button44["enabled"] = False									# buttonEnabled
button44["color"] = pgvar.UI_button_selected_color					# buttonColor
button44["group"] = "menu02popup01"							# buttonGroup
button44["visible"] = False									# buttonVisible

button45 = {}
button45["name"] = "menu02popup01element03"					# button_name
button45["origin_x"] = UI_popup_small_origin_x				# button_origin_x
button45["origin_y"] = UI_popup_small_origin_y + 40			# button_origin_y
button45["width"] = UI_popup_small_width						# button_width
button45["height"] = 20										# button_height
button45["label_txt"] = " Do Something Interesting:"			# button_label_txt
button45["type"] = "popup_element"							# buttonType
button45["enabled"] = False									# buttonEnabled
button45["color"] = pgvar.UI_label_color							# buttonColor
button45["group"] = "menu02popup01"							# buttonGroup
button45["visible"] = False									# buttonVisible

button46 = {}
button46["name"] = "menu02popup01element04"					# button_name
button46["origin_x"] = UI_popup_small_origin_x + 20			# button_origin_x
button46["origin_y"] = UI_popup_small_origin_y + 80			# button_origin_y
button46["width"] = 80										# button_width
button46["height"] = 20										# button_height
button46["label_txt"] = "Something"							# button_label_txt
button46["type"] = "popup_element_button"						# buttonType
button46["enabled"] = False									# buttonEnabled
button46["color"] = pgvar.UI_button_color							# buttonColor
button46["group"] = "menu02popup01"							# buttonGroup
button46["visible"] = False									# buttonVisible

button47 = {}
button47["name"] = "menu02popup01element05"					# button_name
button47["origin_x"] = UI_popup_small_origin_x + 20			# button_origin_x
button47["origin_y"] = UI_popup_small_origin_y + 100			# button_origin_y
button47["width"] = 80										# button_width
button47["height"] = 20										# button_height
button47["label_txt"] = "Interesting"							# button_label_txt
button47["type"] = "popup_element_button"						# buttonType
button47["enabled"] = False									# buttonEnabled
button47["color"] = pgvar.UI_button_color							# buttonColor
button47["group"] = "menu02popup01"							# buttonGroup
button47["visible"] = False									# buttonVisible

button48 = {}
button48["name"] = "menu02popup01element06"								# button_name
button48["origin_x"] = UI_popup_small_origin_x							# button_origin_x
button48["origin_y"] = UI_popup_small_origin_y + UI_popup_small_height - 60 	# button_origin_y
button48["width"] = UI_popup_small_width									# button_width
button48["height"] = 60													# button_height
button48["label_txt"] = ""												# button_label_txt
button48["type"] = "popup_element"										# buttonType
button48["enabled"] = False												# buttonEnabled
button48["color"] = pgvar.UI_label_color										# buttonColor
button48["group"] = "menu02popup01"										# buttonGroup
button48["visible"] = False												# buttonVisible

button49 = {}
button49["name"] = "menu02popup01element07"								# button_name
button49["origin_x"] = UI_popup_small_origin_x + 20						# button_origin_x
button49["origin_y"] = UI_popup_small_origin_y + UI_popup_small_height - 40 	# button_origin_y
button49["width"] = 60													# button_width
button49["height"] = 20													# button_height
button49["label_txt"] = " OK "												# button_label_txt
button49["type"] = "popup_element_button"									# buttonType
button49["enabled"] = False												# buttonEnabled
button49["color"] = pgvar.UI_button_color 										# buttonColor
button49["group"] = "menu02popup01"										# buttonGroup
button49["visible"] = False												# buttonVisible

button50 = {}
button50["name"] = "menu02popup01element08"								# button_name
button50["origin_x"] = UI_popup_small_origin_x + UI_popup_small_width -80	# button_origin_x
button50["origin_y"] = UI_popup_small_origin_y + UI_popup_small_height - 40 	# button_origin_y
button50["width"] = 60													# button_width
button50["height"] = 20													# button_height
button50["label_txt"] = "Cancel"											# button_label_txt
button50["type"] = "popup_element_button"									# buttonType
button50["enabled"] = False												# buttonEnabled
button50["color"] = pgvar.UI_button_color 										# buttonColor
button50["group"] = "menu02popup01"										# buttonGroup
button50["visible"] = False												# buttonVisible








allButtons[12] = labelGroup02		# group02 label
allButtons[13] = bGroup02Button01 	# group02 button 01
allButtons[14] = bGroup02Button02		# group02 button 02
allButtons[15] = labelGroup03		# group03 label
allButtons[16] = bGroup03Button01 	# group03 button 01
allButtons[17] = bGroup03Button02		# group03 button 02
allButtons[18] = bGroup03Button03		# group03 button 03
allButtons[19] = buttonFPS		# FPS display
allButtons[20] = button20 	# display scale
allButtons[21] = button21 	# display grid
allButtons[22] = button22 	# display origin
allButtons[23] = button23		# display options label
allButtons[24] = button24 	# Dropdown01 - Label
allButtons[25] = button25		# Dropdown01 - selected display
allButtons[26] = button26		# Dropdown01 - opener
allButtons[27] = button27		# Dropdown01 - option1
allButtons[28] = button28		# Dropdown01 - option2
allButtons[29] = button29		# Dropdown01 - option3
allButtons[30] = button30		# Menu 01
allButtons[31] = button31		# Menu 01 - option 01 - Monday
allButtons[32] = button32		# Menu 01 - option 02 - Tuesday
allButtons[33] = button33		# Menu 01 - option 03 - Wednesday
allButtons[34] = button34		# Menu 01 - option 04 - Thursday
allButtons[35] = button35		# Menu 01 - option 05 - Friday
allButtons[36] = button36		# Menu 02
allButtons[37] = button37		# Menu 03
allButtons[38] = button38		# Text Field - label
allButtons[39] = button39		# Text Field - text entry box
allButtons[40] = button40		# Menu 02  - small popup
allButtons[41] = button41		# Menu 02  - Medium popup
allButtons[42] = button42		# Menu 02  - Large popup
allButtons[43] = button43		# Menu 02  - small popup - element 01 - background box
allButtons[44] = button44		# Menu 02  - small popup - element 02 - title bar
allButtons[45] = button45		# Menu 02  - small popup - element 03 - option description
allButtons[46] = button46		# Menu 02  - small popup - element 04 - something button
allButtons[47] = button47		# Menu 02  - small popup - element 05 - interesting button
allButtons[48] = button48		# Menu 02  - small popup - element 06 - ok / cancel background
allButtons[49] = button49		# Menu 02  - small popup - element 06 - ok button
allButtons[50] = button50		# Menu 02  - small popup - element 06 - cancel button



# ************************************************************************************************************************
# ************************************************************************************************************************
# 	functions  
# ************************************************************************************************************************
# ************************************************************************************************************************


my_buttons = []			#initializes my_buttons list, each button is added to this for display
buttonToDraw = {}			#each button is loaded into this dictionary, added to my_buttons list




# # #########################################################################################
# # # DEFINE BUTTONS
# # #########################################################################################



def enumerateButtons():
	for i, button in enumerate(my_buttons):
		button.display()	


"""
# # #########################################################################################
# # This figures out which button was clicked
def findButton(buttons, x, y):
	for b in buttons:
		if x <= b.x + b.x_width:
			if x >= b.x:
				if y >= b.y:
					if y <= b.y + b.y_height:
						print lineNum(), "selected button label_txt = ", b.button_name
						return b
	return None
"""



# # #########################################################################################
# # this updates pushy buttons
def updatePushyButtons(selected_button):
	print lineNum(), "updating pushy buttons"

"""
	MOVE PUSHY BUTTON PROCESSING HERE
"""



############################################################################################
# # UPDATE STICKY BUTTONS
# # this updates sticky buttons  based on actions taken
############################################################################################

buttonToCheck = {}

"""
def updateStickyButtons(selected_button):
	print lineNum(), "updateStickyButtons() - started"
	print lineNum(), "selected_button = ", selected_button
"""
	"""
	# for sticky buttons, iterate through nested allButtons dictionary and flip buttonEnabled
	for allButtonsID, allButtonsValue in allButtons.items():
		for key in allButtonsValue:
			#print lineNum(), "key", key
			#buttonToCheck[key] = allButtonsValue[key]
			#print lineNum(), "buttonToCheck", key, allButtonsValue[key]
			if allButtonsValue[key] == "sticky":
				print lineNum(), "found a sticky button"
				print lineNum(), "key, ", key, "value", allButtonsValue[key]
				#print lineNum(), "buttonToCheck", key, allButtonsValue[key]
	"""
"""	
	if selected_button == "sticky01":
		if buttonSticky01["enabled"] == False:
			print lineNum(), "sticky01 button found"
			buttonSticky01["enabled"] = True
			buttonSticky01["color"] = pgvar.UI_button_selected_color
			print lineNum(), "flipped sticky01 from false to true"
			defineButtons()	
			
		elif buttonSticky01["enabled"] == True:
			print lineNum(), "sticky01 button found"
			buttonSticky01["enabled"] = False
			buttonSticky01["color"] = pgvar.UI_button_color
			print lineNum(), "flipped stick01 from true to false"
			defineButtons()
"""

"""
	if selected_button == "sticky02":
		if buttonSticky02["enabled"] == False:
			print lineNum(), "sticky02 button found"
			buttonSticky02["enabled"] = True
			buttonSticky02["color"] = pgvar.UI_button_selected_color
			print lineNum(), "flipped sticky02 from false to true"
			defineButtons()	
			
		elif buttonSticky02["enabled"] == True:
			print lineNum(), "sticky02 button found"
			buttonSticky02["enabled"] = False
			buttonSticky02["color"] = pgvar.UI_button_color
			print lineNum(), "flipped sticky02 from true to false"
			defineButtons()
"""
"""
	if selected_button == "sticky03":
		if buttonSticky03["enabled"] == False:
			print lineNum(), "sticky03 button found"
			buttonSticky03["enabled"] = True
			buttonSticky03["color"] = pgvar.UI_button_selected_color
			print lineNum(), "flipped sticky03 from false to true"
			defineButtons()	
			
		elif buttonSticky03["enabled"] == True:
			print lineNum(), "sticky03 button found"
			buttonSticky03["enabled"] = False
			buttonSticky03["color"] = pgvar.UI_button_color
			print lineNum(), "flipped sticky03 from true to false"
			defineButtons()			
"""

"""
	# # # FPS BUTTON
	if selected_button == "fps":
		if buttonFPS["enabled"] == False:
			buttonFPS["enabled"] = True
			buttonFPS["color"] = pgvar.UI_button_selected_color
			defineButtons()	
			
		elif buttonFPS["enabled"] == True:
			buttonFPS["enabled"] = False
			buttonFPS["color"] = pgvar.UI_button_color
			redrawEverything()
"""


	# # # ORIGIN BUTTON
	if selected_button == "origin":
		if button22["enabled"] == False:
			button22["enabled"] = True
			button22["color"] = pgvar.UI_button_selected_color
			defineButtons()	
			redrawEverything()
			
		elif button22["enabled"] == True:
			button22["enabled"] = False
			button22["color"] = pgvar.UI_button_color
			defineButtons()
			redrawEverything()


	# # # GRID BUTTON
	if selected_button == "grid":
		if button21["enabled"] == False:
			button21["enabled"] = True
			button21["color"] = pgvar.UI_button_selected_color
			defineButtons()	
			redrawEverything()
			
		elif button21["enabled"] == True:
			button21["enabled"] = False
			button21["color"] = pgvar.UI_button_color
			defineButtons()
			redrawEverything()


	print lineNum(), "updateStickyButtons() - completed"
	return
	



## ############################################################################################
## UPDATE GROUP BUTTONS
## ############################################################################################

"""
def updateGroupButtons(selected_button):
	print lineNum(), "running update group buttons"

	# # Group 01 processing
	if selected_button == "Group01Button01":
		
		if bGroup01Button01["enabled"] == True:
			bGroup01Button01["enabled"] = False
			bGroup01Button01["color"] = pgvar.UI_button_color
			bGroup01Button02["enabled"] = True
			bGroup01Button02["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
		
		elif bGroup01Button01["enabled"] == False:
			bGroup01Button01["enabled"] = True
			bGroup01Button01["color"] = pgvar.UI_button_selected_color
			bGroup01Button02["enabled"] = False
			bGroup01Button02["color"] = pgvar.UI_button_color
			pfunc.defineButtons()	

	if selected_button == "Group01Button02":
		
		if bGroup01Button02["enabled"] == True:
			bGroup01Button02["enabled"] = False
			bGroup01Button02["color"] = pgvar.UI_button_color
			bGroup01Button01["enabled"] = True
			bGroup01Button01["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()	
		
		elif bGroup01Button02["enabled"] == False:
			bGroup01Button02["enabled"] = True
			bGroup01Button02["color"] = pgvar.UI_button_selected_color
			bGroup01Button01["enabled"] = False
			bGroup01Button01["color"] = pgvar.UI_button_color
			pfunc.defineButtons()
"""

"""
	# # Group 02 processing
	if selected_button == "Group02Button01":
		
		if bGroup02Button01["enabled"] == True:
			bGroup02Button01["enabled"] = False
			bGroup02Button01["color"] = pgvar.UI_button_color
			bGroup02Button02["enabled"] = True
			bGroup02Button02["color"] = pgvar.UI_button_selected_color
			defineButtons()	
		
		elif bGroup02Button01["enabled"] == False:
			bGroup02Button01["enabled"] = True
			bGroup02Button01["color"] = pgvar.UI_button_selected_color
			bGroup02Button02["enabled"] = False
			bGroup02Button02["color"] = pgvar.UI_button_color
			defineButtons()	

	if selected_button == "Group02Button02":
		
		if bGroup02Button02["enabled"] == True:
			bGroup02Button02["enabled"] = False
			bGroup02Button02["color"] = pgvar.UI_button_color
			bGroup02Button01["enabled"] = True
			bGroup02Button01["color"] = pgvar.UI_button_selected_color
			defineButtons()	
		
		elif bGroup02Button02["enabled"] == False:
			bGroup02Button02["enabled"] = True
			bGroup02Button02["color"] = pgvar.UI_button_selected_color
			bGroup02Button01["enabled"] = False
			bGroup02Button01["color"] = pgvar.UI_button_color
			defineButtons()
"""

"""
	# # Group 03 processing
	if selected_button == "Group03Button01":
		
		if bGroup03Button01["enabled"] == False:
			bGroup03Button01["enabled"] = True
			bGroup03Button01["color"] = pgvar.UI_button_selected_color
			
			bGroup03Button02["enabled"] = False
			bGroup03Button02["color"] = pgvar.UI_button_color
			
			bGroup03Button03["enabled"] = False
			bGroup03Button03["color"] = pgvar.UI_button_color

			pfunc.defineButtons()	

	if selected_button == "Group03Button02":
		
		if bGroup03Button02["enabled"] == False:
			bGroup03Button02["enabled"] = True
			bGroup03Button02["color"] = pgvar.UI_button_selected_color
			
			bGroup03Button01["enabled"] = False
			bGroup03Button01["color"] = pgvar.UI_button_color
			
			bGroup03Button03["enabled"] = False
			bGroup03Button03["color"] = pgvar.UI_button_color

			pfunc.defineButtons()	

	if selected_button == "Group03Button03":
		
		if bGroup03Button03["enabled"] == False:
			bGroup03Button03["enabled"] = True
			bGroup03Button03["color"] = pgvar.UI_button_selected_color
			
			bGroup03Button01["enabled"] = False
			bGroup03Button01["color"] = pgvar.UI_button_color
			
			bGroup03Button02["enabled"] = False
			bGroup03Button02["color"] = pgvar.UI_button_color

			pfunc.defineButtons()	
"""

## ############################################################################################
## UPDATE DROPDOWN BUTTONS
## ############################################################################################

def updateDropdownButtons(selected_button):
	print lineNum(), "running update Dropdown buttons"

	if selected_button == "dropdown01opener":
		if button26["enabled"] == False:
			print lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			# update this button
			button26["enabled"] = True
			button26["color"] = pgvar.UI_button_selected_color
			button26["label_txt"] = "<<"

			# update associated buttons
			button27["visible"] = True	
			button28["visible"] = True
			button29["visible"] = True

			defineButtons()	

			print lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			print lineNum(), button26["name"], "enabled:", button26["enabled"], "visible:", button26["visible"]
			
		elif button26["enabled"] == True:
			print " --------------------------------------- "
			print lineNum(), "STARTED dropdown true to false "
			print " --------------------------------------- "

			# udapte this button
			print lineNum(), button26["name"], "enabled was: ", button26["enabled"]
			button26["enabled"] = False
			button26["color"] = pgvar.UI_button_color
			button26["label_txt"] = ">>"
			print lineNum(), button26["name"], "enabled:", button26["enabled"], "visible:", button26["visible"]

			# update associated buttons
			button27["visible"] = False
			button28["visible"] = False
			button29["visible"] = False
			print lineNum(), "buttons27,28,29 visible:", button27["visible"], button28["visible"], button29["visible"]

			screen.fill(background_color)
			defineButtons()
			redrawEverything()

			print lineNum(), button26["name"], "enabled:", button26["enabled"], "visible:", button26["visible"]
			print " --------------------------------------- "
			print lineNum(), "FINISHED dropdown true to false "
			print " --------------------------------------- "
			print type(button27["visible"])

	if selected_button == "dropdown01option01":
		if button26["enabled"] == True:
			button25["label_txt"] = "Option 01"
			button27["color"] = pgvar.UI_button_selected_color
			button28["color"] = pgvar.UI_button_color
			button29["color"] = pgvar.UI_button_color
			defineButtons()

	if selected_button == "dropdown01option02":
		if button26["enabled"] == True: 
			button25["label_txt"] = "Option 02"
			button27["color"] = pgvar.UI_button_color
			button28["color"] = pgvar.UI_button_selected_color
			button29["color"] = pgvar.UI_button_color		
			defineButtons()

	if selected_button == "dropdown01option03":
		if button26["enabled"] == True:
			button25["label_txt"] = "Option 03"
			button27["color"] = pgvar.UI_button_color
			button28["color"] = pgvar.UI_button_color
			button29["color"] = pgvar.UI_button_selected_color
			defineButtons()

	if selected_button == "dropdown01Label":
		if button25["label_txt"] != "- select -":
			if button25["enabled"] == False:
				button25["enabled"] = True
				button25["color"] = pgvar.UI_button_selected_color
				defineButtons()	
				redrawEverything()
				
			elif button25["enabled"] == True:
				button25["enabled"] = False
				button25["color"] = pgvar.UI_button_color
				defineButtons()
				redrawEverything()


## ############################################################################################
## UPDATE MENU BUTTONS
## ############################################################################################

def updateMenuButtons(selected_button):
	print lineNum(), "running updateMenuButtons"

	## START MENU 01 HANDLING

	if selected_button == "menu01":
		print lineNum(), "menu01 was clicked on"
		print lineNum(), button30["name"], "is ", button30["enabled"]
		
		if button30["enabled"] == False:
			print "was false, turning to true"
			
			button30["enabled"] = True
			button30["color"] = pgvar.UI_button_selected_color
			button31["visible"] = True
			button32["visible"] = True
			button33["visible"] = True			
			button34["visible"] = True
			button35["visible"] = True

			print lineNum(), "~", button31["name"], "Visible=", button31["visible"]
			print lineNum(), "~", button32["name"], "Visible=", button32["visible"]
			print lineNum(), "~", button33["name"], "Visible=", button33["visible"]			
			print lineNum(), "~", button34["name"], "Visible=", button34["visible"]
			print lineNum(), "~", button35["name"], "Visible=", button35["visible"]

			defineButtons()	
			
		elif button30["enabled"] == True:
			print lineNum(), "was true, turning to false"
			button30["enabled"] = False
			button30["color"] = pgvar.UI_button_color
			button31["visible"] = False
			button32["visible"] = False
			button33["visible"] = False			
			button34["visible"] = False
			button35["visible"] = False		
			
			print lineNum(), "~", button31["name"], "Visible=", button31["visible"]
			print lineNum(), "~", button32["name"], "Visible=", button32["visible"]
			print lineNum(), "~", button33["name"], "Visible=", button33["visible"]			
			print lineNum(), "~", button34["name"], "Visible=", button34["visible"]
			print lineNum(), "~", button35["name"], "Visible=", button35["visible"]

			defineButtons()
			redrawEverything()

	if selected_button == "menu01option01":
		if button30["enabled"] == True:
			print "~~ you clicked Monday ~~"
			if button31["enabled"] == False:
				button31["enabled"] = True
				button31["color"] = pgvar.UI_button_selected_color
				defineButtons()
			elif button31["enabled"] == True:
				button31["enabled"] = False
				button31["color"] = pgvar.UI_button_color
				defineButtons()

	if selected_button == "menu01option02":
		if button30["enabled"] == True:
			print "~~ you clicked Tuesday ~~"
			if button32["enabled"] == False:
				button32["enabled"] = True
				button32["color"] = pgvar.UI_button_selected_color
				defineButtons()
			elif button32["enabled"] == True:
				button32["enabled"] = False
				button32["color"] = pgvar.UI_button_color
				defineButtons()

	if selected_button == "menu01option03":
		if button30["enabled"] == True:
			print "~~ you clicked Wednesday ~~"
			if button33["enabled"] == False:
				button33["enabled"] = True
				button33["color"] = pgvar.UI_button_selected_color
				defineButtons()
			elif button33["enabled"] == True:
				button33["enabled"] = False
				button33["color"] = pgvar.UI_button_color
				defineButtons()

	if selected_button == "menu01option04":
		if button30["enabled"] == True:
			print "~~ you clicked Thursday ~~"
			if button34["enabled"] == False:
				button34["enabled"] = True
				button34["color"] = pgvar.UI_button_selected_color
				defineButtons()
			elif button34["enabled"] == True:
				button34["enabled"] = False
				button34["color"] = pgvar.UI_button_color
				defineButtons()

	if selected_button == "menu01option05":
		if button30["enabled"] == True:
			print "~~ you clicked Friday ~~"
			if button35["enabled"] == False:
				button35["enabled"] = True
				button35["color"] = pgvar.UI_button_selected_color
				defineButtons()
			elif button35["enabled"] == True:
				button35["enabled"] = False
				button35["color"] = pgvar.UI_button_color
				defineButtons()

	## END MENU 01 HANDLING

	## START MENU 02 HANDLING

	if selected_button == "menu02":
		if button36["enabled"] == False:
			# flip this menu button
			button36["enabled"] = True
			button36["color"] = pgvar.UI_button_selected_color
			
			# flip related buttons in the group
			button40["visible"] = True
			button41["visible"] = True
			button42["visible"] = True			

			defineButtons()	

		elif button36["enabled"] == True:
			# flip this menu button
			button36["enabled"] = False
			button36["color"] = pgvar.UI_button_color
			
			# flip related buttons in the group
			button40["visible"] = False
			button41["visible"] = False
			button42["visible"] = False			

			defineButtons()
			redrawEverything()	

	if selected_button == "menu02popup01":
		if button36["enabled"] == True:
			if button40["enabled"] == False:
				#flip this menu buttone
				button40["enabled"] = True
				button40["color"] = pgvar.UI_button_selected_color

				#flip related buttons
				button43["visible"] = True
				button44["visible"] = True
				button45["visible"] = True
				button46["visible"] = True
				button47["visible"] = True
				button48["visible"] = True
				button49["visible"] = True	
				button50["visible"] = True

				defineButtons()
				#redrawEverything()	
		
			elif button40["enabled"] == True:
				#flop this menu buttone
				button40["enabled"] = False
				button40["color"] = pgvar.UI_button_color

				button43["visible"] = False
				button44["visible"] = False
				button45["visible"] = False
				button46["visible"] = False
				button47["visible"] = False
				button48["visible"] = False
				button49["visible"] = False	
				button50["visible"] = False

				defineButtons()
				redrawEverything()	

	## END START MENU 02 HANDLING



## ############################################################################################
## UPDATE TEXT ENTRY BUTTONS
## ############################################################################################

def updateTextEntry(selected_button):
	if selected_button == "textField01":
		if button39["enabled"] == False:
			button39["enabled"] = True
			button39["color"] = UI_text_entry_box_color_active
			defineButtons()
			#enumerateButtons()

		elif button39["enabled"] == True:
			button39["enabled"] = False
			button39["color"] = UI_text_entry_box_color
			defineButtons()







## ############################################################################################
## OTHER FUNCTIONS
## ############################################################################################

"""
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

# # Redraw the backgroundm, buttons, screen, etc. 
def redrawEverything():
	print lineNum(), "redrawEverything() - started"
	
	print lineNum(), "drawing background"
	screen.fill(background_color)

	# check if draw grids is enabled, and draw if so
	if button21["enabled"] == True:
		drawGrid()

	# check if draw origin is enabled, and draw if so. 
	if button22["enabled"] == True:
		drawOrigin()

	print lineNum(), "drawing borders and frames"
	pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
	pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))

	print lineNum(), "redifining buttons and redrawing"
	defineButtons()
	for i, button in enumerate(my_buttons):
		button.display()

	print lineNum(), "redrawEverything() - completed"
"""



# # Draw origin lines
def drawOrigin():
	pygame.draw.lines(screen, red, False, [((pygame_window_width / 2),0),((pygame_window_width / 2 ),pygame_window_height)],2)
	pygame.draw.lines(screen, red, False, [(0,(pygame_window_height / 2)),(pygame_window_width, (pygame_window_height / 2))],2)


# # Draw grid lines
def drawGrid():
	# # Draw grid
	grid_width = pygame_window_width / 10
	grid_height = pgvar.pygame_window_height / 10

	pygame.draw.lines(screen, gridYellow, False, [((pygame_window_width / 2),0),((pygame_window_width / 2 ),pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width,0),(grid_width,pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width * 2,0),(grid_width * 2,pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width * 3,0),(grid_width * 3,pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width * 4,0),(grid_width * 4,pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width * 6,0),(grid_width * 6,pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width * 7,0),(grid_width * 7,pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width * 8,0),(grid_width * 8,pygame_window_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(grid_width * 9,0),(grid_width * 9,pygame_window_height)],1)

	pygame.draw.lines(screen, gridYellow, False, [(0,(pygame_window_height / 2)),(pygame_window_width, (pygame_window_height / 2))],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height), (pygame_window_height,grid_height)],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height * 2), (pygame_window_height,grid_height * 2)],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height * 3), (pygame_window_height,grid_height * 3)],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height * 4), (pygame_window_height,grid_height * 4)],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height * 6), (pygame_window_height,grid_height * 6)],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height * 7), (pygame_window_height,grid_height * 7)],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height * 8), (pygame_window_height,grid_height * 8)],1)
	pygame.draw.lines(screen, gridYellow, False, [(0,grid_height * 9), (pygame_window_height,grid_height * 9)],1)	








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

		# render "sticky" type buttons
		elif self.buttonType == "sticky":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "label" type buttons
		elif self.buttonType == "label":
			self.color = pgvar.UI_label_color																	# since self.color = buttonColor by default, this overwrites that for labels
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "group" type buttons
		elif self.buttonType == "group":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "dropdown" type buttons
		elif self.buttonType == "dropdown":	
			
			if self.buttonVisible == True:
				#print lineNum(), "rendering dropdown type buttons, button: ", self.button_name, "buttonVisible?:", self.buttonVisible
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)						# set label
				screen.blit(label, (self.x + 5, self.y))														# draw label



		# render "Menu" type buttons
		elif self.buttonType == "menu":	
			
			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))


		elif self.buttonType == "textEntry":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "popup" type buttons
		elif self.buttonType == "popup":

			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))

		elif self.buttonType == "popup_element":

			if self.button_name == "menu02popup01element03":
				self.buttonVisible = button45["visible"]
			if self.button_name == "menu02popup01element06":
				self.buttonVisible = button48["visible"]


			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				#pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))

		elif self.buttonType == "popup_element_button":

			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 1)  	#border

				label = myfont.render(str(self.button_label_txt), 0, UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))



# ************************************************************************************************************************
# ************************************************************************************************************************
# 	MAIN code	#
# ************************************************************************************************************************
# ************************************************************************************************************************


########## EVENT MONITORING / UPDATE DISPLAY ########### 

"""
running = True

while running:
"""

"""
	if buttonFPS["enabled"] == True:
		pygame.draw.rect(screen, blue, (pygame_window_width - 100, pygame_window_height - 30, 80, 20))   
		count_fps()
		show_fps()
"""


	for event in pygame.event.get():

		"""
		if event.type == pygame.QUIT:
			running = False
		"""	
		
		"""
		if event.type == pygame.MOUSEBUTTONDOWN:							#mousebuttondown only runs once, things run outside if this if loop
			(mouseX, mouseY) = pygame.mouse.get_pos()						# will run continually while button is held down
			print lineNum(), "mouseX = ", mouseX, "mouseY = ", mouseY			# this if.even MOUSEBUTTONDOWN **MUST** be under the for event in pygame.event.get() to run only once
			selected_button = findButton(my_buttons, mouseX, mouseY)
			print lineNum(), "selected button = ", selected_button

			if selected_button != None:
		
				if selected_button.button_label_txt == "EXIT":
					print lineNum(), "you pressed exit"
					running = False
		"""

				"""		
				if selected_button.buttonType == "pushy":
					print lineNum(), "running MOUSEBUTTONDOWN pushy event"
					print lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = UI_button_click_color
					print lineNum(), "selected_button.color now : ", selected_button.color			
					selected_button.buttonEnabled = True
					print lineNum(), "clicked button is a pushy temporary button"
				"""

				"""
					if selected_button.button_name == "command01":
						print lineNum(), "you clicked command01"
						buttonCommand01["enabled"] = True
						buttonCommand01["color"] = UI_button_click_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print lineNum(), "running code for Command01"
						# command01 function call goes here:
				"""

				"""
					if selected_button.button_name == "command02":
						print lineNum(), "you clicked command02"
						buttonCommand02["enabled"] = True
						buttonCommand02["color"] = UI_button_click_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print lineNum(), "running code for Command02"
						#command02 function call goes here:


					if selected_button.button_name == "command03":
						print lineNum(), "you clicked command03"
						buttonCommand03["enabled"] = True
						buttonCommand03["color"] = UI_button_click_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print lineNum(), "running code for Command03"
						#command03 function call goes here:		
				"""

				"""
				if selected_button.buttonType == "sticky":
					print lineNum(), "running sticky event"
					updateStickyButtons(selected_button.button_name)
				"""

				"""
				if selected_button.buttonType == "group":
					print lineNum(), "running group type button event"
					updateGroupButtons(selected_button.button_name)
				"""
		
				if selected_button.buttonType == "dropdown":
					print lineNum(), "running dropdown button event"
					updateDropdownButtons(selected_button.button_name)

				if selected_button.buttonType == "menu":
					print lineNum(), "running menu button event"
					updateMenuButtons(selected_button.button_name)

				if selected_button.buttonType == "textEntry":
					print lineNum(), "running text entry event"
					updateTextEntry(selected_button.button_name)

		if event.type == pygame.KEYDOWN:
		 	print "you pressed a key"
		 	if button39["enabled"] == True:

			 	if event.key == pygame.K_RETURN:
			 		print(entered_text)
			 		#entered_text = ""
					button39["label_txt"] = entered_text
					button39["enabled"] = False
					button39["color"] = UI_text_entry_box_color
					defineButtons()
					enumerateButtons()

				elif event.key == pygame.K_BACKSPACE:
					entered_text = entered_text[:-1]
					button39["label_txt"] = entered_text
					defineButtons()
					enumerateButtons()

				else:
			 		if len(entered_text) <= 15:
						entered_text += event.unicode
						print "entered_text", entered_text
						button39["label_txt"] = entered_text
						defineButtons()
						enumerateButtons()


		"""
		if event.type == pygame.MOUSEBUTTONUP:

			if selected_button != None:
				
				if selected_button.buttonType == "pushy":
					print lineNum(), "running MOUSEBUTTONUP pushy event"
					print lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = pgvar.UI_button_color 			#reverts button back to normal color after letting go of mouse
					print lineNum(), "selected_button.color now : ", selected_button.color	
			
					if selected_button.button_name == "command01":
						print lineNum(), "you clicked command01"
						buttonCommand01["enabled"] = False
						buttonCommand01["color"] = pgvar.UI_button_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event command01"
						for i, button in enumerate(my_buttons):
							button.display()

					if selected_button.button_name == "command02":
						print lineNum(), "you clicked command02"
						buttonCommand02["enabled"] = False
						buttonCommand02["color"] = pgvar.UI_button_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event command02"
						for i, button in enumerate(my_buttons):
							button.display()



					if selected_button.button_name == "command03":
						print lineNum(), "you clicked command03"
						buttonCommand03["enabled"] = False
						buttonCommand03["color"] = pgvar.UI_button_color
						defineButtons()

						print lineNum(), "____drawing buttons from pushy event command03"
						for i, button in enumerate(my_buttons):
							button.display()
		"""
			

			selected_button = None
			print lineNum(), "buttons27,28,29 visible:", button27["visible"], button28["visible"], button29["visible"]
			print lineNum(), "selected_button = ", selected_button
			print lineNum(), "buttons27,28,29 visible:", button27["visible"], button28["visible"], button29["visible"]
			
			# # re draw buttons!
			# # without this here, pushy buttons don't return to normal on mouseup
			print lineNum(), "____drawing buttons in MOUSEBUTTONUP call"
			#print lineNum(), "buttons27,28,29 visible:", button27["visible"], button28["visible"], button29["visible"]
			for i, button in enumerate(my_buttons):
				button.display()		
			
			print lineNum(), "buttons27,28,29 visible:", button27["visible"], button28["visible"], button29["visible"]
			

	# always do this last
	pygame.display.flip()