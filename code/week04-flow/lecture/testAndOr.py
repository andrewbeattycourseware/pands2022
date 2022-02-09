# messing with ands and ors
# Author: Andrew Beatty

number = -1
if ( number >=0 ) and ( number <= 100) :
    print("valid")

if (number <= 0) or (number >= 100 ) :
    isbad = True
    print("stop")
else:
    isbad = False
    print("go")