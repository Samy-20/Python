# self - is a parameter refrence of current class
# self is use to access the method and parameter from class


# code without using self parameter
class Myclass:
    def __init__(my, name, age):
        my.name = name
        my.age = age
    
    def output(sam):
        print('hello\t' + sam.name)
        
c1 = Myclass('sahil', 2)
c1.output()


# class Sedan:
#     def __init__(self, model, manufacturer, Engine, saftey, Boot):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.Engine = Engine
#         self.safety = saftey
#         self.Boot = Boot
        
#     def display(self):
#         print(f"Hello there these a sahil here, \n I am is talking about most famous sedans as {self.model} with boot of {self.Boot}, powerfull engine {self.Engine} and with saftey featur {self.safety}")
        
# s1 = Sedan("Verna", "Hyundai", "Turbo-charged 2.0 lit", "5 star", "528L")
# s2 = Sedan("Salvia", "Skoda", "1.5L Turbo Petrol", "5 star", "521L")

# s1.display()
# # s2.display()
