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

# Answer: 232792560

## HackerRank version

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def next_prime(n):
	if n==2:
		return 3
	n += 2
	while (not is_prime(n)):
		n += 2
	return n

def prime_factorization(n):
	if n == 1:
		return [n]
	prime_f = []
	i = 2
	while( n != 1 ):
		if n % i ==0:
			prime_f.append(i)
			n /= i
		else:
			i = next_prime(i)
	return prime_f

def make_min_count_dict(list_o_lists):
	d = {}
	for i in list_o_lists:
		temp_count = {}
		for j in i:
			if j in temp_count.keys():
				temp_count[j] += 1
			else:
				temp_count[j] = 1
		for j in temp_count.keys():
			if (j in d.keys() and temp_count[j] > d[j]) or j not in d.keys():
				d[j] = temp_count[j]
	return d

def smallest_multiple(n):
	primes = []
	for i in range(1, n+1):
		primes.append(prime_factorization(i))
	prime_count = make_min_count_dict(primes)
	sm = 1
	for i in prime_count.keys():
		sm *= i**prime_count[i]
	return sm

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	print(smallest_multiple(n))

