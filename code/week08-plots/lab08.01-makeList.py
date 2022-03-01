# This is just to show you numpy exists
# Author: Andrew Beatty

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

# add 5000 to each entry
salariesPlus = salaries + 5000
print(salariesPlus)

# you can also multiply 
salariesMult = salaries * 1.05 # add 5% by mulitplying by 1.05
print(salariesMult)
# this is a float array to convert to an int array
newSalaries = salariesMult.astype(int)
print(newSalaries)