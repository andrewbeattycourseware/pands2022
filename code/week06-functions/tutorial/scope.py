# demonstrate scope


var = 3

def fun(var):
    #global var
    
    print ("in function ", var)
    if (True):
        print ("in if", var)

print ("global", var)
fun(20)
print ("global", var)