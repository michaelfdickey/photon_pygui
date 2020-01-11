

# ************************************************************************************
#	initial variables	#
# ************************************************************************************


# ************************************************************************************
#	initial lists	#
# ************************************************************************************



# ************************************************************************************
# 	initial dictionaries 		#











menu02popup01element08 = {}
menu02popup01element08["name"] = "menu02popup01element08"													# button_name
menu02popup01element08["origin_x"] = pgvar.UI_popup_small_origin_x + pgvar.UI_popup_small_width -80		# button_origin_x
menu02popup01element08["origin_y"] = pgvar.UI_popup_small_origin_y + pgvar.UI_popup_small_height - 40 		# button_origin_y
menu02popup01element08["width"] = 60																		# button_width
menu02popup01element08["height"] = 20																		# button_height
menu02popup01element08["label_txt"] = "Cancel"															# button_label_txt
menu02popup01element08["type"] = "popup_element_button"													# buttonType
menu02popup01element08["enabled"] = False																	# buttonEnabled
menu02popup01element08["color"] = pgvar.UI_button_color 													# buttonColor
menu02popup01element08["group"] = "menu02popup01"															# buttonGroup
menu02popup01element08["visible"] = True																# buttonVisible







"""
allButtons[12] = labelGroup02		# group02 label
allButtons[13] = bGroup02Button01 	# group02 button 01
allButtons[14] = bGroup02Button02		# group02 button 02
allButtons[15] = labelGroup03		# group03 label
allButtons[16] = bGroup03Button01 	# group03 button 01
allButtons[17] = bGroup03Button02		# group03 button 02
allButtons[18] = bGroup03Button03		# group03 button 03
allButtons[19] = buttonFPS		# FPS display
allButtons[20] = button20 	# display scale
allButtons[21] = buttonGrid 	# display grid
allButtons[22] = buttonOrigin 	# display origin
allButtons[23] = button23		# display options label
allButtons[24] = labelDropdown 	# Dropdown01 - Label
allButtons[25] = lDropdown01TEXT		# Dropdown01 - selected display
allButtons[26] = bDropdown01opener		# Dropdown01 - opener
allButtons[27] = bDropdown01option01		# Dropdown01 - option1
allButtons[28] = bDropdown01option02		# Dropdown01 - option2
allButtons[29] = bDropdown01option03		# Dropdown01 - option3
"""







allButtons[37] = button37		# Menu 03











allButtons[50] = menu02popup01element08		# Menu 02  - small popup - element 06 - cancel button



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


"""
def enumerateButtons():
	for i, button in enumerate(my_buttons):
		button.display()	
"""

"""
# # #########################################################################################
# # This figures out which button was clicked
def findButton(buttons, x, y):
	for b in buttons:
		if x <= b.x + b.x_width:
			if x >= b.x:
				if y >= b.y:
					if y <= b.y + b.y_height:
						print pfunc.lineNum(), "selected button label_txt = ", b.button_name
						return b
	return None
"""



# # #########################################################################################
# # this updates pushy buttons
def updatePushyButtons(selected_button):
	print pfunc.lineNum(), "updating pushy buttons"

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
	print pfunc.lineNum(), "updateStickyButtons() - started"
	print pfunc.lineNum(), "selected_button = ", selected_button
