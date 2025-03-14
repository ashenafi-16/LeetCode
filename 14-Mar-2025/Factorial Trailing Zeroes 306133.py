# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def trailing(n):
            if n <= 5:
                return n//5
            
            return n// 5 + trailing(n//5)
        return trailing(n)