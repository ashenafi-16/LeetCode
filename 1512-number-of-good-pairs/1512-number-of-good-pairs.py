class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = Counter()
        count = 0
        for i in range(len(nums)):
            if nums[i] in num_count:
                count += num_count[nums[i]]
            num_count[nums[i]] += 1
        return count
