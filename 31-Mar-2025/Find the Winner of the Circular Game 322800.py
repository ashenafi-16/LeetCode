# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def recursive(k,n):
            if n == 1:
                return 0
            return (recursive(k,n-1) + k) % n
        return recursive(k,n) + 1
        