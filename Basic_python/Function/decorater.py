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


# def cars(Company):
#     def innner(x):
#         return Company(x).upper()
#     return innner

# @cars
# def tata(model):
#     return "TATa" + model

# print(("SUMO GOLD"))


def cars(n):
    def cars(models):
        def inner():
            if n == 1:
                return models().upper()
            else:
                return models.lower()
        return inner
    return cars

@cars(1)
def car_models():
    return "Honada civic type - r"

print(car_models())

