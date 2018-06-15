# dna.py

from random import choice

def complementary_base(base):
    """Return complement of single base."""
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "C":
        return "G"
    elif base == "G":
        return "C"
    return base   # leave anything else
        
def complement(dna):
    """Return complement of dna strand."""
    result = ""
    for base in dna:
        result += complementary_base(base)
    return result

def random_dna(length=30):
    """Return random strand of dna of given length."""
    fragment = ""
    for _ in range(length):
        fragment += choice("ACGT")
    return fragment
        
def main():
    dna = random_dna()
    print("Sequence  :", dna)
    print("Complement:", complement(dna))

main()
