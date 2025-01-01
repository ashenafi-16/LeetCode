class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count_negative = 0
        for nums in grid:
            for num in nums:
                if num < 0:
                    count_negative += 1
        return count_negative