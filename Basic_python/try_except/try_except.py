# try:
#     x = int(input("Enter the value of x : "))
#     y = int(input("Enter the value of y : "))
#     z = x/y
#     print(z)
    
# except ZeroDivisionError:
#     print("you enter the value of y is zero, Enter the valid input")
        

# except ValueError:
#     print("gave a valid input")
    
# else:
#     print("Calculation is correct")    
     
# finally:
#     print("Execution is completed!")


# try:
#     fileName = "demo.txt"
#     f = open(fileName, 'r')
# except FileNotFoundError:
#     print("these file not exist in these directory!, Enter the valid name of file")
# else:
#     print(f.read())

try:
    l = [1,2,5,3]
    ind = int(input("Enter the index : "))
except ValueError:
    print("Enter the correct number")
except IndexError:
    print("Enter the valid index")
else:
    print(f"the number at inedx {ind} is {l[ind]}")
    