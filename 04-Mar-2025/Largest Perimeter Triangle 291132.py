# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = 0
        for i in range(1,len(nums)-1):
            three_sum = nums[i] + nums[i+1] + nums[i-1]
            if nums[i] + nums[i+1] > nums[i-1]:
                if three_sum > perimeter:
                    perimeter = three_sum
        return perimeter
