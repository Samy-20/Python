# Modifying Attribute Values :- three ways to modify attributes
# 1) Modifying an Attribute’s Value Directly
# 2) Modifying an Attribute’s Value Through a Method
# 3) Incrementing an Attribute’s Value Through a Method


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}" 
    
    def milage_car(self):
        # self.milage = milage
        print(f"{self.model} distance run is {self.odometer_reading}")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
my_new_car = Car("Audi", "R8", 2010)

# 1) Modifying an Attribute’s Value Directly
# my_new_car.milage = 25 
# # my_new_car.get_descriptive_name()
# my_new_car.milage_car()

# 2) Modifying an Attribute’s Value Through a Method
# my_new_car.milage_car(25)

# 3) Incrementing an Attribute’s Value Through a Method
my_used_car = Car("Wolkswagon", "Polo", "2010")

my_used_car.increment_odometer(100)
my_used_car.milage_car()


