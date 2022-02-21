# messing with functions

#print ("hello", 33, True, end=" ", sep=":")
#print ("fin")


def multiply(arg1 = 0, arg2 = 0):
    if arg2 == 0:
        return 0
    print ("calculating...")
    return arg1 * arg2

ans =  multiply(arg2 = 2)
print (ans)