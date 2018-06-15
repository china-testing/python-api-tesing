# evens.py
# Find even values in a list of numbers.

def evens(items):
    """Return list of even values in items."""
    result = []
    for item in items:
        if item % 2 == 0:
            result += [item]
    return result
