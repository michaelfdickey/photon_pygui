# temp.py
	



	if selected_button == "sticky02":
		if pgui.buttonSticky02["enabled"] == False:
			print lineNum(), "sticky02 button found"
			pgui.buttonSticky02["enabled"] = True
			pgui.buttonSticky02["color"] = pgvar.UI_button_selected_color
			print lineNum(), "flipped sticky02 from false to true"
			pfunc.defineButtons()	
			
		elif pgui.buttonSticky02["enabled"] == True:
			print lineNum(), "sticky02 button found"
			pgui.buttonSticky02["enabled"] = False
			pgui.buttonSticky02["color"] = pgvar.UI_button_color
			print lineNum(), "flipped sticky02 from true to false"
			pfunc.defineButtons()