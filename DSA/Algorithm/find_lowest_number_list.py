my_array = [7, 12, 5, 8, 0, 4]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i
        
print("lowest value from array: ", minVal)
