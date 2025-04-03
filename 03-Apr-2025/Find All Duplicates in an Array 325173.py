# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        left = 0
        res = []
        n = len(nums)
        while left < n:
            pos = nums[left] - 1
            if pos != left:
                nums[pos],nums[left] = nums[left],nums[pos]
                if nums[pos] == nums[left]:
                    left += 1
                
            else:
               
                left += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
        return res
       
    
