# string

# a = "Hello" # similar 'Hello'
# print(a)

# a = """        init
# PS D:\PYthon> git init
# Reinitialized existing Git repository in D:/PYthon/.git/
# PS D:\PYthon> git init 
# Reinitialized existing Git repository in D:/PYthon/.git/
# PS D:\PYthon> git add             
# Nothing specified, nothing added.
# hint: Maybe you wanted to say 'git add .'?
# hint: Disable this message with "git config advice.addEmptyPathspec false"
# """ 
# # for content we use """"""

# print(a)

# # Sclincing

# a = "Hello"
# print(a[2:4])
# print(a[2:])
# print(a[:4])
# print(a[-1])
# print(a[-5:-1])

# modify String

# a = "  hello world"

# print(a.upper())
# print(a.lower())
# print(a.strip()) # strip - use to remove all blank spaces

# print(a.replace('h', 'j')) # replace - use to replace the keyword
# print(a.split("o")) # split the string at given keyword


# Concate
# To concatenate, or combine, two strings you can use the + operator.

# a = "Civic"
# b = "Type-R"

# c = a + " " + b
# print(c)

# # Format 
# engine = 1.5
# print(f"Honda Civic type-R is come with {engine} lit engine\n")

# # Combine number and sentence

# engine = 1.5
# print(f"Honda Civic type-R is come with {engine} lit engine\n")
# print(f"Honda Civic type-R is come with {engine * 2} lit engine")
# txt = "We are the so-called \"Vikings\" from the north." # these statement allo you use "" in string
# txt = "We are the \\ so-called \"Vikings\" from the north." # these statement allo you use "" in string
# print(txt)

# a = "120000"
# print(a.isascii()) # return only ascii then true else false

# frozenset is a immutable version of sets

# a = frozenset([1, 2, 3, 4, 5])
# a.pop(2) #not been change a actual set so that is immutable
# print(a)