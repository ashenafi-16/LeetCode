# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        array = []

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                a = abs(points[j][0] - points[i][0])
                b = abs(points[j][1] - points[i][1])
                array.append((a+b,i,j))
        graph = {i:i for i in range(len(points))}
        total = 0
        array.sort()
        def find(x):
            while x != graph[x]:
                graph[x] = graph[graph[x]]
                x = graph[x]
            return graph[x]
        
        def union(val,x,y):
            root1 = find(x)
            root2 = find(y)
            nonlocal total
            if root1 != root2:
                total += val
            graph[root1] = root2
        for weight,fir,sec in array:
            union(weight,fir,sec)
        return total


        
                
    




