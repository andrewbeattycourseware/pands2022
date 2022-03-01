# messing with matplotlib
# Author: Andrew Beatty

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label= "xsquared")
plt.plot(xpoints, xpoints, label="straight", color="blue")
plt.legend()

randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label="random")

plt.show()

