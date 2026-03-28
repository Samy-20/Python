""" 1) take salry < 50000 -> 20%inc or no incr"""


# salary = int(input("Enter salary : "))

# if salary <= 50000:
#     salary += salary * 0.2
#     print(salary) 
    
# else:
#     print("No Increment!")
    
    
""" 2) if salary < 20000 -> 20% inc, salary < 40k -> 15%, salary < 80k -> 10%, 80k < salary -> 5%"""

salary = int(input("Enter salary : "))

if salary <= 20000:
    salary += salary * 0.2
    print(salary) 

elif salary <= 40000:
    salary += salary * 0.15
    print(salary) 

elif salary <= 80000:
    salary += salary * 0.1
    print(salary) 
    
elif salary > 80000:
    salary += salary * 0.05
    print(salary) 
    
else:
    print("No Increment!")
