# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        if not nums:
            return 0
        while k > nums[0]:
            fir = heappop(nums)
            sec = heappop(nums)
            heappush(nums,((min(fir,sec) * 2) + max(fir,sec)))
            count += 1
        return count
