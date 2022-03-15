# this program is to show how you can use try except 
# Author: Andrew Beatty

#filename = 'data.txt'
import sys

#print (sys.argv)
filename = sys.argv[1]

try:
    with open(filename) as f:
        print (f.read())
    var = 10/0
except FileNotFoundError as e:
    print("file does (", filename,") does not exist", sep='')
    #print(e)


print ("the end")