"""
	"""
	# for sticky buttons, iterate through nested allButtons dictionary and flip buttonEnabled
	for allButtonsID, allButtonsValue in allButtons.items():
		for key in allButtonsValue:
			#print pfunc.lineNum(), "key", key
			#buttonToCheck[key] = allButtonsValue[key]
			#print pfunc.lineNum(), "buttonToCheck", key, allButtonsValue[key]
			if allButtonsValue[key] == "sticky":
				print pfunc.lineNum(), "found a sticky button"
				print pfunc.lineNum(), "key, ", key, "value", allButtonsValue[key]
				#print pfunc.lineNum(), "buttonToCheck", key, allButtonsValue[key]
	"""
"""	
	if selected_button == "sticky01":
		if buttonSticky01["enabled"] == False:
			print pfunc.lineNum(), "sticky01 button found"
			buttonSticky01["enabled"] = True
			buttonSticky01["color"] = pgvar.UI_button_selected_color
			print pfunc.lineNum(), "flipped sticky01 from false to true"
			pfunc.pfunc.defineButtons()
			
		elif buttonSticky01["enabled"] == True:
			print pfunc.lineNum(), "sticky01 button found"
			buttonSticky01["enabled"] = False
			buttonSticky01["color"] = pgvar.UI_button_color
			print pfunc.lineNum(), "flipped stick01 from true to false"
			pfunc.defineButtons()
"""

"""
	if selected_button == "sticky02":
		if buttonSticky02["enabled"] == False:
			print pfunc.lineNum(), "sticky02 button found"
			buttonSticky02["enabled"] = True
			buttonSticky02["color"] = pgvar.UI_button_selected_color
			print pfunc.lineNum(), "flipped sticky02 from false to true"
			pfunc.pfunc.defineButtons()
			
		elif buttonSticky02["enabled"] == True:
			print pfunc.lineNum(), "sticky02 button found"
			buttonSticky02["enabled"] = False
			buttonSticky02["color"] = pgvar.UI_button_color
			print pfunc.lineNum(), "flipped sticky02 from true to false"
			pfunc.defineButtons()
"""
"""
	if selected_button == "sticky03":
		if buttonSticky03["enabled"] == False:
			print pfunc.lineNum(), "sticky03 button found"
			buttonSticky03["enabled"] = True
			buttonSticky03["color"] = pgvar.UI_button_selected_color
			print pfunc.lineNum(), "flipped sticky03 from false to true"
			pfunc.pfunc.defineButtons()
			
		elif buttonSticky03["enabled"] == True:
			print pfunc.lineNum(), "sticky03 button found"
			buttonSticky03["enabled"] = False
			buttonSticky03["color"] = pgvar.UI_button_color
			print pfunc.lineNum(), "flipped sticky03 from true to false"
			pfunc.pfunc.defineButtons()		
"""

"""
	# # # FPS BUTTON
	if selected_button == "fps":
		if buttonFPS["enabled"] == False:
			buttonFPS["enabled"] = True
			buttonFPS["color"] = pgvar.UI_button_selected_color
			pfunc.pfunc.defineButtons()
			
		elif buttonFPS["enabled"] == True:
			buttonFPS["enabled"] = False
			buttonFPS["color"] = pgvar.UI_button_color
			pfunc.redrawEverything()
"""

"""
	# # # ORIGIN BUTTON
	if selected_button == "origin":
		if buttonOrigin["enabled"] == False:
			buttonOrigin["enabled"] = True
			buttonOrigin["color"] = pgvar.UI_button_selected_color
			pfunc.pfunc.defineButtons()
			pfunc.redrawEverything()
			
		elif buttonOrigin["enabled"] == True:
			buttonOrigin["enabled"] = False
			buttonOrigin["color"] = pgvar.UI_button_color
			pfunc.defineButtons()
			pfunc.redrawEverything()
"""


"""
	# # # GRID BUTTON
	if selected_button == "grid":
		if buttonGrid["enabled"] == False:
			buttonGrid["enabled"] = True
			buttonGrid["color"] = pgvar.UI_button_selected_color
			pfunc.pfunc.defineButtons()
			pfunc.redrawEverything()
			
		elif buttonGrid["enabled"] == True:
			buttonGrid["enabled"] = False
			buttonGrid["color"] = pgvar.UI_button_color
			pfunc.defineButtons()
			pfunc.redrawEverything()
