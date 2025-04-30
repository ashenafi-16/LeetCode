# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        ans = []
        for i in range(len(grid)):
            heap_val = []
            for j in range(len(grid[i])):
                heappush(heap_val,grid[i][j])
            
            
            
            ans.extend(nlargest(limits[i],heap_val))
        heapify(ans)
        return sum(nlargest(k,ans))
