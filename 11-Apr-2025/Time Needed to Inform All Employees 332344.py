# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        visited = set()
        res = 0
        grid = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] >= 0:
                grid[manager[i]].append(i)
        def get_neighbor(idx):
            return grid[idx]
        def rec(idx,count):
            nonlocal res
            if idx not in visited:
                visited.add(idx)
            
            for neighbor in get_neighbor(idx):
                if neighbor not in visited:
                    rec(neighbor,count + informTime[neighbor])
                res = max(res,count)
        
        rec(headID,informTime[headID])

        return res