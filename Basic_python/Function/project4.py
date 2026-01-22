# Log function name, arguments, and result.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"function is : {func.__name__}")
        print(f"args : {args}")
        print(f"kwargs : {kwargs}")
        result = func(args, kwargs)
        print(result)
        return result
    return wrapper

@logger
def createUser(name, role):
    return f"User {name} create with role {role}"

createUser("Sam", role = "Admin")



# Output -

# function is : createUser
# args : ('Sam',)
# kwargs : {'role': 'Admin'}
# User ('Sam',) create with role {'role': 'Admin'}