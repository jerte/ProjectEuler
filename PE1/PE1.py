###     Problem 1:  Sum of all multiples of 3 or 5 under 1000 ###

def multiplesSum(multiples,under):
    sum1 = 0
    for i in range(1,under):
        for multiple in multiples:
            if(i % multiple == 0):
                sum1 = sum1 + i
                break
    return sum1

###     Answer: 233168

## HackerRank version

import sys

def sum_3n5_multiples_under_n(n):
	threes = int((n-1)/3)
	fives = int((n-1)/5)
	lcm = int((n-1)/15)
	
	return int(3*i_to_n_sum(threes) + 5*i_to_n_sum(fives) - 15*i_to_n_sum(lcm))

def i_to_n_sum(n):
	return n*(n+1) >> 1
	
t = int(input().strip())
for i in range(t):
	n = int(input().strip())
	print(sum_3n5_multiples_under_n(n))

