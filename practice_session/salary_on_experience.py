"""Write a program to calculate the bonas and final salary of an aneloyee tid

Rules:
 If the employee's salary is less than on vocal te 18, est

If experience is less than 2 years, no boour is given.

If experience is between 2 and 5 years, a 10% bomo 15 gramm

If experience is ecre than 5 years, 153 bons is g

97 If the employee's salary is greater than 4,

If experience is less than 2 years, but is n

99 If experience is between 2 and 5 years, g

100 If experience is more than 5 years, a les tous is get

101 Output:

102 Display the bonus amount.

D

103 Display the final salary salary tonas"""


salary = int(input("Enter the salary : "))
exepriene  = int(input("Enter the expereience : "))
bonus = 0

if salary <= 50000:
    if 2 <= exepriene:
        bonus = 0.1*salary
        salary += bonus
    elif exepriene >= 5:
        bonus = 0.15*salary
        salary += bonus 
    else:
        print("Soory, you haven't applicable for bonus!")
        
elif salary > 50000:
    if 2 <= exepriene:
        bonus = 0.5*salary
        salary += bonus

    elif exepriene >= 5:
        bonus = 0.1*salary
        salary += bonus
    else:
        print("Soory, you haven't applicable for bonus!")
        
else: 
    print("Soory, you haven't applicable for bonus!")
        
        
print("bonus is", bonus)
print("final salary", salary) 