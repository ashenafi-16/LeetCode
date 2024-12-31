class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]*len(nums)
        rightsum = [0]*len(nums)
        for i in range(1,len(nums)):
            leftsum[i] = leftsum[i-1] + nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            rightsum[i] = rightsum[i+1] + nums[i+1]
        for i in range(len(nums)):
            nums[i] = abs(leftsum[i] - rightsum[i])
        return nums