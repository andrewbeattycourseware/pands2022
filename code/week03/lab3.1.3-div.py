# div.py
# program that reads in two numbers and
# outputs the integer answer and remainder
# Author: Andrew Beatty

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x/y)
remainder = x % y

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))
