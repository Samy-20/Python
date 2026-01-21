# function is a block of code that run when it call

# def function():
#     print("You are running function")

# function()

# passing variable in funnction called as arguments

# def Profile(age, name): 
#     print(F'My name is {name} and age is {age}')

# # age = input(int("Enter your age"))
# age = 20
# Profile(age, "sam")

# # adding two number with function

# def add(num1, num2):
#     c = num1 + num2
#     return c

# sum = add(1, 2)
# print(sum)


# # '*,' is used keyword only parameter
# def my_function(*, name):
#   print("Hello", name)

# my_function(name = "sam")


# # ',/' is used keyword without parameter
# def my_function(name, /):
#   print("Hello", name)

# name = "sam"
# my_function(name)


# scope
# two types are global and local scope

# # global scope
# def employee():
#     print(f"Employee age: {emp_age}")

# emp_age = 20
# employee()
# print(emp_age)


# # local scope
# def employee():
#     age = 20
#     print(f"Employee age: {age}")

# employee()
# # print(age) # cannot access the age because it present in function

# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x # if i remove these nonlocal it cannot access the x varible(gave a error)
#     print(x)
#     x = "hello"
#     print(x)
#   myfunc2()
#   return x

# print(myfunc1())


x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)