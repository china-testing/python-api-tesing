# factorial.py

def factorial(n):
    """Return n! = 1*2*3*...*n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    for n in range(20):
        print(n, factorial(n))
    print(factorial(2000))

main()
