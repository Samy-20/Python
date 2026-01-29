# x = lambda a : a + 10
# print(x(5))

# def fibonaci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonaci(n-1) + fibonaci(n-2)
    
# fibonaci(7)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
# print(type(numbers))
# print(type(odd_numbers))

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)