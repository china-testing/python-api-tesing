# find.py
# Find an item in a list

def find(target, items):
    """Return first index of target in items or -1."""
    for i in range(len(items)):
        if target == items[i]:
            return i
    return -1
