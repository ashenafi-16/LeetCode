class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left  = 0
        min_index = float('inf')
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_index = min(min_index, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return min_index if min_index != float('inf') else 0 
