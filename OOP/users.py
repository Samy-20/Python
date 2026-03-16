"""Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user."""

class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.fname} and {self.lname} is a User")
        print(f"your login attempts {self.login_attempts}")
        
    def greet_user(self):
        print(f"Hello, I am {self.fname} {self.lname}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
# u1 = User("Sky", "Herald")
# u2 = User("sam", "ronald")
# u3 = User("Ramesh", "Shah")

# for x in (u1, u2, u3):
#     x.describe_user()
#     x.greet_user()
#     print("**************\n-----------------\n")

# u = User("Jason", "Broly")
# u.increment_login_attempts()
# u.increment_login_attempts()
# u.reset_login_attempts()
# u.describe_user()


"""An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""


class Privileges():
    def __init__(self, privileges  = ["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges       

    def show(self):
        print(f"All privilage {self.privileges}")

class Admin(User):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.privileges = Privileges()
        
        
admin = Admin("Sam", "Herald")
admin.describe_user
admin.privileges.show()
