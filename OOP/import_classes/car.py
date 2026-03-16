class Car:
    def __init__(self, model, company):
        self.model = model
        self.company = company
        
    def show_car(self):
        print(f"Car name is a {self.model} manufacturar by {self.company}")
        
        