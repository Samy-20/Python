# class Person():
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
        
#     def display(self):
#         print(self.fname, self.lname)
        
# class Student(Person):
#     def __init__(self, fname, lname, grade, year):
#         super().__init__(fname, lname)
#         self.grade = grade
#         self.graduation_year = year

#     def display(self):
#         print(f"name is {self.fname} {self.lname} i complete my graduation in {self.graduation_year} with {self.grade} grade")

# s1 = Student("sky", "herald", "A", 2000)
# p1 = Person("sam", "tyson")
# print(s1.fname, s1.lname, s1.grade, s1.graduation_year)
# s1.display()
# p1.display()



class Suv():
    def __init__(self, model):
        self.model = model
        print("Welcome Suv world!")
    
class Mahindra(Suv):
    def __init__(self, model, year, engine):
        super().__init__(model)
        self.year = year
        self.engine = engine
        
        def display(self):
            print(f"{self.model} is a brand of Mahindra lanching year {self.year} with {self.engine} cylinder engine")

suv1 = Mahindra("Scorpio N", 2000, 4)
suv1.display()