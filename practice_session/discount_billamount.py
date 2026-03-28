"""asking user for billl amount 5000 more appply 10% disount"""

# bill_amount = int(input("Enter the bill amount"))

# if bill_amount > 5000:
#     discount = 0.1 * bill_amount
#     bill_amount -= discount
#     print(bill_amount)

# else:
#     print("no discount")
    
    
"""if 2000<bill_amount<4000 then 5% discount, 4000<=bill<8000 -> 10%, 8000<bill<12000 15%, 12000< bill<15000 -> 20%, 15000<bill 20%"""

bill_amount = int(input("Enter the bill amount: "))

if 2000 <= bill_amount:
    discount = 0.05 * bill_amount
    bill_amount -= discount
    print(bill_amount)

elif 4000 <= bill_amount:
    discount = 0.1 * bill_amount
    bill_amount -= discount
    print(bill_amount)
    
elif 8000 <= bill_amount:
    discount = 0.15 * bill_amount
    bill_amount -= discount
    print(bill_amount)
    
elif 12000 <= bill_amount:
    discount = 0.20 * bill_amount
    bill_amount -= discount
    print(bill_amount)
    
elif 15000 <= bill_amount :
    discount = 0.25 * bill_amount
    bill_amount -= discount
    print(bill_amount)
    

else:
    print(f"no discount, amount {bill_amount}")