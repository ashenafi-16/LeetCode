# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =  1
        high = max(piles)
        def checker(mid):
            count = 0
            for val in piles:
                count += (math.ceil(val/mid))
            return count
        while low <= high:
            mid = (low + high)//2
            if checker(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1


