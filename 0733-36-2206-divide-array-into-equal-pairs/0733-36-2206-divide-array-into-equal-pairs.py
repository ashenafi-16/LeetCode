class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for val in count.values():
            if val % 2 != 0:
                return False
        return True