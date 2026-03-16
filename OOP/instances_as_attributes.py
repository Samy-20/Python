"""We define a new class called Car_engine that doesn’t inherit from any other class. 
The __init__() method 1 has one parameter, cylinder, in addition
to self. 
This is an optional parameter that sets the no of cylinder size to 4 if no
value is provided. 
The method show_engine() has been moved to this class as well 
2.
In the Hatchback class, we now add an attribute called self.carEngine 
3.
This line tells Python to create a new instance of carEngine (with a default size of 4, because we’re not specifying a value) and assign that instance to the attribute self.carEngine. 
This will happen every time the __init__() method is called; any Hatchback instance will now have a carEngine instance created
automatically.
We create an car and assign it to the variable car_1. When
we want to describe the carEngine, we need to work through the car
"""

class Car:
    def __init__(self, model, manufacturar, year):
        self.model = model
        self.manufacturar = manufacturar
        self.year = year
        
    def discribe_car(self):
        print(f"Car model - {self.model}\nCar manufacturar - {self.manufacturar}\nCar year - {self.year}")
        

class Car_engine():
    def __init__(self, cylinder = 4):
        self.cylinder = cylinder
    
    def show_engine(self):
        print(f"These model are present no of cyliner is {self.cylinder}")
        
class Hatchback(Car):
    def __init__(self, model, manufacturar, year):
        super().__init__(model, manufacturar, year)
        self.carEngine = Car_engine()
        
car_1 = Hatchback("Polo", "Toyota", 2015)
car_1.discribe_car()
car_1.carEngine.show_engine()
    
        