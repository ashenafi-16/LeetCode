# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        rem = right - left
        res = right & left
        ans = 0
        for i in range(32):
            if res & (1 << i):
                if 2 ** i <= rem:
                    pass
                else:
                    ans += 2 ** i
        return ans


