# Messing with functions
# Author: Andrew Beatty

def topower(number, power = 3):
    #print (number)
    return number ** power

num = 7
answer = topower(num)
print ("cube of", num ," is", answer)

answer = topower(5, 2)
print (answer)