# Messsing with numpy
# Author: Andrew Beatty
import numpy as np

listOfNumbers = [1,2,3,6]
numbers = np.array([1,2,4,5])

#listOfNumbers = listOfNumbers + 3
numbers = numbers * np.array([1,4,5,6])

print (listOfNumbers)
print (numbers)

randomNumbers = np.random.normal(size = 100)
print (randomNumbers)