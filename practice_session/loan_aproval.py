

salary = int(input("Enter Your current salary : "))
credit_score = int(input("Enter Your current credit score : "))
loan_status = 0
condition = 0

if salary >= 30000:
    if credit_score >= 750:
        loan_status = 1
    
    elif credit_score >= 600:
        loan_status = 1
        condition = 1
    
    else:
        loan_status = 0
        
else:
    if credit_score >= 750:
        loan_status = 1
    
    else:
        loan_status = 0
        
if loan_status == 1 and condition == 1:
    print("loan approve with condition")
    
elif loan_status == 1:
    print("Loan Approve")
    
else:
    print("loan is not Approve")