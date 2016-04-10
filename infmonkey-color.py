#Infinite Monkey Theorem - Color Edition
#by Droidge

#Colour index:
#30 - Black
#31 - Red
#32 - Green
#33 - Yellow
#34 - Blue
#35 - Magenta
#36 - Cyan
#37 - White
#38 - Crimson

import sys
import random

colSelection = [34, 37, 31,] #Colours to use - refer to Colour Index
totalChar = raw_input("Number of characters to output (try 320): ")
lineBreak = raw_input("Number of characters to break line after (try 40): ")

def randomColour():
	foo = random.choice(colSelection) 
	return foo

print("(Try moving mousewheel if output seems to have halted)")
for i in range(int(totalChar)):
	if i % int(lineBreak) == 0:
		print("\n")
	sys.stdout.write('\033[1;' + str(randomColour()) + 'm#\033[1;m')
