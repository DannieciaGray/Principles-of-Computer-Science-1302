def is_prime(n):
    #check if number is greater than 1
    if n > 1:
        i = 2
         #use while to 
        while i != n:
              #checking if theres another number other than itself that n is divisible by  
              if n % i == 0 :
                   return False
              
              i+=1
        return True 
              

    return False
    
   
print(is_prime(5))
print(is_prime(11))
print(is_prime(9))
