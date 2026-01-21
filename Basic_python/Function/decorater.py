# def func1(func):
#     def fun2():
#         return func().upper()
#     return fun2


# @func1 # using these decorater we can use function into other function
# def function():
#     return "Hello world"

# @func1
# def Function():
#     return "honda Civic" 

# print(function())
# print(Function())


def cars(Company):
    def innner(x):
        return Company(x).upper()

@cars
def tata(model):
    return "TATa" + model