"""

	print pfunc.lineNum(), "updateStickyButtons() - completed"
	return
	



## ############################################################################################
## UPDATE GROUP BUTTONS
## ############################################################################################

"""
def updateGroupButtons(selected_button):
	print pfunc.lineNum(), "running update group buttons"

	# # Group 01 processing
	if selected_button == "Group01Button01":
		
		if bGroup01Button01["enabled"] == True:
			bGroup01Button01["enabled"] = False
			bGroup01Button01["color"] = pgvar.UI_button_color
			bGroup01Button02["enabled"] = True
			bGroup01Button02["color"] = pgvar.UI_button_selected_color
			pfunc.pfunc.pfunc.defineButtons()
		
		elif bGroup01Button01["enabled"] == False:
			bGroup01Button01["enabled"] = True
			bGroup01Button01["color"] = pgvar.UI_button_selected_color
			bGroup01Button02["enabled"] = False
			bGroup01Button02["color"] = pgvar.UI_button_color
			pfunc.pfunc.pfunc.defineButtons()

	if selected_button == "Group01Button02":
		
		if bGroup01Button02["enabled"] == True:
			bGroup01Button02["enabled"] = False
			bGroup01Button02["color"] = pgvar.UI_button_color
			bGroup01Button01["enabled"] = True
			bGroup01Button01["color"] = pgvar.UI_button_selected_color
			pfunc.pfunc.pfunc.defineButtons()
		
		elif bGroup01Button02["enabled"] == False:
			bGroup01Button02["enabled"] = True
			bGroup01Button02["color"] = pgvar.UI_button_selected_color
			bGroup01Button01["enabled"] = False
			bGroup01Button01["color"] = pgvar.UI_button_color
			pfunc.pfunc.defineButtons()
"""

"""
	# # Group 02 processing
	if selected_button == "Group02Button01":
		
		if bGroup02Button01["enabled"] == True:
			bGroup02Button01["enabled"] = False
			bGroup02Button01["color"] = pgvar.UI_button_color
			bGroup02Button02["enabled"] = True
			bGroup02Button02["color"] = pgvar.UI_button_selected_color
			pfunc.pfunc.defineButtons()
		
		elif bGroup02Button01["enabled"] == False:
			bGroup02Button01["enabled"] = True
			bGroup02Button01["color"] = pgvar.UI_button_selected_color
			bGroup02Button02["enabled"] = False
			bGroup02Button02["color"] = pgvar.UI_button_color
			pfunc.pfunc.defineButtons()

	if selected_button == "Group02Button02":
		
		if bGroup02Button02["enabled"] == True:
			bGroup02Button02["enabled"] = False
			bGroup02Button02["color"] = pgvar.UI_button_color
			bGroup02Button01["enabled"] = True
			bGroup02Button01["color"] = pgvar.UI_button_selected_color
			pfunc.pfunc.defineButtons()
		
		elif bGroup02Button02["enabled"] == False:
			bGroup02Button02["enabled"] = True
			bGroup02Button02["color"] = pgvar.UI_button_selected_color
			bGroup02Button01["enabled"] = False
			bGroup02Button01["color"] = pgvar.UI_button_color
			pfunc.defineButtons()
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

			pfunc.pfunc.pfunc.defineButtons()

	if selected_button == "Group03Button02":
		
		if bGroup03Button02["enabled"] == False:
			bGroup03Button02["enabled"] = True
			bGroup03Button02["color"] = pgvar.UI_button_selected_color
			
			bGroup03Button01["enabled"] = False
			bGroup03Button01["color"] = pgvar.UI_button_color
			
			bGroup03Button03["enabled"] = False
			bGroup03Button03["color"] = pgvar.UI_button_color

			pfunc.pfunc.pfunc.defineButtons()

	if selected_button == "Group03Button03":
		
		if bGroup03Button03["enabled"] == False:
			bGroup03Button03["enabled"] = True
			bGroup03Button03["color"] = pgvar.UI_button_selected_color
			
			bGroup03Button01["enabled"] = False
			bGroup03Button01["color"] = pgvar.UI_button_color
			
			bGroup03Button02["enabled"] = False
			bGroup03Button02["color"] = pgvar.UI_button_color

			pfunc.pfunc.pfunc.defineButtons()
