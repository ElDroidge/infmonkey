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

charSet = (tuple(string.ascii_lowercase) + (".", ",", " ")) #Declares the keys on the typewriter keyboard
charTotal = raw_input("Number of characters to output: ") #Declares the number of keys in final document
lineBreak = raw_input("Number of characters to break line after: ")

print("----------")

for i in range(int(charTotal)):
    sys.stdout.write(random.choice(charSet))
    if i % lineBreak = 0:
    	print("\n")
    	

print("\n----------")
	



