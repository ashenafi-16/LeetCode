class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        result = []
        if len(nums) == 1:
            result.append(f"{nums[0]}")
            return result
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1] + 1:
                if right - left > 1:
                    result.append(f"{nums[left]}->{nums[right-1]}")
                else:
                    result.append(f"{nums[right-1]}")
                left = right
            if right == len(nums) -1:
                if right - left >= 1:
                    result.append(f"{nums[left]}->{nums[right]}")
                else:
                    result.append(f"{nums[right]}")
                
        return result
