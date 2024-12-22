class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] - 1
        nums.sort(reverse=True)
        return nums[0]*nums[1]