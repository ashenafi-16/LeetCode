# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_c = 0 
        l_c = 0
        count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l_c += 1
            else:
                r_c += 1
            if l_c == r_c:
                count += 1
        return count
