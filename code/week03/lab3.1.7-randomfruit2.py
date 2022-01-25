# randomfruit2.py
# This program prints out a random fruit
# (using a tuple)
#
# There is a way to get random to pick directly from a list or tuple
# that is for another day
#
# Author: Andrew Beatty

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# we want a random number between 0 and lenght-1
index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))
