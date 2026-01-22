# Allow function execution only if user is logged in.

def login_required(func):
    def wrapper():
        logged_in = False
        if logged_in:
            func()
        else:
            print("You haven't login, so first logined in!")
    return wrapper

@login_required
def dashboard():
    print("Welcome to dashboard!")

dashboard()