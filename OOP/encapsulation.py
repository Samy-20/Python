class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        
    
    
    def _validate(self, age):
        if self._age > 60:
            return True
        else:
            return False
        
    def get_age(self):
        return self._age
        
    def set_age(self, age):
        if self._validate(age):
            print("You are over aged")
        elif self._age < 0:
            print("Enter the valid age")
        else:
            print("you are elligible")
            
p1 = Person("Sam", 80)
# print(p1.name)
# print(p1._age)

print(p1.set_age(22))
print(p1.get_age())




