# messsing with the os module
# Author Andrew Beatty

import os

filename = 'test.txt'
if os.path.exists(filename):
    print(filename, "already exists")
    os.remove(filename)
else:
    print(filename, "does not exist do you want to create it?")


