# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        rem = right - left
        res = right & left
        ans = 0
        
        t = int(math.log2(res)) if res != 0 else 0
        
        for i in range(t+1):
            if res & (1 << i):
                if 2 ** i > rem:
                    ans += 2 ** i
        return ans


