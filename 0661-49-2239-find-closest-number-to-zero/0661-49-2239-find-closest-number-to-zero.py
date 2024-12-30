class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum = index = float("inf")
        copy = [0]* len(nums)
        
        for i in range(len(nums)):
            copy[i] = abs(nums[i])
            if minimum > copy[i]:
                minimum = copy[i]
                index = i
        minimum = nums[index]
        if minimum < 0 and abs(minimum) in nums:
            return abs(minimum)

        return minimum            