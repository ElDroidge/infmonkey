#py-infmonkey
#A simple program that is inspired by the "infinite monkey theorem",
#where a monkey hitting random keys on a typewriter keyboard
#for an infinite amount of time will almost surely produce
#a recognizable text, such as the complete works of William Shakespeare.
#This version has the lowercase letters of the English Alphabet; 
#along with a period/full stop, a comma, and a space. 

import sys
import string
import random

#custom functions here
def sepr():
	print("----------\n")

#variables here	
charSet = (tuple(string.ascii_lowercase) + (".", ",", " ")) #Declares the keys on the typewriter keyboard
charTotal = raw_input("Number of characters to output: ") #Declares the number of keys in final document
lineBreak = raw_input("Number of characters to break line after: ")

sepr()

for i in range(int(charTotal)):
    if i % int(lineBreak) == 0 and i != 0:
    	print("\n")
    sys.stdout.write(random.choice(charSet))
print("\n")

sepr()
	



