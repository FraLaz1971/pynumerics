#!/usr/bin/env python3

def splash():
    print("**********************************")
    print("*** tconv.py: python3 program ")
    print("*** to convert temperature")
    print("*** from celsius to fahrenheit")
    print("*** degrees and viceversa")
    print("**********************************")

def bye():
    print("goodbye.")
    k = input("press enter to close the terminal")

def c2f_conversion():
    c = input("what is the temperature in degrees celsius?")
    print("you selected", c)
    f = (9/5)*int(c) + 32
    print(c, "degrees celsius = ", int(f + 0.5) ,"degrees fahrenheit.")

def f2c_conversion():
    f = input("temperature in fahrenheit degrees ?")
    print("you selected", f)
    c = 5/9*(int(f) - 32)
    print(f, "degrees fahrenheit = ", int(c + 0.5) ,"degrees celsius.")

def conversions():
    print("do you want to convert from");
    print("Celsius to fahrenheit or");
    print("from Fahrenheit to Celsius?");
    d = input("F or C?")
    print("you entered", d)
    if (d == "F" or d == "f"): 
        f2c_conversion()
    elif (d == "C" or d == "c"): 
        c2f_conversion()
    else:
            print("please type F or C")
            conversions()

def ui_loop():
    while (1):
        a = input("do you want do another conversion (y/n)?")
        if (a == "Y" or a == "y"): 
            conversions()
        elif (a == "n" or a == "N"): 
            bye()
            break
        else:
            print("please type y or n")

def bye():
    print("goodbye.")
    k = input("press enter to close the terminal")


splash()
conversions()
ui_loop()

