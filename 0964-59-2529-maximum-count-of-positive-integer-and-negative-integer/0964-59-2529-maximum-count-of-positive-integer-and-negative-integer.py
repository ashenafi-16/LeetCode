class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = 0 
        neg = 0
        while l < len(nums) and nums[l] <= 0:
            if nums[l] < 0:
                neg += 1
            l += 1
        pos = len(nums) - l
        return max(pos,neg)