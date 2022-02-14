# generate primes
# Author: Andrew Beatty

primes = []
upto = 100000

for candidate in range(2, upto):
    #print (candidate)
    isPrime = True
    # only need to check if divisable by prime
    for divisor in primes:
        # if divisable by an int it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # so there is not reason to keep checking
            break

    if isPrime:
        primes.append(candidate)

print (primes)