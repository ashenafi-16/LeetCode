# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
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
                res.append(i+1)
        return res
       
    