def Car(car1):
    def wrapper():
        car1()
        print("The car model")
    return car1

@Car
def car1():
    print("BMW M5 with 2.5lit engine")
    
car1()