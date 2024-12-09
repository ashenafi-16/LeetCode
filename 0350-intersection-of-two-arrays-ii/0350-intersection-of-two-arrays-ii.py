class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        num_count = defaultdict(int)
        for i in nums2:
            num_count[i] += 1
        left = 0
        for right in range(len(nums1)):
            if nums1[right] not in num_count:
                continue
            
            nums1[left] = nums1[right]
            num_count[nums1[left]] -= 1
            if num_count[nums1[left]] == 0:
                del num_count[nums1[left]]
            left += 1
        return nums1[:left]
            