"""

"""
## ############################################################################################
## UPDATE DROPDOWN BUTTONS
## ############################################################################################

def updateDropdownButtons(selected_button):
	print pfunc.lineNum(), "running update Dropdown buttons"

	if selected_button == "dropdown01opener":
		if bDropdown01opener["enabled"] == False:
			print pfunc.lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			# update this button
			bDropdown01opener["enabled"] = True
			bDropdown01opener["color"] = pgvar.UI_button_selected_color
			bDropdown01opener["label_txt"] = "<<"

			# update associated buttons
			bDropdown01option01["visible"] = True	
			bDropdown01option02["visible"] = True
			bDropdown01option03["visible"] = True

			pfunc.pfunc.defineButtons()

			print pfunc.lineNum(), "~~~~ running dropdown opener fasle to true  ~~~~"
			print pfunc.lineNum(), bDropdown01opener["name"], "enabled:", bDropdown01opener["enabled"], "visible:", bDropdown01opener["visible"]
			
		elif bDropdown01opener["enabled"] == True:
			print " --------------------------------------- "
			print pfunc.lineNum(), "STARTED dropdown true to false "
			print " --------------------------------------- "

			# udapte this button
			print pfunc.lineNum(), bDropdown01opener["name"], "enabled was: ", bDropdown01opener["enabled"]
			bDropdown01opener["enabled"] = False
			bDropdown01opener["color"] = pgvar.UI_button_color
			bDropdown01opener["label_txt"] = ">>"
			print pfunc.lineNum(), bDropdown01opener["name"], "enabled:", bDropdown01opener["enabled"], "visible:", bDropdown01opener["visible"]

			# update associated buttons
			bDropdown01option01["visible"] = False
			bDropdown01option02["visible"] = False
			bDropdown01option03["visible"] = False
			print pfunc.lineNum(), "buttons27,28,29 visible:", bDropdown01option01["visible"], bDropdown01option02["visible"], bDropdown01option03["visible"]

			screen.fill(background_color)
			pfunc.defineButtons()
			pfunc.redrawEverything()

			print pfunc.lineNum(), bDropdown01opener["name"], "enabled:", bDropdown01opener["enabled"], "visible:", bDropdown01opener["visible"]
			print " --------------------------------------- "
			print pfunc.lineNum(), "FINISHED dropdown true to false "
			print " --------------------------------------- "
			print type(bDropdown01option01["visible"])

	if selected_button == "dropdown01option01":
		if bDropdown01opener["enabled"] == True:
			lDropdown01TEXT["label_txt"] = "Option 01"
			bDropdown01option01["color"] = pgvar.UI_button_selected_color
			bDropdown01option02["color"] = pgvar.UI_button_color
			bDropdown01option03["color"] = pgvar.UI_button_color
			pfunc.defineButtons()

	if selected_button == "dropdown01option02":
		if bDropdown01opener["enabled"] == True: 
			lDropdown01TEXT["label_txt"] = "Option 02"
			bDropdown01option01["color"] = pgvar.UI_button_color
			bDropdown01option02["color"] = pgvar.UI_button_selected_color
			bDropdown01option03["color"] = pgvar.UI_button_color		
			pfunc.defineButtons()

	if selected_button == "dropdown01option03":
		if bDropdown01opener["enabled"] == True:
			lDropdown01TEXT["label_txt"] = "Option 03"
			bDropdown01option01["color"] = pgvar.UI_button_color
			bDropdown01option02["color"] = pgvar.UI_button_color
			bDropdown01option03["color"] = pgvar.UI_button_selected_color
			pfunc.defineButtons()

	if selected_button == "dropdown01TEXT":
		if lDropdown01TEXT["label_txt"] != "- select -":
			if lDropdown01TEXT["enabled"] == False:
				lDropdown01TEXT["enabled"] = True
				lDropdown01TEXT["color"] = pgvar.UI_button_selected_color
				pfunc.pfunc.defineButtons()
				pfunc.redrawEverything()
				
			elif lDropdown01TEXT["enabled"] == True:
				lDropdown01TEXT["enabled"] = False
				lDropdown01TEXT["color"] = pgvar.UI_button_color
				pfunc.defineButtons()
				pfunc.redrawEverything()
