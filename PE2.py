###     Problem 2: Sum of even terms in Fibonacci sequence whose values 
###                do no exceed four million ###

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

print iterativeFibunder(4000000)

###     Answer: 4613732

