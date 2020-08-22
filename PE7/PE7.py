#What is the 10001st prime number?
import math

def getnthprime(n):
    i = 1
    p = 1
    while i<=n:
        p += 1
        if isPrime(p):
            print(i, p)
            i += 1
        
    
    return p

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#print(getnthprime(10001))

#Answer: 104743

# HackerRank version

primes = [0, 2, 3]

def isprime(x):
	j=2
	while j <= int(x**.5)+1:
		if x%j==0 and x!=j:
			return False
		j+=1
	return True

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	try:
		if primes[n]:
			print(primes[n])
	except:
		i = len(primes)
		p = primes[i-1]+2
		while n>= i:
			if isprime(p):
				primes.append(p)
				i += 1
			p += 2
		print(primes[n])
