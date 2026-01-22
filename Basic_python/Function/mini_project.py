import time

# -------------------------------
# Decorator 1: Login Check
# -------------------------------
def login_required(func):
    def wrapper(*args, **kwargs):
        logged_in = True   # simulate login
        if logged_in:
            return func(*args, **kwargs)
        else:
            print("❌ Access Denied. Please login.")
    return wrapper


# -------------------------------
# Decorator 2: Logger
# -------------------------------
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"\n🔹 Function Called: {func.__name__}")
        print(f"🔹 Args: {args}")
        print(f"🔹 Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"🔹 Result: {result}")
        return result
    return wrapper


# -------------------------------
# Function: Create User
# -------------------------------
@login_required
@logger
def create_user(*args, **kwargs):
    user = {}
    
    # args → positional values
    for index, value in enumerate(args):
        user[f"field_{index+1}"] = value

    # kwargs → key-value pairs
    for key, value in kwargs.items():
        user[key] = value

    return user


# -------------------------------
# Function: Display User
# -------------------------------
@login_required
@logger
def display_user(**user_data):
    print("\n👤 User Details")
    for key, value in user_data.items():
        print(f"{key} : {value}")


# -------------------------------
# Function: System Stats
# -------------------------------
@login_required
@logger
def system_stats(*args):
    print("\n📊 System Stats")
    for stat in args:
        print(f"- {stat}")
    return "Stats Displayed"


# -------------------------------
# Main Execution
# -------------------------------
user_data = create_user(
    "UID102",
    "Active",
    name="Rahul",
    age=21,
    role="Admin"
)

display_user(**user_data)

system_stats("Users: 120", "Active: 95", "Inactive: 25")
