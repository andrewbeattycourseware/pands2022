# more messing with functions
# variable scope
# Author: Andrew Beatty
x = 7

def topower(number, power=3):
    global x
    print ("in function x is", x)
    x = 3
    return number ** power

topower(4)
print("outside fun x is", x)
