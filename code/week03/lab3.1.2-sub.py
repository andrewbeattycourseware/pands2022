# Program to subtract on number from another.

# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations
# author Andrew Beatty

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x-y
print("{} minus {} is {} ".format(x, y, answer))
