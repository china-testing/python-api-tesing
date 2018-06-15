# guess.py
# User guesses a random number.

from random import randint

def userguess(secret):
    """Ask user for guesses until matching secret."""
    guess = int(input("Your guess? "))
    while guess != secret:
        guess = int(input("Your guess? "))
    
def main():
    secret = randint(1, 10)
    userguess(secret)

main()
