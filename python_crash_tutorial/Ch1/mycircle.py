# mycircle.py
# Mimic circle() with adaptive radius.

def mycircle(radius):
    """Draw circle as polygon."""
    if radius < 20:
        sides = 10
    elif radius < 100:
        sides = 30
    else:
        sides = 50
    polygon(sides, 6.28*radius/sides)
