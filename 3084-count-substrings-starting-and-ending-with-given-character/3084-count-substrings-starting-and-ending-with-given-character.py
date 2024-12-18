class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        ch_count = s.count(c)
        return (ch_count * (ch_count + 1)//2)

    
