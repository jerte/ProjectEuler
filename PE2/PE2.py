###		Problem 2: Sum of even terms in Fibonacci sequence whose values 
###				   do no exceed four million ###

def iterativeFibunder(under):
	fibsum = 0
	f1 = 1
	f2 = 1
	while(f2 < under):
		temp = f2
		f2 = f1 + f2
		f1 = temp
		
		if(f2 % 2 == 0):
			fibsum = fibsum + f2
	
	return fibsum

###		Answer: 4613732

## HackerRank version

def iterative_fib_under(under):
	fibsum = 0
	f1 = 1
	f2 = 1
	while(f2+f1 < under):
		temp = f2
		f2 = f1 + f2
		f1 = temp

		if(f2 % 2 == 0):
			fibsum = fibsum + f2

	return fibsum

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	print(iterative_fib_under(n))
