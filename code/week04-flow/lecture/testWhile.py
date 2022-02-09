# messing with while loops
# Author: Andrew Beatty

#while condition:
#    statements

count = 0
while count < 10:
    print(count)
    count = count + 1

count = 10
while count >= 0:
    print(count)
    count -= 1
print ("blast Off")


val = input("enter something (q to quit):")
while val != 'q':
    print ("you said: " + val)
    val = input("(q to quit):")
print ("goodbye")