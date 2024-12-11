class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_num = float("-inf")
        nums.sort()
        left,right = 0,len(nums)-1
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum > max_num:
                max_num = cur_sum
            left += 1
            right -= 1
        return max_num