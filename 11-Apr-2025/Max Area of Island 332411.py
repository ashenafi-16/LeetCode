# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visit =set()
        def rec(i,j):
            nonlocal count
            if i >= len(grid) or j >= len(grid[i]) or i < 0 or j < 0 or grid[i][j] == 0 or (i,j) in visit:
                return 0
            else:
                count += 1
            visit.add((i,j))
            rec(i + 1,j)
            rec(i - 1,j)
            rec(i,j + 1)
            rec(i,j - 1)
            return count
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count = 0
                if grid[i][j] == 1:
                    res = max(res,rec(i,j))
        return res
