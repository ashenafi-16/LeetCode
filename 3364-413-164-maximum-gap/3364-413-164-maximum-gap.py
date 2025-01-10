class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        if len(nums) < 2:
            return maximum
        for i in range(1,len(nums)):
            diff = abs(nums[i] - nums[i-1])
            if diff > maximum:
                maximum = diff
        return maximum
        