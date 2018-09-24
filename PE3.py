###     Problem 3:  Largest prime factor of 600851475143
import math
def primefactors(number):
    og = number
    factors = []
    factorsMult = 1

    i = 2
    while(factorsMult!=og):
        while(number % i == 0):
            factors.append(i)
            number = number / i
        i = i + 1

        factorsMult = 1
        for factor in factors:
            factorsMult = factorsMult * factor
        
    return max(factors)

def isprime(num):
    for i in range(2, int(math.sqrt(num))):
        if(num % i == 0):
            return False
    return True

print(primefactors(600851475143))
###     Answer: 6857
