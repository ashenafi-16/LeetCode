# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0] * len(nums)
        for(i,val) in enumerate(requests):
            pre[val[0]] += 1
            if val[1] + 1 < len(nums):
                pre[val[1] + 1] -= 1  
        for i in range(1,len(pre)):
            pre[i] = pre[i] + pre[i-1]
        nums.sort()
        pre.sort()
        total = 0
        for i in range(len(pre)):
            total += pre[i] * nums[i]
        return (total % (10 ** 9 + 7))


