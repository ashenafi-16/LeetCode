class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        count_t = defaultdict()
        diff = 0
        for i in range(len(t)):
            count_t[t[i]] = i
        for i in range(len(s)):
            diff += abs(count_t[s[i]] - i)
        return diff
