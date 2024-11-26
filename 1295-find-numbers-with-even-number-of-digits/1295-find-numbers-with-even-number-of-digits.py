class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for right in nums:
            if len(str(right)) %2 == 0:
                count += 1
        return count

