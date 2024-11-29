class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left < right:
                triplet_sum = nums[left]+nums[right]+nums[i]
                if triplet_sum == 0:
                    res.append([nums[left],nums[right],nums[i]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
            
                elif triplet_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res