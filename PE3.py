###     Problem 3:  Largest prime factor of 600851475143
import math

def primefactors(number):
    og = number
    factors = {}
    factorsMult = 1

    i = 2
    lastPrime = 2
    while(factorsMult!=og):
        while(number % i == 0):
            if i in factors:
                factors[i] = factors[i] + 1
            else:
                factors[i] = 1
            number = number / i

        factorsMult = 1
        for factor in factors:
            factorsMult = factorsMult * math.pow(factor,factors[factor])
        
        lastPrime = i
        i = nextPrime(i)
    return max(factors)

def nextPrime(num):
    num = num + 1
    while( not isPrime(num)):
        num = num + 1
    return num

def isPrime(num):
    for i in range(2,int(math.sqrt(num))):
        if( num % i == 0 ):
            return False
    return True

print(primefactors(600851475143))
###     Answer: 6857
