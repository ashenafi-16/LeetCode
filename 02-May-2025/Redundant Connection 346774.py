# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {i:i for i in range(1,n+1)}  
        size = [1] * len(edges) 
        def find(x):
            if x == graph[x]:
                return x
            return find(graph[x])
        def union(x,y):
            root1 = find(x)
            root2 = find(y)
            if root1 == root2:
                return True
            else:
                if size[root1-1] > size[root2-1]:

                    graph[root1] = root2
                    size[root1-1] += size[root2-1]
                else:
                    graph[root2] = root1
                    size[root2-1] += size[root1-1]

                    
        
        for fir ,sec in edges:
            if union(fir,sec):
                return [fir,sec]
          
        return []