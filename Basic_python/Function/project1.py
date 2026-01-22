# Create a calculator that can add, subtract, multiply any number of values.

def add(*args):
    return sum(args)

def sub(*args):
    return sub(args)

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result
    
print(multiply(4, 2))