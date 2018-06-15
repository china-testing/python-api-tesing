# speller2.py

def contents(filename):
    """Return contents of text file as string.

    Args:
        filename - name of file
    Returns:
        contents of file as one string
    Raises:
        OSError if error opening or reading file
    """
    with open(filename) as f:
        return f.read()
        
def main():
    try:
        validwords = contents("dictioary.txt").split()
    except OSError as err:
        print(err)
        print("Stopping, unable to read dictionary file.")
        return
    word = input("Enter a word: ")
    if word.lower() in validwords:
        print("Looks ok")
    else:
        print("Not in this dictionary")

main()
