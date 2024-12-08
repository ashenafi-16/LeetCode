class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n = len(nums)
        nums = Counter(nums)
        res = []
        for idx,val in nums.items():
            if val > n//3:
                res.append(idx)
        return res