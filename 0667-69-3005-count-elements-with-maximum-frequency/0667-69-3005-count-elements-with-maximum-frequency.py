class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        max_freq_count = 0
        max_freq_val = max(num_count.values())
        for val in num_count.values():
            if max_freq_val == val:
                max_freq_count += val
        return max_freq_count