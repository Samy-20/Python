# # *args
# def add_numbers(*args):
#     print(args)
#     print(type(args))
#     return sum(args)

# print(add_numbers(1, 2, 3, 4))


# **kwargs
def add_numbers(**kwargs):
    print(kwargs)
    print(type(kwargs))

    # for i in kwargs:
    #     print(i)    

add_numbers(name = "SAM", Age = "22")