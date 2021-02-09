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
    c = 5/9*(int(f) - 32)
    print(int(f), "°F = ", c ,"°C")



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
