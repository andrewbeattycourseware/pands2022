# This is to demonstrate matplot lib
# by ploting y = x squared
# you could use seaborn
# Author: Andrew Beatty

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
