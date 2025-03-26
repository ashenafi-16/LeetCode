# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        low = -1
        high = len(queries) - 1
        def checker(mid):
            pre_sum = [0] * (len(nums) + 1)
            for i in range(mid):
                sec = (queries[i][1] + 1)
                pre_sum[queries[i][0]] += queries[i][2] 
                pre_sum[sec] -= queries[i][2] 
            for i in range(len(nums)):
                pre_sum[i] = pre_sum[i] + pre_sum[i - 1] if i- 1 >= 0 else pre_sum[i]
                if nums[i] > pre_sum[i]:
                    return False
            return True
        while low <= high:
            mid = (low + high)//2
            if checker(mid + 1):
                high = mid - 1
                
            else:
                low = mid + 1
        return low + 1  if low < len(queries) else -1