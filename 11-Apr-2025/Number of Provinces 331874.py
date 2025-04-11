# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        grid = defaultdict(list)
        stk = []
        visit = set()
        component = 0
        def get_neighbor(node):
            return grid[node]

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    grid[i].append(j)

        def rec(node):
           
            if node not in visit:
                visit.add(node)

            for neighbor in get_neighbor(node):
                if neighbor not in visit:
                    rec(neighbor)

        for node,val in grid.items():
            if node in visit:
                continue
            component += 1
            
            rec(node)
        return component
            