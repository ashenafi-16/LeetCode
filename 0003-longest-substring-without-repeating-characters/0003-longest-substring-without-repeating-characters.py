class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_count = 0
        for right in range(len(s)):
            while s[right] in s[left : right]:
                left += 1 
            max_count = max(max_count,right - left +1)
        return max_count 