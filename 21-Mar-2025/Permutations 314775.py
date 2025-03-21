# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def permutation(idx,temp):
            if len(set(temp)) == len(nums):
                arr.append(temp.copy())
                return 
            if idx >= len(nums):
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                permutation(idx + 1,temp)
                temp.pop()
                permutation(idx + 1,temp)
        permutation(0,[])
        return arr