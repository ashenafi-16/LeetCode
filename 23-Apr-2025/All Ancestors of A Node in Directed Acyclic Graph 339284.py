# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        count  = defaultdict(list)
        res = [[] for i in range(n)]
        for fir,sec in edges:
            count[sec].append(fir)
        def get_neighbor(node):
            return count[node]
        def rec(key):
            
            nonlocal visited
            nonlocal result
            if key not in visited:
                visited.add(key)
            for neighbor in get_neighbor(key):
                if neighbor not in visited:
                    result.append(neighbor)
                    rec(neighbor)
        for key in range(n):
            visited = set()
            result = []
            rec(key)
            result.sort()
            res[key] = result
        return res


        