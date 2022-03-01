# adding legend and titles to lab08.08
# Author: Andrew Beatty
import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
# I prefer putting the abolute values into variables that are set at the top
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

plt.scatter(ages, salaries, label="salaries")
#plt.show() # if you do this the proram will halt here until the plot is closed

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints  # multiply each entry by itself

plt.plot(xpoints, ypoints, color='r', label = "x squared")

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
#plt.show()  # see how the axis have changed

plt.savefig('prettier-plot.png')