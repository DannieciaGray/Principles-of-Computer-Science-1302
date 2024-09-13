# Multiple Inheritance 

class Vehicle:
    def __init__(self):
        self.name = "Vehicle"

class Airplane:
    def __init__(self):
        self.make = "Boeing"

class FlyingCar(Vehicle,Airplane):
    def __init__(self):



#MUltilevel Inheritance
#Constructor Chaining 

class Vehicle:
    def __init__(self, make, weight):
        self.make = make

class Car(Vehicle):
    def __init__(self, model, make, year):
        self.model = model
        Vehicle.__init__(make)

class SUV(Car):
    def __init__(self, numCylinder,model,make):
        Car .__init__(self,model,make)
        self.num_cylinders = 4


#Starting point:
suv1 = SUV(numCylinder: 4, model: "Avalon",make:"Toyota")




#Hierarchical Inheritance

class Vehicle:
    def __init__(self):
        self.make = "Toyota"

    def print_vehicle_make(self):
        print(self.make)



class Car(Vehicle):
    def __init__(self,num_cylinders):
        Vehicle. __init__(self)
        self.num_cylinders = num_cylinders



class Truck(Vehicle):
    def __init__(self,cargoCapacity):
        Vehicle. __init__(self)
        self.cargoCapacity = cargoCapacity


car1 = Car(4)
truck1 = Truck(100)
car1.print_vehicle_make()
truck1.print_vehicle_make()


#Hybrid Inheritance





