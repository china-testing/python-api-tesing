# balance_table_format.py
# Print table of account balances earning interest.

def balance(p, r, t):
    """Return new balance using compound annual interest."""
    return p*(1 + r)**t

def main():
    print("Calculates compound interest over time.")
    principal = float(input("Principal: "))
    rate = float(input("Interest rate (as a decimal): "))
    years = int(input("Number of years: "))
    for year in range(years + 1):
        amt = balance(principal, rate, year)
        print(year, amt)
    for year in range(years + 1):
        amt = balance(principal, rate, year)
        print("{:3d}   ${:>7.2f}".format(year, amt))
    
main()
