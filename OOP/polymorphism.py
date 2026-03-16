# Polymorphism - single function that is used for diffrent form

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Swim")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Fly")
        
car1 = Car("Honda", "Verna")
boat1 = Boat("Lamborgini", "Yach")
plane1 = Plane("Raffle", "R15")

for x in (car1, boat1, plane1):
    x.move()