# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low  = min(ranks)
        high = (cars ** 2) * max(ranks)
        def checker(mid):
            count = 0
            for val in ranks:
                count += floor(sqrt(mid/val))
            return count
        while low <= high:
            mid = (low + high) //2
            if checker(mid) >= cars:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1
