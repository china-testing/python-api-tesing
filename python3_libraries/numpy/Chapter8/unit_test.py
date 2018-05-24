import numpy as np
import unittest


def factorial(n):
   if n == 0:
      return 1

   if n < 0:
      raise ValueError, "Unexpected negative value"

   return np.arange(1, n+1).cumprod()


class FactorialTest(unittest.TestCase):
   def test_factorial(self):
      #Test for the factorial of 3 that should pass.
      self.assertEqual(6, factorial(3)[-1])
      np.testing.assert_equal(np.array([1, 2, 6]), factorial(3))

   def test_zero(self):
      #Test for the factorial of 0 that should pass.
      self.assertEqual(1, factorial(0))

   def test_negative(self):
      #Test for the factorial of negative numbers that should fail.
      # It should throw a ValueError, but we expect IndexError
      self.assertRaises(IndexError, factorial(-10))


if __name__ == '__main__':
    unittest.main()
