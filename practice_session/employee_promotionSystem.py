rating = float(input("Enter the your performance rating from 0.0 to 5.0 : "))
experience = int(input("Enter the experience : "))

promotion_status = 0

if experience >= 5:
    if rating >= 4.5:
        promotion_status = "promotion with high hike"
    
    elif rating < 3:
        promotion_status = "Promotion"
        
    else:
        promotion_status = "No promotion"
        
else:
    if rating >= 4.5:
        promotion_status = "promotion with high hike"
        
    else:
        promotion_status = "No promotion"
        
print(promotion_status)
        