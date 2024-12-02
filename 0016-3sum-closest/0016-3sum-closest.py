class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i+ 1,len(nums) - 1
            while left < right:
                three_sum = nums[right] + nums[left] + nums[i]
                if abs(three_sum - target) < abs(closest - target):
                    closest = three_sum
                if three_sum > target:
                    right -= 1
                elif three_sum < target:
                    left += 1
                else:
                    return three_sum
                
        return closest

