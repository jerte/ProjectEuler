###		Problem 3:	Largest prime factor of 600851475143
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

###		Answer: 6857

## HackerRank version

import sys
import math

def is_prime(num):
	for i in range(2,int(math.sqrt(num))+1):
		if( num % i == 0 ):
			return False
	return True

def largest_prime_under(n):
	if is_prime(n):
		return n
	else:
		finder = int(n/2)+1
		stopper = True
		while( stopper ):
			if is_prime(finder) and n % finder==0:
				stopper = False
			else:
				finder -= 1
		return finder

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	print(largest_prime_under(n))
