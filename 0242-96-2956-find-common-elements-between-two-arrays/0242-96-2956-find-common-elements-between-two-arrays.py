class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 =0 
        answer2 = 0
        for num in nums1:
            if num in nums2:
                answer1 += 1     
        for num in nums2:
            if num in nums1:
                answer2 += 1   
        return [answer1,answer2]   