# mymin.py
# Find smallest element of a list

def mymin(items):
    """Return smallest element in items."""
    smallest = items[0]
    for item in items[1:]:
        if item < smallest:
            smallest = item
    return smallest
