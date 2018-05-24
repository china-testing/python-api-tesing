import numpy as np

def factorial(n):
   """
   Test for the factorial of 3 that should pass.
   >>> factorial(3)
   6

   Test for the factorial of 0 that should fail.
   >>> factorial(0)
   1
   """
   return np.arange(1, n+1).cumprod()[-1]
