from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_dice(self):
        output = randint(1,6)
        print(f"Your output is :- {output}")
        
        
dice1 = Dice()
dice1.roll_dice()