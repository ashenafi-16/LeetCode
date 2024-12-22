class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)-1
        return nums[0]*nums[1] - nums[n] * nums[n-1]