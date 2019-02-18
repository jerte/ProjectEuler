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
    for i in range(8*start/10, start):
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

print(largepalprod(3))

## Answer: 906609
