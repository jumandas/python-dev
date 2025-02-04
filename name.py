#sys stands for system
#sys.argv (argument vector)
#passing input while running the argument (command line argument)
#python name.py Juman
#sys.argv[0] will print the name of the filte
#sys.argv[1] will be an input during the command line argument

import sys
try:
    print("hello , my name is", sys.argv[1])
except IndexError:
    print("too few arguments")


#Another way of executing arguments

import sys

if len(sys.argv) < 2:
    print("Too Few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello my name is" , sys.argv[1])

#David is valid input 
#"David Malan" is valid input
#David Malan is invalid input
#no input is invalid input
