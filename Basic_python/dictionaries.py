# # dictionaries is a mutable
# # dict = ["keys" : "values"]

# car_dict = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year" : 1995,
#     "year" : 1996 # duplicate are not allowed in dict
# }

# print(car_dict["brand"]) # Access the items from dict

# print(car_dict.get("model"))
# print(car_dict.keys())
# print(car_dict.values())

# # car_dict["model"] =  1996 # dict are mutable
# # print(car_dict)

# # update method
# car_dict.update({"year" : 1996})
# print(car_dict)

# # addition of new items in dict
# car_dict.update({"gear set" : "Automatic"})
# print(car_dict)

# # remove methods
# # # 1. pop
# # car_dict.pop("gear set")
# # print(car_dict)

# # # 2. popitem
# # car_dict.popitem()
# # print(car_dict)

# # # 3. del
# # del car_dict["gear set"]
# # print(car_dict)

# # loop in dict
# for x in car_dict.items():
#     print(x)


# # copy dictionaries
# muscle_car = car_dict.copy()
# print(f"\n{muscle_car}\n")
# muscle_car.update({"fuel" : "petrol"})

# nested dictionaries

sedan = {
    "Virtus" : {
        "Brand" : "Wolkswagon",
        "engine" : "1.5li",
        "cylinder" : 4
    },
    "M8" : {
        "Brand" : "BMW",
        "engine" : "4.0li",
        "cylinder" : 8
    },
    "Accord" : {
        "Brand" : "honda",
        "engine" : "2.0li",
        "cylinder" : 4
    }
}

print(f"\n{sedan}\n")

print(f"{sedan["Accord"]}\n")

print(sedan["Virtus"]["Brand"])
