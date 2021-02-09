#!/usr/bin/env python3
import sys
stdin_fileno = sys.stdin

debug = 0

def splash():
	print("***********************************************")
	print("*** program to convert temperature          ***")
	print("*** from celsius to fahrenheit degrees      ***")
	print("***********************************************")

def conversion(c):
    if (debug):
        print("you selected", c)
    f = (9/5)*int(c) + 32
    print(int(c), "°C = ", f ,"°F")



def bye():
	print("goodbye.")
	k = input("press enter to close the terminal")



if (debug): 
    splash()
line = stdin_fileno
for line in stdin_fileno:
	conversion(line)
if (debug): 
    bye()
