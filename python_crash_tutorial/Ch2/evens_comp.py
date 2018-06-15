# evens_comp.py
# Find even values in a list of numbers using list comprehension

def evens(items):
    """Return list of even values in items."""
    return [item for item in items if item % 2 == 0]
