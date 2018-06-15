# conjugator.py

def conjugate(verb):
    """Return conjugation of regular -ar Spanish verbs."""
    stem = verb[:-2]
    return [stem + "o", stem + "as", stem + "a",
            stem + "amos", stem + "áis", stem + "an"]

def main():
    verb = input("Enter an -ar verb: ")
    print("Present indicative conjugation of " + verb + ":")
    for form in conjugate(verb):
        print(form)

main()
