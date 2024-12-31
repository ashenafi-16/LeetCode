class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):    
            l = i + 1
            while l < len(nums):
                if nums[l] + nums[i] < target:
                    count += 1
                l += 1
        return count