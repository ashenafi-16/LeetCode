class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        total = 0
        for idx,val in num_count.items():
            if val==1:
                total += idx
        return total