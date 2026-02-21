# class myclass(): # class
#     x = 5 # property
    
# # p = myclass() # p - object
# # print(p.x)


# # multiple Object
# p1 = myclass()
# p2 = myclass()
# p3 = myclass()
# p4 = myclass()

# print(p1, p2, p3, p4)

# # question 

# class person:
#     def __init__(self, name, age): # without __init__ method we have to assign a values manually
#         self.name = name 
#         self.age  = age
    
#     def greet(self):
#         print(f'hello, my name is {self.name} and age is {self.age}')
        
# p1 = person('john', 20)
# p1.greet()


# class Person:
#     def __init__(self, age, name):
#         self.name = name
#         self.age = age
        
# p1 = Person(23, 'sam')
# # p2 = Person('Samy')
# print(p1.name, p1.age)

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        
    def greet(self):
        print(f"Hello, \n name - {self.name} \n age - {self.age} \n city - {self.city} \n country - {self.country}")
        
p1 = Person('sam', 20, 'nashik', 'india')
p1.greet()
