# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low  = 0
        high = len(nums)-1
        res = float('inf')
        while low <= high:
            mid = (low + high) //2
            
            if nums[mid] >= nums[low] and nums[mid] >= nums[high]:
                
                low = mid + 1
            else:
                
                high = mid - 1
            res = min(nums[mid],res)
            
        return res
    
    