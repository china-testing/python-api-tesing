# speller.py

def contents(filename):
    """Return contents of text file as string."""
    with open(filename) as f:
        return f.read()

def main():
    validwords = contents("dictionary.txt").split()
    word = input("Enter a word: ")
    if word.lower() in validwords:
        print("Looks ok")
    else:
        print("Not in this dictionary")

main()
