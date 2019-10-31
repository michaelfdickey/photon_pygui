# nested dictionaries

width = 100
height = 100

button01 = {}
button01[0] = "button01"
button01[1] = 0
button01[2] = width
button01[3] = height
button01[4] = True

button02 = {}
button02[0] = "button02"
button02[1] = 0
button02[2] = width
button02[3] = height
button02[4] = True

button03 = {}
button03[0] = "button03"
button03[1] = 0
button03[2] = width
button03[3] = height
button03[4] = True

allButtons = {}
allButtons[0] = button01
allButtons[1] = button02
allButtons[2] = button03

print "allButtons Dict: ", allButtons

print "allButtons[0]    : ", allButtons[0]

print "allButtons[0][0]", allButtons[0][0]


newButton = {}


for allButtonsID, allButtonsValue in allButtons.items():
	#print "allButtons key: ", allButtonsID

	for key in allButtonsValue:
		#print "key in allButtonsValue: ", key, " value :", allButtonsValue[key]
		newButton[key] = allButtonsValue[key]
		print "newButton iterated key: ", key, "value: ", newButton[key]

print "newButton dict  : ", newButton
print "newButton dict[0] : ", newButton[0]