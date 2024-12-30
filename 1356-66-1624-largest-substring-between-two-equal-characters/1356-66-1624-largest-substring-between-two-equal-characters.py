class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    
        char_occur = {}
        longest_sub = -1
        for idx,char in enumerate(s):
            if char in char_occur:
                longest_sub = max(longest_sub,idx - char_occur[char] - 1)
            else:
                char_occur[char] = idx
        return longest_sub