
# the with statement will atomatically close the file
# when it is finished with it

with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written
    print (data)

with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line") # returns the number of chars written
    print (data)
