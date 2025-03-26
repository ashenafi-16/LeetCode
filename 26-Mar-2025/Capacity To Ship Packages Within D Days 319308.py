# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        def checker(mid):
            count_day = 0
            temp = 0
            for i in range(len(weights)):
                if temp + weights[i] > mid:
                    count_day += 1
                    temp = 0
                temp += weights[i]
            return count_day

        while low <= high:
            mid = (low + high)//2
            if checker(mid) < days:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1
