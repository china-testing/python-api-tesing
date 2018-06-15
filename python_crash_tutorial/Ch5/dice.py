# dice.py

from random import randint

class Dice:
    def __init__(self, n):
        self.dice = [Die() for _ in range(n)]
        
    def rollall(self):
        for die in self.dice:
            die.roll()

    def values(self):
        return [int(die) for die in self.dice]
    
    def __str__(self):
        return str(self.values())

class Die:
    def __init__(self):
        self.value = randint(1, 6)
        
    def roll(self):
        self.value = randint(1, 6)
        
    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

def main():
    dice = Dice(5)
    dice.rollall()
    print(dice)

if __name__ == "__main__":
    main()
