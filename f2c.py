#!/usr/bin/env python3
import sys
stdin_fileno = sys.stdin

debug = 0


def splash():
	print("***********************************************")
	print("*** program to convert temperature          ***")
	print("*** from celsius to fahrenheit degrees      ***")
	print("***********************************************")

def conversion(f):
    if (debug):
        print("you selected", f)
    c = 5/9*(float(f) - 32)
    print("{:8.2f}".format(float(f)), "F deg. = ", "{:8.2f}".format(c) ,"C deg.")



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
