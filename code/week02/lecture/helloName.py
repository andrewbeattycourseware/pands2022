# Uses a variable to greet
# Author: Andrew Beatty

name = "Andrew"
print ('hello ' + name )

# this won't work
age = 34
#print ('Your age is ' + age)
print ('your age is ' + str(age))
print ('Hello {} \tYour age is {}'.format(name, age))