# chuck.py

from dice import Dice

class ChuckALuck:
    """Play the game Chuck-a-Luck."""
    def __init__(self):
        self.dice = Dice(3)
        self.score = 0

    def play_once(self, guess):
        """Roll dice and update score based on guess."""
        self.dice.rollall()
        print("The roll:", self.dice)
        matches = self.dice.values().count(guess)
        score = matches if matches > 0 else -1
        print("Score:", score)
        self.score += score
        
    def play(self):
        """Allow user to repeatedly guess."""
        print("Welcome to Chuck-A-Luck")
        guess = int(input("Guess 1-6 (0 to stop): "))
        while guess != 0:
            self.play_once(guess)
            print("Current total:", self.score)
            guess = int(input("Guess 1-6 (0 to stop): "))
        print("Thanks for playing.")
        
def main():
    game = ChuckALuck()
    game.play()

if __name__ == "__main__":
    main()
