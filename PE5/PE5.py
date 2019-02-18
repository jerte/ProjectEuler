# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

import math

def multiplelcm(numlist):
    primefactors = factorslist(numlist)
    lcm = {}
    for i in primefactors:
        for j in i:
            multiplicity = sum([x==j for x in i])
            if (j in lcm.keys()):
                if multiplicity > lcm[j]:
                    lcm[j] = multiplicity
            else:
                lcm[j] = multiplicity
    
    val = 1
    for i in lcm.keys():
        val = val * math.pow(i,lcm[i])
    return val

def factorslist(numlist):
    numfactors = []
    for i in numlist:
        numfactors.append(factors(i))
    return np.asarray(numfactors)

def factors(num):
    factors = []
    if num == 1:
        return [1]
    i = 2
    while num!=1:
        if num % i == 0:
            num = num / i
            factors.append(i)
        else:
            i = nextprime(i)
    return factors

def nextprime(x):
    x += 1
    while ( not isPrime(x) ):
        x += 1
    return x

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print multiplelcm( [i for i in range(1,21)] )
# Answer: 232792560



