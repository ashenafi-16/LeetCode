# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        value = [0]*len(nums)
        for val in nums:
            value[val-1] = val
        res = []
        for i in range(len(value)):
            if value[i] == 0:
                res.append(i+1)
        return res