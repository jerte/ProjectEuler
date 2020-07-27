#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
from math import sqrt as sqrt

def isPrime(x):
	for i in range(2, int(sqrt(x)+1)):
		if x % i == 0:
			return False
	return True

def sumPrimesBelow(x):
	sum = 0
	for i in range(2, x):
		if isPrime(i):
			sum += i
	return sum

print(sumPrimesBelow(2000000))

#Answer: 142913828922
