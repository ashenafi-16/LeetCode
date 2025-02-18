# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mapping = {0:1}
        res = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            diff = cur_sum - goal
            if diff in mapping:
                res += mapping[diff]
            if cur_sum not in mapping:
                mapping[cur_sum] = 1
            else:
                mapping[cur_sum] = mapping[cur_sum] + 1
        return res