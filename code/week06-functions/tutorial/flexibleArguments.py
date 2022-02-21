# messing with flexible arguments

def average(*numbers):
    sumOfNums = sum(numbers)
    return sumOfNums / len(numbers)

print (average(2, 4, 6, 8, 10))

def storeValues (**obj):
    print (obj)

storeValues(name= "joe", age = 33)