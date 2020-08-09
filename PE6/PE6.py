#Find the difference between the sum of the squares 
#of the first one hundred natural numbers and the square of the sum.

def sumosquares(numlist):
    sums = 0
    for i in numlist:
        sums += i * i
    return sums

def squareosum(numlist):
    sums = 0
    for i in numlist:
        sums += i
    return sums * sums
'''
first100 = [i for i in range(1,101)]
print(sumosquares(first100))
print(squareosum(first100))
print(squareosum(first100) - sumosquares(first100))
'''
# Answer: 25164150

# HackerRank version

def sum_squares(n):
	sum = n*(n+1)*(2*n+1)/6
	return sum

def square_sum(n):
	sum = n * (n+1) / 2
	return sum**2

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	print(int(square_sum(n) - sum_squares(n)))
