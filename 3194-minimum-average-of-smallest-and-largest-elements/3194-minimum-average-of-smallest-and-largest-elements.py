class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        res = []
        left,right = 0,len(nums)-1
        while left < right:
            res.append((nums[left] + nums[right])/2)
            left += 1
            right -= 1
        minimum = round(min(res),1)
        return minimum