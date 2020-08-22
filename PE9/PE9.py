# PE9: Find a Pythagorean triplet (a**2 + b**2 = c**2) such that a + b + c = 1000

def findPythSumTriplet(x):
	for i in range(1,500):
		for j in range(1, 500):
			for k in range(1,500):
				if i**2 + j**2 == k**2 and i + j + k == 1000:
					return i*j*k

#print(findPythSumTriplet(1000))

#Answer: 31875000

# HackerRank version

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	
	product = -1
	for a in range(1,int(n/3)+1):
		b = (a**2 - (a-n)**2 ) / (2*(a-n))
		temp = a*b*(n-a-b) 
		if int(b) == b and temp>product:
			product = temp
			break
			
	print(int(product))
	
