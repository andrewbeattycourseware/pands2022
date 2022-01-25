# Give the absolute value of a number
# 
# Author: Andrew Beatty

# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float
number = float(input("Enter a number:"))

absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))
