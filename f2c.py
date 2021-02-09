#!/usr/bin/env python3

def splash():
	print("***********************************************")
	print("*** program to convert temperature          ***")
	print("*** from celsius to fahrenheit degrees      ***")
	print("***********************************************")

def conversion():
	c = input("what is the temperature in degrees celsius?")
	print("you selected", c)
	f = (9/5)*int(c) + 32
	print(c, "degrees celsius = ", f ,"degrees fahrenheit.")


def ui_loop():
	while (1):
		a = input("do you want do another conversion (y/n)?")
		if (a == "Y" or a == "y"): 
			conversion()
		elif (a == "n" or a == "N"): 
			bye()
			break
		else:
			print("please type y or n")

def bye():
	print("goodbye.")
	k = input("press enter to close the terminal")



splash()
conversion()
ui_loop()

