# This program is to show how to make a module,  
# that contains functions, and test cases for the functions
# it has a function called fibonacci that takes in number
# and returns a list containing a fibonacci squence with that 
# many numbers
import logging
#logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number < 0:
        raise ValueError('number must be > 0')
    if number == 0:
        return []
    a = 0 
    b = 1
    fibonacciSequence = [0]
    # we have one in the list already so number - 1 times
    # this is not the most efficient code
    # yield would be a start
    for i in range(1,number):
        fibonacciSequence.append(b)
        # this is funky code make a = b and b = a + b
        a , b = b, a + b
    logging.debug("%d :%s", number, fibonacciSequence)


    return fibonacciSequence

if __name__ == '__main__':
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    logging.debug("%s", fibonacci(7))
    assert fibonacci(7) == return7, 'incorrect return value for 7'
    assert fibonacci(11) == return11, 'incorrect return value for 11'
    assert fibonacci(0) == [], 'incorrect return value for 0'
    assert fibonacci(1) == [0], 'incorrect return value for 1'
    try:
        fibonacci(-1)
    except ValueError:
        # we want this exception to be thrown
        # so this is an example where we want to do nothing
        pass
    else:
        # if the exception was not thrown we should throw an 
        # Assertion error 
        assert False, 'fibonacci should have throw a ValueError'
        # or
        #raise AssertionError("fibonacci should have thrown a value Error ")
    print("all good")
