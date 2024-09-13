"""
This prograom will write a python class called BankAccount that manages checking and savings accounts.
The class has three attributes: a customer name,the customer's savings account balance, and the customer's 
checking account balance

Author:Danniecia Gray
"""

class Location:    
    def __init__(self, x, y):        
        self.x = x        
        self.y = y

    #TODO: write the methods here

    # checks to see if self.x is less than or equal to other.x
    def __le__(self,other):
        if self.x <= other.x and self.y <= other.y:
            res = True

        else:
            res = False 

        return res
    
    # checks to see if self.x is equal to other.x
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            res = True

        else:
            res = False 

        return res
                

        


#Driver code - no modifications are required after this line
loc1 = Location(3,4)
loc2 = Location(5,8)
print(loc1==loc2)
print(loc1<=loc2)
