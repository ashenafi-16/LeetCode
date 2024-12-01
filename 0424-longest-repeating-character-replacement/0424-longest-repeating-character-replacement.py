class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        c = defaultdict(int)
        count_max = max_count = left = 0
        for right in range(len(s)):
            c[s[right]] += 1
            
            count_max = max(count_max,c[s[right]])
            while (right - left + 1) - count_max > k:
                c[s[left]] -= 1
                left += 1
            max_count = max(max_count,right - left +1)
        return max_count
                