# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        sort_ = sorted(edges,key=lambda x:x[0],reverse=True)
        type1 = {i:i for i in range(1,n+1)}
        type2 = {i:i for i in range(1,n+1)}
        count = 0
        def find(x,graph):
            while x != graph[x]:
                graph[x] = graph[graph[x]]
                x = graph[x]
            return graph[x]
        def union(x,y,types):
            nonlocal count
            if types == 1 or types == 3:
                root1 = find(x,type1)
                root2 = find(y,type1)
               
            if types == 2 or types == 3:
                root1 = find(x,type2)
                root2 = find(y,type2)
            if root1 == root2:
                count += 1
            
            
            if root1 != root2:
                if types == 1 or types == 3:

                    type1[root1] = root2
                if types == 2 or types == 3:
                    type2[root1] = root2
        for ty,fir,sec in sort_:
           
            union(fir,sec,ty)
        c = 0      
        for idx,val in type1.items():
            if idx == val:
                c += 1
            if c >= 2:
                return -1
        c = 0
        for idx,val in type2.items():
            if idx == val:
                c += 1
            if c >= 2:
                return -1


        return count
            
        
