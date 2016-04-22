#Infinite Monkey Theorem - Color Edition
#by Droidge

#Colour index:
#0 - Black
#1 - Red
#2 - Green
#3 - Yellow
#4 - Blue
#5 - Magenta
#6 - Cyan
#7 - White
#8 - Crimson

import sys
import random

colSelection = raw_input("Colours to use (refer to Colour Index inside code) (eg. '07' for 'Black' and 'White'): ")
#print(list(colSelection))
totalChar = raw_input("Number of 'pixels' to print: ")
lineBreak =raw_input("Number of 'pixels' to break line after: ")

def randomColour():
	foo = random.choice(list(colSelection)) 
	return foo

print("\n(Try moving mousewheel if output seems to have halted)")
for i in range(int(totalChar)):
	if i % int(lineBreak) == 0:
		print("")
	sys.stdout.write('\033[1;' + '3' + str(randomColour()) + 'm██\033[1;m')
