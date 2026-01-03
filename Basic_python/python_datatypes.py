# # a variable which value we assign 

# i = 1 # int datatype
# f = 2.3 # float
# s = "sam" # string
# c = 1j # complex
# # print(type(i))
# b = True


# # step to specify the data type
# i = int(1.23)
# print(i)

# f = float(1)
# print(f)

# b = bool(00)
# print(b)

#list - is can be changed/mutable

# l = list(("sam", "ramesh", "sammer"))
# l.append("rahul")
# print(l)
a = ["sam", "is", "running"]
print(type(a))

# tuple is a unmutale/canot be changed
# if we try to do change is show a error.

# t = tuple(("hello", "how", "are", "you"))
# print(t)


# # Creating a frozenset
# frozen = frozenset([1, 2, 3, 2, 1])
# print(frozen)  # Output: frozenset({1, 2, 3})

# # You can't modify it
# frozen.add(4)  # This would raise an error!

# # But you can use it as a dictionary key
# my_dict = {frozen: "some value"}  # This works!