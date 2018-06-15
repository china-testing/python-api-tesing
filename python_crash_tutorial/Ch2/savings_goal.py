# savings_goal.py
# Use accum to determine number of years until goal.

def years_to_goal(principal, rate, goal):
    """Return number of years to reach savings goal."""
    balance = principal
    years = 0
    while balance < goal:
        interest = balance * rate
        balance += interest
        years += 1
    return years

def main():
    print("Calculates number of years to reach goal.")
    principal = float(input("Principal: "))
    rate = float(input("Interest rate (as a decimal): "))
    goal = float(input("Desired balance: "))
    print("The goal is reached in",
          years_to_goal(principal, rate, goal), "years.")
    
main()
