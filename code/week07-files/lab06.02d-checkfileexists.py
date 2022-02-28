import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("File does not exist")
    #initialise file here