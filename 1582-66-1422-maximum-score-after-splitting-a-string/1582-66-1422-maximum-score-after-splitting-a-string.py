class Solution:
    def maxScore(self, s: str) -> int:
        ones_count = s.count('1')
        zeros_count = 0
        max_val = 0
        for i in range(len(s)-1):
            if s[i] == '1':
                ones_count -= 1
            else:
                zeros_count += 1
            max_val = max(max_val , ones_count + zeros_count)
        return max_val