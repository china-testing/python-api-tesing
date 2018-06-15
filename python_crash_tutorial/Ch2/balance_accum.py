# balance_accum.py
# Print table of compound interest values over time.

def balance_accum(principal, rate, years):
    """Return balance with accumulated compound interest."""
    balance = principal
    for _ in range(years):
        interest = balance * rate
        balance += interest
    return balance

def main():
    print("Calculates compound interest over time.")
    principal = float(input("Principal: "))
    rate = float(input("Interest rate (as a decimal): "))
    years = int(input("Number of years: "))
    for year in range(years + 1):
        print(year, balance_accum(principal, rate, year))
    
main()
