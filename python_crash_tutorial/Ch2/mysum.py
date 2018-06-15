# mysum.py

def mysum(items):
    """Return sum of values in items."""
    total = 0
    for item in items:
        total += item
    return total

def main():
    data = [4, 9, 2, 8, 3, 2, 5, 4, 2]
    print("My sum of", data, "is", mysum(data))

main()
