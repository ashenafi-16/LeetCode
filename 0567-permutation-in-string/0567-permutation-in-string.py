class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_count = Counter(s1)
        window_count = Counter()
        left = 0
        for i in range(len(s2)):
            window_count[s2[i]] += 1
            if i >= len(s1) - 1:
                if window_count == s1_count:
                    return True
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1
        return False
