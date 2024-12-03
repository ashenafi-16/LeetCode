class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                length = end - start + 1

                if l <= length <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)

                if length > r:
                    break

        return min_sum if min_sum != float('inf') else -1