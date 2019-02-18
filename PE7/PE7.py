#What is the 10001st prime number?
import math

def getnthprime(n):
    i = 1
    p = 1
    while i<=n:
        p += 1
        if isPrime(p):
            print i, p
            i += 1
        
    
    return p

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print getnthprime(10001)

#Answer: 104743
