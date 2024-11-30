class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        count ,found= 0,False
        char_count = defaultdict(int)
        for i in s:
            char_count[i]+=1
            
        for value in char_count.values():
            if value % 2 == 0:
                count += value
            else:
                count += value -1
                found = True
                
        if found:
            return count + 1
        return count