# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        l = 0
        res  = 0
        r = 0
        if len(happiness) == 0:
            return 0
        temp = happiness[r]
        for i in range(k):
            res += temp
            r += 1
            l += 1
            if r < len(happiness):
                temp = happiness[r] - l
            if temp < 0:
                temp = 0 
        return res

