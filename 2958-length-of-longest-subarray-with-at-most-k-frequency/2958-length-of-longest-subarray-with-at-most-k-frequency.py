class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        count_num = defaultdict(int)
        max_count = 0
        left= 0
        for right in range(len(nums)):
            count_num[nums[right]] += 1
        
            while count_num[nums[right]] > k:
                
                count_num[nums[left]] -= 1
                left += 1
                      
            max_count = max(max_count,right - left + 1)
        return max_count