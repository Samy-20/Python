# if else is a condition statement

# age_limit = 18
# age = 20

# if age > age_limit: # when the value of if true then only it execute the if condition 

#     print("you are elligible")
# else:
#     print("you are not elligible")

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# age = 10
# if age > 18 : print("You are elligible") 
# else: print("you are not")

# nested loop

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

username = "Emil"
password = "python123"
is_active = False

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")