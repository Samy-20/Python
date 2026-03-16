class Vehicle():
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
        print("these is a vehicle sector")
    
    def seating_capacity(self, capacity):
        return f"The seating capacity {self.name} is  {capacity} passenger"
    
    def fare(self, capacity):
        return capacity * 100
        
class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return super().seating_capacity(capacity)
    
    def fare(self, capacity):
        total = super().fare(capacity)
        return total + (total * 10 / 100)
    
    
v1 = Bus("Volvo bus", 120, 6)
print(v1.seating_capacity(40))
print(v1.fare(40))