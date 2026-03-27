# def is_power_of_three(n):
#     if n <= 0:
#         return False
#     while n % 3 == 0:
#         n //= 3
#     return n == 1

# # Example usage
# number = int(input("Enter a number: "))
# if is_power_of_three(number):
#     print(f"{number} is a power of 3.")
# else:
#     print(f"{number} is not a power of 3.")

# l = [1,2,34]

# for x in l:
#     print(x + 2)

# import gc

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# a = Node(1)
# b = Node(2)

# # Create circular reference
# a.next = b
# b.next = a

# del a
# del b

# print("Garbage Collector collects:", gc.collect())


# a = []
# b = [a]
# a.append(b)
# print(gc.collect())



# import gc 
# x = [1,2,4]
# # y = (x)
# # del x
# # print(y)
# print(gc.collect())


# import sys 

# a = 10**10
# print(sys.getsizeof(a))

# def function(func):
#     print("helow")
#     return func()
    
        
# @function
# def func1():
#     print("hey hi")
    
# func1()
    
    
# a = [1,4,23,3]
# x, *y, z = a
# print(x, y, z)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = []

# print(sum(nums))

# s = filter(lambda x : x**3 > 100, nums)
# print(list(s))



# import gc
# import sys
# a = [1,2,3,4]
# b = [a]

# print(sys.getrefcount(a))

# generational_count


    # from functools import reduce
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # result = reduce(lambda x, y : x + y, map(
    #     lambda x : x*x,
    #     filter(lambda x : x % 2 == 0, nums)
    # ))

    # print(result)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared = map(lambda x : x * x, nums)
# print(squared)    

# even = list(filter(lambda x : x % 2 == 0, nums))
# print(even)

from functools import reduce
# sum_of = reduce(lambda a, b : a + b, nums)
# print(sum_of)

# result = reduce(lambda x, y : x + y, map(lambda x : x * x, filter(lambda x : x % 2, nums)))
# print(result)

result  = list(sum(lambda x, y : x + y, filter(lambda x : x % 2 == 0, nums)))