#sys stands for system
#sys.argv (argument vector)
#passing input while running the argument (command line argument)
#python name.py Juman
#sys.exit will exit the program
#sys.argv[0] will print the name of the file
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
#David Malan is invalid input
#no input is invalid input


# proper way of handling the sys.argv with sys.exit
import sys

#check for errors
if len(sys.argv) < 2:
    sys.exit("Too Few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("hello my name is" , sys.argv[1])
    
# David is valid input 
# David Malan is invalid input
#no input is invalid input
# even "David Malan" is a valid input , need to check with double quotes
