# wordlist.py

from string import punctuation

def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s

def wordlist(text):
    """Return list of words in string."""
    return remove_punctuation(text).split()

def main():
    examples = ["Is this a good example?",
                "Yes, of course it is!",
                "Ok - thanks."]
    for text in examples:
        print(wordlist(text))

main()
