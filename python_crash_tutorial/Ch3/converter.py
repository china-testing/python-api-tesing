def digit_to_int(digit):
    """Return int corresponding to string digit."""
    return ord(digit) - 48

def decimal_to_int(digits):
    """Return int corresponding to decimal string."""
    result = 0
    for digit in digits:
        result = 10 * result + digit_to_int(digit)
    return result
