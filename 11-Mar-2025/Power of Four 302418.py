# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def fact(n):  
            if n == 1:
                return True
            elif n < 1:
                return False
            return fact(n/4)
        return fact(n)
        
       