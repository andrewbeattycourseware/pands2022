# plottask.py
# This program  displays a plot of the functions in specific range on the one set of axes.
# Author: Fatima Zeino

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(0, 4))

fpoints = xpoints
plt.plot(xpoints, fpoints, color='g', label="f(x)")

gpoints = xpoints * xpoints
plt.plot(xpoints, gpoints, color='b', label="g(x)")

hpoints = xpoints * xpoints * xpoints
plt.plot(xpoints, hpoints, color='r', label="h(x)")

plt.title("Functios")
plt.xlabel("X")
plt.ylabel("(X)=Y")
plt.legend()
#plt.show()
plt.savefig('functios-plot.png')

