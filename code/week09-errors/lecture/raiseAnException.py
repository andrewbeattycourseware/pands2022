# Demonstrate raising an exception.
# This program prompts the user for a number and
# return that number multiplied by 2
# Author: Andrew Beatty

try:
    inputVar = input('enter a number:')
    number = int(inputVar)
    if (number < 0):
        raise ValueError("negative value entered")
    print ('Number multiplied by 2 is:', number *2)
except ValueError as e:
    print ("please enter a positive number")
    print (e)