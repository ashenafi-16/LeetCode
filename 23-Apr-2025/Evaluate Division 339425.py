# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        count = defaultdict(list)
        ite = 0                
        for idx,(fir ,sec) in enumerate(equations):
            count[fir].append((sec, values[idx]))
            count[sec].append((fir,(1/values[idx])))
        ans = []
        def dfs(fir,sec,visited):
            if fir not in count or sec not in count:
                return -1
            if fir == sec:
                return 1
            visited.add(fir)
            for neigh,val in count[fir]:
                if neigh in visited:
                    continue
                res = dfs(neigh,sec,visited)
                if res != -1:
                    return res * val
            return -1  


        for fir ,sec in queries:
            ans.append(dfs(fir,sec,set()))
        return ans