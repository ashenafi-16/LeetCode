class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        char_count = defaultdict(int)
        left = 0
        max_count = 0
        for i in range(len(s)):
            char_count[s[i]] += 1
            while max(char_count.values()) > 2:
                char_count[s[left]] -= 1
                left += 1
            max_count = max(max_count,i-left+1)
        return max_count

