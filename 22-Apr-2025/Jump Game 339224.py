# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = nums[0]
        i = 0
        l = 0
        while i < len(nums):
            
            cur = max((nums[i] + i),cur)
            
            print(i,cur,l)
            if l > i:
                return False
            if cur >= len(nums)- 1:
                
                return True
            
            
            if i < cur:
                i += 1
            l += 1
        return False
            

            