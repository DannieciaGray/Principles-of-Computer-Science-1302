#Anoter recursive method 
#Count Down: N N-1 ... 3 2 1 Go

def count_down(n):
    #Base case 
    if n == 0:
        print("Go")
        return


    #Recursive case 
    print(n, end=" ")
    count_down(n-1)

count_down(5)


def fact(n):
    #Base Case: When the answer is known; return it
    if n == 0:
        return 1
    

    #recursive case: when the answer is unknown;
    #however, we can break down the problem into smaller ones
    else:
        return n * fact(n-1)
    
print(fact(5))

#Fibonnaci Sequence
def fib_with_memorization(n):
    res={}
    print("Computing fib #",n)
    #Base case/cases 
    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    #Recursive case 
    #first, check if the result is already available 
    if n is res:
        return res[n]
    
    tmp = fib_with_memorization(n-1) + fib_with_memorization(n-1)
    res[n] = tmp
    return tmp
    
   

print(fib_with_memorization(50))