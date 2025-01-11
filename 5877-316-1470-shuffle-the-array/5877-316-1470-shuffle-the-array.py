class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0]*len(nums)
        i = 0
        r = len(nums)//2
        l = 0
        while i < len(nums):
            res[i] = nums[l]
            i += 1
            res[i] = nums[r]
            i += 1
            r += 1
            l += 1
        return res