# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = int(math.log2(10 ** 9))
        pre_ = [[0] * (n+1) for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(n+1):
                if nums[i] & (1 << j):
                    pre_[i][j] = 1
            if i > 0:
                for j in range(n+1):
                    pre_[i][j] += pre_[i-1][j]
        length = 0
        left = 0
        right = 0
        
        while left <= right and right < len(pre_):
            cond = True
            for i in range(n+1):
                previous = pre_[left-1][i] if left - 1 >= 0 else 0
                if pre_[right][i] - previous > 1:
                    cond = False
                    
                    break
            if cond:
                length = max(length,right - left + 1)
                right += 1
            else:
                left += 1
        return length