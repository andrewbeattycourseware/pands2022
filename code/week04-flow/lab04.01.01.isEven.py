# Program prompts the user for an number 
# and indicates if the number is odd or even
# Author: Andrew Beatty

number = int(input("enter an integer:"))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))
