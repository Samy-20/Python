"""class Outer:
    def __init__(self):
        self.name = "Outer class"
        
    class Inner:
        def __init__(self):
            self.name = "Inner class"
        
        def display(self):
            print(self.name)
    
outer = Outer()
inner = Outer().Inner()
print(outer.name)
print(inner.name)

inner.display()"""


# Multiple inner class

class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()
    
    class CPU:
        def processing(self):
            print("Processing data")
        
    class RAM:
        def store(self):
            print("Storing data")
            
computer = Computer()
computer.cpu.processing()
computer.ram.store()