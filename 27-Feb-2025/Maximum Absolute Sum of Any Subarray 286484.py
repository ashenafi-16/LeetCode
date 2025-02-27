# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        maxim = max(nums)
        minn = min(nums)
       
        if minn < 0 and maxim < 0:
            return abs(minn)
        if minn > 0 and maxim > 0:
            return maxim
        return abs(maxim-minn)