#Implement the Stack ADT in Python 

class CustomStack:
    def __init__(self):
        self.data = [] #internal storage

    def push(self,value): #push "value" into the stack
        self.data.append(value)

    def pop(self): #Remove and return the topmost item 
        if len(self.data) == 0:
            raise ValueError("Stack is Empty")
        res = self.data.pop() 
        return res 
        

    def isEmpty(self):
        return len(self.data) == 0

    def top(self):
        if len(self.data) == 0:
            raise ValueError("Stack is Empty")
        return self.data[-1]
    
    def bottom(self):
        if len(self.data) == 0:
            raise ValueError("Stack is Empty")
        return self.data[0]
    
    def push_bottom(self):
        pass #HomeWork 

    
