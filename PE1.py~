###     Problem 1:  Sum of all multiples of 3 or 5 under 1000 ###

def multiplesSum(multiples,under):
    sum1 = 0
    for i in range(1,under):
        for multiple in multiples:
            if(i % multiple == 0):
                sum1 = sum1 + i
                break
    return sum1

print multiplesSum([3,5],1000)

###     Answer: 233168
