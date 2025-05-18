# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1,xor = 0,0
        if len(nums1) & 1 != 0:
            for val in nums2:
                xor1 ^= val
        if len(nums2) & 1 != 0:
            for val in nums1:
                xor ^= val
        return xor1 ^ xor