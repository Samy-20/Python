# # tuples

# # # Tuple immutable hota hai, isliye methods bahut kam hote hain.

# t = (1,2,4,6,7,3,8)

# # print(type(t))
# print(t.count(1))
# print(t.index(7))
# print(sum(t))


# # convert tuple to list add new data then again convert to list to tuple

# Suv = ("Defender", "Cadillac", "G-Wagon", "Jimmy", "Range Rover Evoque")

# Off_Road = list(Suv)
# print(type(Off_Road))   
# Off_Road.append("Land Cruiser")

# Suv = tuple(Off_Road)
# print(type(Suv))
# print(Suv)


# # Unpack Tuples

# car = ("Polo", "Aulto", "Tigor")
# (wolkwagon, Suzuki, tata) = car # pack the variable of these with same posiition variable of above Tuple

# print(wolkwagon)


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# Loop in tuples

car = ("Polo", "Aulto", "Tigor", "Verna", "Virtus", "Cevorlet")
count = 0


for x in range(len(car)):
    print(car[x])
    count += 1

print(f"Total count of car: {count}")