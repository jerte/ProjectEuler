# Find the largest palindrome made from the product of two 3-digit numbers.
import math

def largepalprod(digits):
	start = 0
	for i in range(0,digits):
		if(i==0):
			start += 9
		else:
			start += 9 * math.pow(10,i)
	start = int(start)
	start2 = start

	pals = []
	for i in range(int(8*start/10), start):
		for j in range(8*start2/10,start2):
			if( isPal(i,j) ):
				pals.append( (i,j,i*j) )
		
	prods = [i[2] for i in pals]
	return max(prods)
		

def isPal(num1,num2):
	prod = num1*num2
	prod = str(prod)
	for i in range(0,len(prod)):
		if(prod[i] != prod[len(prod)-i-1]):
			return False
	return True

## Answer: 906609

## HackerRank version

def isPalh(num):
	prod = str(num)
	return prod == prod[::-1]

def isThreeDigProduct(n):
	i = 999
	while( i > 100 ):
		if n % i == 0:
			j = int(n / i / 100)
			if j < 10 and j > 0:
				return True
		i -= 1
	return False

def largest_palindrome_product_under_N(N):
	cur = N-1
	pal_products = set()
	while( cur > 101100 ):
		if isPalh(cur) and isThreeDigProduct(cur):
			return cur
		cur -= 1
	
	return 101101

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	print(largest_palindrome_product_under_N(n))
