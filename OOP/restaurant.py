"""Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods. """

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def open_restaurant(self):
        print("Restaurant is open")
        
    def set_number_served(self, customers):
        self.number_served += customers  
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name}\n{self.cuisine_type}")
        print(f"Daily active customer count {self.number_served}")
        print("----------------------------------------------")
        
      
        
# restaurant = Restaurant("Red wine", "Room")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


"""Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance."""

# restaurant1 = Restaurant("snow white", "Massage")
# restaurant2 = Restaurant("sunsine", "Food")
# restaurant3 = Restaurant("white blue", "lauge")

# for x in (restaurant1, restaurant2, restaurant3):
#     x.describe_restaurant()

# restaurant = Restaurant("Blue star", "Pub")
# restaurant.set_number_served(20) 
# # restaurant.set_number_served(20) 
# restaurant.describe_restaurant()


"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method."""

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Mongo", "Strawberry", "Cerry"]  
        
    def show_flavors(self):
        for x in self.flavors:
            print(f"{x}")

restaurant = IceCreamStand("Redinson blue", "Food", 2)
restaurant.show_flavors()
        
