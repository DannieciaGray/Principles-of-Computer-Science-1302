import math

class Location:
    #TODO: Implement the Location class according to the given UML class diagram and descriptions
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ","+str(self.y) + ")"

class Car:
    #TODO: Implement the Car class according to the given UML class diagram and descriptions
    def __init__(self,name,location,cost):
        self.name = name
        self.location = location
        self.cost = cost

    def __str__(self):
        return "[" + str(self.name) + "," + str(self.location) + "," + str(self.cost) +"]"

    def move_to(self,new_x,new_y):
        self.new_x = new_x 
        self.new_y = new_y
    
class Passenger:
    #TODO: Implement the Passenger class according to the given UML class diagram and descriptions
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def __str__(self):
        return "[" + str(self.name) + "," + str(self.location) + "]"
    
    def move_to(self,new_x,new_y):
        self.new_x = new_x 
        self.new_y = new_y

class RideSharingApp:
    #TODO: Implement the RideSharingApp class according to the given UML class diagram and descriptions
    def __init__(self,cars = [],passengers = []):
        self.cars = cars
        self.passengers =passengers

    def add_car(self,car):
        #Adds the given car object to the cars attribute
        cars = self.cars

        cars.append(car)

    def add_passenger(self,passenger):
        #Adds the given passenger object to the passenger attribute
        passengers = self.passengers

        passengers.append(passenger)

    def remove_car(self,car):
        #Removes the given car object from the car attribute
        cars = self.cars

        cars.pop(car)
        
    def remove_passenger(self,passenger):
        #Removes the given passenger object from the passenger attribute
        passengers = self.passengers
        
        passengers.pop(passenger)
    
    def find_cheapest_car(self):
        #Finds the cheapest car and prints the string representation of that car
        if self.cars:
            cheapest_car = min(self.cars, key = lambda car: car.cost)
            print(f"Cheapest car available: {cheapest_car.name}, Cost per mile: {cheapest_car.cost}")
        
        else:
            print("No cars available")

    def find_nearest_car(self,passenger):
        if not self.cars:
            print("No cars available.")
            return 
        
        nearest_car = None
        min_distance = 10000000

        #Gets passenger location
        passenger_x = passenger.location.x
        passenger_y = passenger.location.y


        for car in self.cars:
            car_x = car.location.x
            car_y = car.location.y

            #Calculates the distance between the passenger and the car
            distance = math.sqrt((car_x - passenger_x) ** 2 + (car_y - passenger_y) ** 2)
            
            if distance < min_distance:
                min_distance = distance
                nearest_car = car

            if nearest_car:
                 print(f"Nearest car for {passenger.name}: {nearest_car.name}, Distance: {min_distance:.2f}")
        

    

#For the remaining code (after this line), no modification is required
print('---------------------Object Creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)

mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)

print('-----------------------Scenario 1---------------------')
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 2---------------------')
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 3---------------------')
car3= Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

