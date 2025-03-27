# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        def helper(mid):
            count  = 0
            for val in candies:
                count += floor(val/mid)
                    
            return count
        low = 1
        high = max(candies)
        while low <= high:
            mid = (low + high)//2
            if helper(mid) >= k :
                low = mid  + 1
            else:
                high = mid - 1
        return high