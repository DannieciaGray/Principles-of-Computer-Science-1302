"""
This prograom will write a python class called BankAccount that manages checking and savings accounts.
The class has three attributes: a customer name,the customer's savings account balance, and the customer's 
checking account balance

Author:Danniecia Gray
"""

class BankAccount:
    def __init__(self,name,checking_balance,savings_balance):
        self.customer_name = name
        self.savings = savings_balance
        self.checking = checking_balance

    def deposit_checking(self,amount):
        # add parameter amount to checking account balance (only if positive)

        if amount > 0:
            self.checking = self.checking + amount

        return self.checking

    def deposit_savings(self,amount):
        # add parameter amount to savings account balance (only if positive)

        if amount > 0:
            self.savings += amount

        return self.savings


    def withdraw_checking(self,amount):
        # subtract parameter amount from checking account balance (only if positive)

        if amount > 0:
            self.checking-= amount
            
        return self.checking

    def withdraw_savings(self,amount):
        # subtract parameter amount from savings account balance (only if positive)

        if amount > 0:
            self.savings -= amount
        return self.savings

    def transfer_to_savings(self,amount):
        # subtract parameter amount from checking account balance and add to savings account balance (only if positive)

        if amount > 0:
            self.checking -= amount
            self.savings += amount 

        return self.savings

#Demo code
account = BankAccount("Mickey", 500.00, 1000.00)    
account.checking = 500    
account.savings = 500    
account.withdraw_savings(100)    
account.withdraw_checking(100)    
account.transfer_to_savings(300)    
#print(account.name)    
print(f'${account.checking:.2f}')    
print(f'${account.savings:.2f}')


    
