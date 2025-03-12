# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n): 
            if n == 0:
                return 1
            val = power(x,n//2)
            if n % 2 == 0:
                return val * val
            else: 
                return x * val * val
        if n < 0:
            return 1/power(x,abs(n))
        return power(x,n)