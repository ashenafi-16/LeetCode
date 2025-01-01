class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c_R = 0
        c_L = 0
        count = 0 
        for r in range(len(s)):
            if s[r] == 'R':
                c_R += 1
            else:
                c_L += 1
            if c_R == c_L:
                count += 1
                c_R = 0
                c_L = 0
        return count
