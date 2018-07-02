'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):
            if n == 0 or x == 1:
                return 1
            if x == 0:
                return 0
            if n % 2 == 1:
                return x * power(x*x, n//2)
            else:
                return power(x*x, n//2)
        return power(x, n) if n >= 0 else 1 / power(x, -n)