class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        from collections import defaultdict
        count_num = defaultdict(int)
        nums.sort()
        left,right = 0 ,len(nums) - 1
        while left < right:
            cur_ave = round((nums[left] + nums[right])/2,1)
            count_num[cur_ave] += 1
            left += 1
            right -= 1
        return len(count_num)