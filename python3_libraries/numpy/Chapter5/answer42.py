from __future__ import print_function
import numpy as np

def ultimate_answer(a):
   result = np.zeros_like(a)
   result.flat = 42

   return result

ufunc = np.frompyfunc(ultimate_answer, 1, 1) 
print("The answer", ufunc(np.arange(4)))

print("The answer", ufunc(np.arange(4).reshape(2, 2)))