"""



## ############################################################################################
## UPDATE MENU BUTTONS
## ############################################################################################

"""
def updateMenuButtons(selected_button):
	print pfunc.lineNum(), "running updateMenuButtons"

	## START MENU 01 HANDLING

	if selected_button == "menu01":
		print pfunc.lineNum(), "menu01 was clicked on"
		print pfunc.lineNum(), pgui.bMenu01["name"], "is ", pgui.bMenu01["enabled"]
		
		if pgui.bMenu01["enabled"] == False:
			print "was false, turning to true"
			
			pgui.bMenu01["enabled"] = True
			pgui.bMenu01["color"] = pgvar.UI_button_selected_color
			pgui.bMenu01option01["visible"] = True
			pgui.bMenu01option02["visible"] = True
			pgui.bMenu01option03["visible"] = True			
			pgui.bMenu01option04["visible"] = True
			pgui.bMenu01option05["visible"] = True

			print pfunc.lineNum(), "~", pgui.bMenu01option01["name"], "Visible=", pgui.bMenu01option01["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option02["name"], "Visible=", pgui.bMenu01option02["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option03["name"], "Visible=", pgui.bMenu01option03["visible"]			
			print pfunc.lineNum(), "~", pgui.bMenu01option04["name"], "Visible=", pgui.bMenu01option04["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option05["name"], "Visible=", pgui.bMenu01option05["visible"]

			pfunc.defineButtons()
			
		elif pgui.bMenu01["enabled"] == True:
			print pfunc.lineNum(), "was true, turning to false"
			pgui.bMenu01["enabled"] = False
			pgui.bMenu01["color"] = pgvar.UI_button_color
			pgui.bMenu01option01["visible"] = False
			pgui.bMenu01option02["visible"] = False
			pgui.bMenu01option03["visible"] = False			
			pgui.bMenu01option04["visible"] = False
			pgui.bMenu01option05["visible"] = False		
			
			print pfunc.lineNum(), "~", pgui.bMenu01option01["name"], "Visible=", pgui.bMenu01option01["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option02["name"], "Visible=", pgui.bMenu01option02["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option03["name"], "Visible=", pgui.bMenu01option03["visible"]			
			print pfunc.lineNum(), "~", pgui.bMenu01option04["name"], "Visible=", pgui.bMenu01option04["visible"]
			print pfunc.lineNum(), "~", pgui.bMenu01option05["name"], "Visible=", pgui.bMenu01option05["visible"]

			pfunc.defineButtons()
			pfunc.redrawEverything()

	if selected_button == "menu01option01":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Monday ~~"
			if pgui.bMenu01option01["enabled"] == False:
				pgui.bMenu01option01["enabled"] = True
				pgui.bMenu01option01["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option01["enabled"] == True:
				pgui.bMenu01option01["enabled"] = False
				pgui.bMenu01option01["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option02":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Tuesday ~~"
			if pgui.bMenu01option02["enabled"] == False:
				pgui.bMenu01option02["enabled"] = True
				pgui.bMenu01option02["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option02["enabled"] == True:
				pgui.bMenu01option02["enabled"] = False
				pgui.bMenu01option02["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option03":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Wednesday ~~"
			if pgui.bMenu01option03["enabled"] == False:
				pgui.bMenu01option03["enabled"] = True
				pgui.bMenu01option03["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option03["enabled"] == True:
				pgui.bMenu01option03["enabled"] = False
				pgui.bMenu01option03["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option04":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Thursday ~~"
			if pgui.bMenu01option04["enabled"] == False:
				pgui.bMenu01option04["enabled"] = True
				pgui.bMenu01option04["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option04["enabled"] == True:
				pgui.bMenu01option04["enabled"] = False
				pgui.bMenu01option04["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	if selected_button == "menu01option05":
		if pgui.bMenu01["enabled"] == True:
			print "~~ you clicked Friday ~~"
			if pgui.bMenu01option05["enabled"] == False:
				pgui.bMenu01option05["enabled"] = True
				pgui.bMenu01option05["color"] = pgvar.UI_button_selected_color
				pfunc.defineButtons()
			elif pgui.bMenu01option05["enabled"] == True:
				pgui.bMenu01option05["enabled"] = False
				pgui.bMenu01option05["color"] = pgvar.UI_button_color
				pfunc.defineButtons()

	## END MENU 01 HANDLING
"""




	## START MENU 02 HANDLING

	if selected_button == "menu02":
		if bMenu02["enabled"] == False:
			# flip this menu button
			bMenu02["enabled"] = True
			bMenu02["color"] = pgvar.UI_button_selected_color
			
			# flip related buttons in the group
			bMenu02popup01["visible"] = True
			bMenu02popup02["visible"] = True
			bMenu02popup03["visible"] = True			

			pfunc.defineButtons()

		elif bMenu02["enabled"] == True:
			# flip this menu button
			bMenu02["enabled"] = False
			bMenu02["color"] = pgvar.UI_button_color
			
			# flip related buttons in the group
			bMenu02popup01["visible"] = False
			bMenu02popup02["visible"] = False
			bMenu02popup03["visible"] = False			

			pfunc.defineButtons()
			pfunc.redrawEverything()	

	if selected_button == "menu02popup01":
		if bMenu02["enabled"] == True:
			if bMenu02popup01["enabled"] == False:
				#flip this menu buttone
				bMenu02popup01["enabled"] = True
				bMenu02popup01["color"] = pgvar.UI_button_selected_color

				#flip related buttons
				menu02popup01element01["visible"] = True
				menu02popup01element02["visible"] = True
				menu02popup01element03["visible"] = True
				menu02popup01element04["visible"] = True
				menu02popup01element05["visible"] = True
				menu02popup01element06["visible"] = True
				menu02popup01element07["visible"] = True	
				menu02popup01element08["visible"] = True

				pfunc.defineButtons()
				#pfunc.redrawEverything()	
		
			elif bMenu02popup01["enabled"] == True:
				#flop this menu buttone
				bMenu02popup01["enabled"] = False
				bMenu02popup01["color"] = pgvar.UI_button_color

				menu02popup01element01["visible"] = False
				menu02popup01element02["visible"] = False
				menu02popup01element03["visible"] = False
				menu02popup01element04["visible"] = False
				menu02popup01element05["visible"] = False
				menu02popup01element06["visible"] = False
				menu02popup01element07["visible"] = False	
				menu02popup01element08["visible"] = False

				pfunc.defineButtons()
				pfunc.redrawEverything()	

	## END START MENU 02 HANDLING


"""

## ############################################################################################
## UPDATE TEXT ENTRY BUTTONS
## ############################################################################################

def updateTextEntry(selected_button):
	if selected_button == "textField01":
		if textField01["enabled"] == False:
			textField01["enabled"] = True
			textField01["color"] = UI_text_entry_box_color_active
			pfunc.defineButtons()
			#enumerateButtons()

		elif textField01["enabled"] == True:
			textField01["enabled"] = False
			textField01["color"] = UI_text_entry_box_color
			pfunc.defineButtons()

"""





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
def pfunc.redrawEverything():
	print pfunc.lineNum(), "pfunc.redrawEverything() - started"
	
	print pfunc.lineNum(), "drawing background"
	screen.fill(background_color)

	# check if draw grids is enabled, and draw if so
	if buttonGrid["enabled"] == True:
		drawGrid()

	# check if draw origin is enabled, and draw if so. 
	if buttonOrigin["enabled"] == True:
		drawOrigin()

	print pfunc.lineNum(), "drawing borders and frames"
	pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height))
	pygame.draw.rect(screen, UI_background_color, (0,0, UI_sideBar_width, pygame_window_height))

	print pfunc.lineNum(), "redifining buttons and redrawing"
	pfunc.defineButtons()
	for i, button in enumerate(my_buttons):
		button.display()

	print pfunc.lineNum(), "pfunc.redrawEverything() - completed"
"""


"""
# # Draw origin lines
def drawOrigin():
	pygame.draw.lines(screen, red, False, [((pygame_window_width / 2),0),((pygame_window_width / 2 ),pygame_window_height)],2)
	pygame.draw.lines(screen, red, False, [(0,(pygame_window_height / 2)),(pygame_window_width, (pygame_window_height / 2))],2)
"""

"""
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
"""







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
				#print pfunc.lineNum(), "rendering dropdown type buttons, button: ", self.button_name, "buttonVisible?:", self.buttonVisible
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
				self.buttonVisible = menu02popup01element03["visible"]
			if self.button_name == "menu02popup01element06":
				self.buttonVisible = menu02popup01element06["visible"]


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
			print pfunc.lineNum(), "mouseX = ", mouseX, "mouseY = ", mouseY			# this if.even MOUSEBUTTONDOWN **MUST** be under the for event in pygame.event.get() to run only once
			selected_button = findButton(my_buttons, mouseX, mouseY)
			print pfunc.lineNum(), "selected button = ", selected_button

			if selected_button != None:
		
				if selected_button.button_label_txt == "EXIT":
					print pfunc.lineNum(), "you pressed exit"
					running = False
		"""

				"""		
				if selected_button.buttonType == "pushy":
					print pfunc.lineNum(), "running MOUSEBUTTONDOWN pushy event"
					print pfunc.lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = UI_button_click_color
					print pfunc.lineNum(), "selected_button.color now : ", selected_button.color			
					selected_button.buttonEnabled = True
					print pfunc.lineNum(), "clicked button is a pushy temporary button"
				"""

				"""
					if selected_button.button_name == "command01":
						print pfunc.lineNum(), "you clicked command01"
						buttonCommand01["enabled"] = True
						buttonCommand01["color"] = UI_button_click_color
						pfunc.defineButtons()

						print pfunc.lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print pfunc.lineNum(), "running code for Command01"
						# command01 function call goes here:
				"""

				"""
					if selected_button.button_name == "command02":
						print pfunc.lineNum(), "you clicked command02"
						buttonCommand02["enabled"] = True
						buttonCommand02["color"] = UI_button_click_color
						pfunc.defineButtons()

						print pfunc.lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print pfunc.lineNum(), "running code for Command02"
						#command02 function call goes here:


					if selected_button.button_name == "command03":
						print pfunc.lineNum(), "you clicked command03"
						buttonCommand03["enabled"] = True
						buttonCommand03["color"] = UI_button_click_color
						pfunc.defineButtons()

						print pfunc.lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(my_buttons):
							button.display()

						print pfunc.lineNum(), "running code for Command03"
						#command03 function call goes here:		
				"""

				"""
				if selected_button.buttonType == "sticky":
					print pfunc.lineNum(), "running sticky event"
					updateStickyButtons(selected_button.button_name)
				"""

				"""
				if selected_button.buttonType == "group":
					print pfunc.lineNum(), "running group type button event"
					updateGroupButtons(selected_button.button_name)
				"""
				
				"""
				if selected_button.buttonType == "dropdown":
					print pfunc.lineNum(), "running dropdown button event"
					updateDropdownButtons(selected_button.button_name)
				"""

				"""
				if selected_button.buttonType == "menu":
					print pfunc.lineNum(), "running menu button event"
					updateMenuButtons(selected_button.button_name)
				"""
				
				"""
				if selected_button.buttonType == "textEntry":
					print pfunc.lineNum(), "running text entry event"
					updateTextEntry(selected_button.button_name)
				"""



		"""
		if event.type == pygame.KEYDOWN:
		 	print "you pressed a key"
		 	if textField01["enabled"] == True:

			 	if event.key == pygame.K_RETURN:
			 		print(entered_text)
			 		#entered_text = ""
					textField01["label_txt"] = entered_text
					textField01["enabled"] = False
					textField01["color"] = UI_text_entry_box_color
					pfunc.defineButtons()
					enumerateButtons()

				elif event.key == pygame.K_BACKSPACE:
					entered_text = entered_text[:-1]
					textField01["label_txt"] = entered_text
					pfunc.defineButtons()
					enumerateButtons()

				else:
			 		if len(entered_text) <= 15:
						entered_text += event.unicode
						print "entered_text", entered_text
						textField01["label_txt"] = entered_text
						pfunc.defineButtons()
						enumerateButtons()
		"""



		"""
		if event.type == pygame.MOUSEBUTTONUP:

			if selected_button != None:
				
				if selected_button.buttonType == "pushy":
					print pfunc.lineNum(), "running MOUSEBUTTONUP pushy event"
					print pfunc.lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = pgvar.UI_button_color 			#reverts button back to normal color after letting go of mouse
					print pfunc.lineNum(), "selected_button.color now : ", selected_button.color	
			
					if selected_button.button_name == "command01":
						print pfunc.lineNum(), "you clicked command01"
						buttonCommand01["enabled"] = False
						buttonCommand01["color"] = pgvar.UI_button_color
						pfunc.defineButtons()

						print pfunc.lineNum(), "____drawing buttons from pushy event command01"
						for i, button in enumerate(my_buttons):
							button.display()

					if selected_button.button_name == "command02":
						print pfunc.lineNum(), "you clicked command02"
						buttonCommand02["enabled"] = False
						buttonCommand02["color"] = pgvar.UI_button_color
						pfunc.defineButtons()

						print pfunc.lineNum(), "____drawing buttons from pushy event command02"
						for i, button in enumerate(my_buttons):
							button.display()



					if selected_button.button_name == "command03":
						print pfunc.lineNum(), "you clicked command03"
						buttonCommand03["enabled"] = False
						buttonCommand03["color"] = pgvar.UI_button_color
						pfunc.defineButtons()

						print pfunc.lineNum(), "____drawing buttons from pushy event command03"
						for i, button in enumerate(my_buttons):
							button.display()
		"""
			

			selected_button = None
			print pfunc.lineNum(), "buttons27,28,29 visible:", bDropdown01option01["visible"], bDropdown01option02["visible"], bDropdown01option03["visible"]
			print pfunc.lineNum(), "selected_button = ", selected_button
			print pfunc.lineNum(), "buttons27,28,29 visible:", bDropdown01option01["visible"], bDropdown01option02["visible"], bDropdown01option03["visible"]
			
			# # re draw buttons!
			# # without this here, pushy buttons don't return to normal on mouseup
			print pfunc.lineNum(), "____drawing buttons in MOUSEBUTTONUP call"
			#print pfunc.lineNum(), "buttons27,28,29 visible:", bDropdown01option01["visible"], bDropdown01option02["visible"], bDropdown01option03["visible"]
			for i, button in enumerate(my_buttons):
				button.display()		
			
			print pfunc.lineNum(), "buttons27,28,29 visible:", bDropdown01option01["visible"], bDropdown01option02["visible"], bDropdown01option03["visible"]
			

	# always do this last
	pygame.display.flip()