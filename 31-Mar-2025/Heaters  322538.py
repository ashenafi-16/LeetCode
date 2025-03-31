# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        for house in houses:
            position = bisect.bisect_left(heaters,house)
            
            left_dist = house - heaters[position - 1] if position - 1 >= 0 else math.inf
            right_dist = heaters[position] - house if position < len(heaters) else float('inf')

            min_dist = min(left_dist,right_dist)
            res = max(res,min_dist)
        return res

