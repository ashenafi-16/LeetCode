# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        arr_i = nums[0]
        for i in range(1,len(nums)+1):
            total = total ^ i
            if i < len(nums):
                arr_i = arr_i ^ nums[i]

        return arr_i ^ total