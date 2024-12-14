class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
     num_count = {}
     for i in range(len(nums)):
        if nums[i] not in num_count:
            num_count[nums[i]] = i
        else:
            if abs(i - num_count[nums[i]]) <= k:
                return True
            else:
                num_count[nums[i]] = i
     return False